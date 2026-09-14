Cada linha de Dart que você escreveu até agora roda dentro de um **isolate**: uma thread com sua própria memória e seu próprio event loop. Um programa começa com um isolate, o isolate *main*, e pode iniciar mais.

O que torna os isolates especiais é que eles não compartilham **nada**. Dois isolates nunca veem o mesmo objeto, então não há travas, nem data race, nem valor atualizado pela metade. Eles conversam entre si apenas passando **cópias** de mensagens.

A maneira mais curta de usar um segundo isolate é **`Isolate.run`**. Ele recebe uma função, roda em um isolate totalmente novo e devolve um `Future` com o resultado:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` vive na biblioteca `dart:isolate`, então o arquivo deve começar com `import 'dart:isolate';`. Enquanto o novo isolate calcula, o isolate principal permanece livre: esse é um **paralelismo** real, o trabalho acontece em outro núcleo do processador.

---

A função que você entrega ao `Isolate.run` pode **capturar** variáveis ao redor dela. Esses valores são copiados para o novo isolate junto com a função, então o cálculo pode depender de quem a chamou:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` retorna um `Future` do que quer que a função retorne, então `triple` pode simplesmente retorná-lo: não é preciso `async` nem `await` quando você apenas repassa o future.

O objetivo de mover o trabalho para outro isolate é que cálculos longos não congelem mais o principal. Um laço que roda por um segundo bloqueia tudo quando roda no isolate principal; dentro de `Isolate.run` ele roda em outro lugar e o isolate principal continua tratando seus próprios eventos.

---

Apenas **dados** são copiados entre isolates; **código** não é. Todo isolate de um programa já pode ver todas as funções e classes de nível superior desse programa, então o cálculo entregue ao `Isolate.run` pode chamá-las livremente:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

O que viaja é o `text` capturado na ida e o `int` resultante na volta, cada um uma cópia. O padrão é sempre o mesmo: deixe a função pesada onde ela está e envolva a **chamada** em `Isolate.run`.

---

`await` e `Isolate.run` resolvem dois problemas diferentes, e vale a pena mantê-los separados.

`await` dá a você **concorrência** em um único isolate: enquanto uma função espera por um temporizador ou um servidor, o isolate roda outro código pendente. Nada roda no mesmo instante, o isolate apenas para de ficar ocioso. Essa é a ferramenta certa para esperar.

`Isolate.run` dá a você **paralelismo**: um segundo isolate em um segundo núcleo do processador, rodando seu próprio código no mesmo instante que o primeiro. Essa é a ferramenta certa para calcular.

```dart
await Future.delayed(const Duration(seconds: 1)); // waiting: no core is busy
await Isolate.run(() => hugeCalculation());       // computing: another core is busy
```

Colocar `await` em um cálculo lento não ajuda em nada: `await bigSum()` ainda roda `bigSum` no isolate atual e o bloqueia até a última linha. Apenas um segundo isolate tira esse trabalho de lá.

---

`Isolate.run` é o atalho para um único resultado. Quando você quer um isolate que continua rodando e responde mais de uma vez, inicie-o você mesmo com **`Isolate.spawn`** e dê a ele um jeito de responder.

Esse jeito é um par de portas. Uma **`ReceivePort`** é uma caixa de correio: você a cria do seu lado e lê as mensagens que chegam. Seu **`sendPort`** é o endereço dessa caixa de correio, e é a única coisa de que o outro isolate precisa para responder.

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` recebe a função a rodar e a única mensagem a passar a ela, aqui o `SendPort`. Do outro lado, `send` solta um valor na caixa de correio, e `await receivePort.first` espera a primeira mensagem e fecha a porta.

---

A função entregue ao `Isolate.spawn` é chamada de **ponto de entrada**. Ela deve ser uma função de nível superior (ou estática) que recebe exatamente um parâmetro: a mensagem que o `Isolate.spawn` passa a ela.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

As mensagens que chegam a uma `ReceivePort` têm o tipo estático `dynamic`, porque qualquer valor pode ter sido enviado. Quando você sabe o que o outro isolate envia, faça um cast:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

Um isolate iniciado sempre segue os mesmos quatro passos: abrir a caixa de correio, iniciar o worker com seu endereço, esperar a resposta, usá-la.

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

O `await` na frente de `Isolate.spawn` espera o isolate *iniciar*, não que ele termine seu trabalho: o resultado chega depois, pela porta.

---

`Isolate.spawn` passa exatamente **uma** mensagem ao ponto de entrada, e o worker geralmente precisa tanto de um `SendPort` para responder quanto de alguns dados para trabalhar. O truque usual é agrupar tudo em uma `List` e desempacotar do outro lado:

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

A lista é copiada na ida, então o worker lê seus próprios valores. Um `SendPort` é uma das poucas coisas que não são copiadas, mas compartilhadas: ele continua apontando para a caixa de correio do isolate que o criou, e é exatamente por isso que pode ser usado como endereço de retorno.

---

`first` lê uma mensagem e fecha a caixa de correio. Uma `ReceivePort` também é uma **`Stream`**, então para ler muitas mensagens você itera sobre ela com `await for`.

O laço nunca termina por si só: a porta fica aberta esperando uma mensagem que pode nunca chegar. Por isso o worker envia um último valor como sinal, geralmente `null`, e o ouvinte reage chamando **`close()`**, que encerra a stream e o laço:

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

Coletar uma série inteira de mensagens segue uma receita: uma lista vazia antes do laço, um `add` por mensagem real, e `close()` no sinal que encerra a stream. Uma vez fechada a porta, o `await for` termina e a função pode retornar:

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

As mensagens mantêm a ordem em que foram enviadas, então a lista que você constrói espelha o trabalho do outro isolate passo a passo.

---

Uma `ReceivePort` aberta conta como trabalho pendente: enquanto uma existir, o isolate que a possui tem um motivo para permanecer vivo e seu event loop continua esperando uma mensagem. Em um programa de linha de comando, um isolate principal com uma porta aberta simplesmente **nunca sai**, e você precisa pará-lo manualmente.

Fechar a porta é, portanto, parte do trabalho, não uma otimização:

- `await port.first` a fecha para você após uma mensagem
- `port.close()` a fecha explicitamente, que é o que você precisa depois de um laço `await for`

`Isolate.run` não tem nada dessa burocracia: ele cria as portas, as fecha e desliga o isolate para você. Prefira-o sempre que um único resultado for tudo de que você precisa.

---

Uma exceção lançada dentro de um isolate não pode pular para outro: os dois têm pilhas separadas. O `Isolate.run` fecha essa lacuna para você capturando o erro, copiando-o de volta e fazendo o future retornado falhar com ele. Do seu lado, portanto, ele é um erro assíncrono comum, capturado com `try`/`catch` ao redor do `await`:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

O `await` dentro do `try` importa, exatamente como com qualquer outro future: sem ele o future deixaria o bloco `try` inacabado e o `catch` nunca rodaria.

Com `Isolate.spawn` não existe essa ponte. Um erro não capturado mata o isolate iniciado silenciosamente e o pai continua esperando uma mensagem que nunca chegará, o que é mais um motivo para recorrer a `Isolate.run` primeiro.

---

O erro que volta do `Isolate.run` é uma **cópia** do que foi lançado do outro lado, então as verificações usuais continuam funcionando: `catch (e)` lhe dá o objeto, e `e is FormatException` diz que tipo de falha foi.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

Em que você não pode confiar é no stack trace apontando para o seu próprio isolate: o erro viajou, a pilha não.

---

Posto tudo junto, um programa com `Isolate.run` se lê como código sequencial comum: a linha antes da chamada roda no isolate principal, o cálculo roda em outro lugar, e a linha depois do `await` roda de volta no isolate principal com o resultado em mãos.

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

Como os isolates não compartilham memória, toda mensagem é **copiada** quando atravessa. Números, booleanos, strings, `null`, listas, mapas e a maioria dos objetos simples podem fazer a viagem; algumas coisas não podem ser copiadas de forma alguma, como um socket aberto, e tentar enviar uma delas lança um `ArgumentError`.

A consequência é a regra que torna os isolates seguros: depois do envio, os dois lados têm **dois objetos independentes**. O que quer que um isolate faça com sua cópia é invisível ao outro.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // the copy grows
print(numbers);                           // [1, 2, 3]
```

`SendPort` é a exceção que confirma a regra: ele é compartilhado em vez de copiado, precisamente para que possa continuar apontando para a caixa de correio original.

---

Cada `Isolate.run` inicia seu próprio isolate, então vários deles realmente rodam no mesmo instante, em tantos núcleos quanto a máquina tiver. O padrão é o que você já conhece dos futures: inicie cada cálculo primeiro, depois espere por todos com `Future.wait`, que mantém os resultados na ordem da entrada.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Iniciar um isolate não é de graça: custa memória e alguns milissegundos. Dividir um cálculo longo entre um punhado de isolates compensa; enviar mil adições triviais a mil isolates não compensa.
