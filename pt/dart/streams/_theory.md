Um `Future` representa um **único** valor que chega mais tarde. Uma **Stream** representa uma **sequência** de valores que chegam ao longo do tempo: teclas pressionadas, pedaços de um arquivo, mensagens de um servidor. Cada valor é chamado de **evento** e, depois do último evento, a stream está **concluída**.

A forma mais simples de construir uma stream é `Stream.fromIterable`, que emite cada elemento de uma lista, um após o outro:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

Para consumir os eventos um a um você usa um laço **`await for`**. Como `await`, ele só é permitido dentro de uma função marcada com `async`, então `main` passa a ser `Future<void> main() async`. O corpo do laço roda uma vez por evento e o laço termina quando a stream está concluída:

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

Um laço `for` comum não funciona aqui: uma `Stream` não é um `Iterable`, seus valores não estão disponíveis todos de uma vez.

---

`Stream.fromIterable` precisa de todos os valores de antemão. Para **produzir** valores um de cada vez, escreva um **gerador assíncrono**: uma função cujo corpo é marcado com `async*` e cujo tipo de retorno é `Stream<T>`. Dentro dela, `yield` envia um evento para a stream:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

O corpo não roda quando você chama `countTo(3)`: ele roda preguiçosamente, à medida que o ouvinte pede valores, e a stream está concluída quando o corpo termina.

Para juntar todos os eventos em uma `List`, chame `toList()`. Ele retorna um `Future<List<T>>`, então você o aguarda com `await`:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

Um laço `await for` pode fazer mais do que imprimir: ele pode atualizar uma variável declarada antes do laço. Uma função que consome uma stream e calcula um resultado precisa ser marcada com `async`, e retorna um `Future` desse resultado:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

A função só chega ao `return` depois que a stream está concluída, então quem chama recebe o valor final ao aguardar o future:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Toda stream acaba terminando. Em um gerador `async*`, a stream está **concluída** assim que o corpo da função termina, seja porque chegou ao fim, seja porque encontrou um `return`. Um laço `await for` sobre uma stream concluída sai, e qualquer future de `toList()` se completa.

Uma stream não recomeça nem repete seus valores: uma vez concluída, permanece concluída.

---

`await for` pausa a função atual até que a stream esteja concluída. Quando você quer reagir aos eventos **sem esperar**, chame `listen` e passe um callback: ele é invocado uma vez por evento, e o código depois de `listen` roda imediatamente.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` também aceita um parâmetro nomeado `onDone`, uma função sem argumentos chamada quando a stream termina:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

Um gerador `async*` pode repassar **todos os eventos de outra stream** com `yield*` (yield-star). É como um laço `await for` que emite cada valor, em uma única linha:

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

A stream externa continua com seus próprios `yield` assim que a stream interna está concluída.

---

Como `Iterable`, uma `Stream` tem métodos que constroem uma **nova stream** a partir de uma existente:

- `map` transforma cada evento
- `where` mantém apenas os eventos que satisfazem uma condição
- `take` para depois de um dado número de eventos

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

Esses métodos são **preguiçosos**: nada roda até que alguém escute a stream resultante. Eles podem ser encadeados, e a stream de origem nunca é modificada.

---

Como `where`, `map` e `take` retornam cada um uma stream, você pode encadeá-los e terminar com `toList()` para obter o resultado como uma lista. Apenas o `toList()` final precisa de um `await`, já que é a única chamada que retorna um `Future`:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

Além de `toList()`, uma stream oferece outros métodos que **consomem** todos os seus eventos e retornam um único `Future`:

- `first` e `last` se completam com o primeiro ou o último evento
- `length` se completa com o número de eventos
- `join(separator)` se completa com todos os eventos unidos em uma única `String`
- `reduce(combine)` combina os eventos dois a dois em um único valor

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` chama `combine` com o resultado obtido até então e o próximo evento. Ele lança uma exceção se a stream estiver vazia, então use-o apenas quando pelo menos um evento for garantido.

---

Os métodos de `Stream` se dividem em dois grupos:

- métodos de **transformação** como `map`, `where`, `take` e `skip` retornam uma **nova `Stream`** e são preguiçosos: nenhum evento é processado até que a nova stream seja escutada
- métodos de **consumo** como `toList`, `reduce`, `join`, `first`, `last` e `length` escutam a stream e retornam um **`Future`** com o resultado final

Uma cadeia, portanto, é formada por zero ou mais chamadas de transformação seguidas por no máximo uma chamada de consumo.

---

Geradores produzem eventos de dentro de uma função. Quando os eventos vêm de **outro lugar** (um botão, um callback de rede, outro objeto) você precisa de um **`StreamController`**. Ele vive na biblioteca `dart:async`, então o arquivo deve começar com `import 'dart:async';`.

Um controlador é dono de uma stream e permite que você empurre eventos para dentro dela:

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` envia um evento
- `close()` encerra a stream; esquecê-lo significa que os ouvintes esperam para sempre
- `stream` é a `Stream` que os ouvintes consomem

Eventos adicionados antes de alguém escutar são guardados em um buffer, então o código acima é seguro: um ouvinte que chega depois ainda recebe `4` e `2`.

---

Um `StreamController` é frequentemente criado e consumido no mesmo lugar: você se inscreve em `controller.stream` com `listen`, depois adiciona eventos com `add` e fecha o controlador com `close`. Como `listen` não espera, os eventos são entregues depois que o código atual termina, mas sempre na ordem em que foram adicionados:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

As streams vistas até agora são de **inscrição única**: elas permitem exatamente um ouvinte. Chamar `listen`, `await for` ou qualquer método de consumo uma segunda vez lança um `StateError` ("Stream has already been listened to").

Para compartilhar uma stream entre vários ouvintes, converta-a em uma stream **broadcast** com `asBroadcastStream()`:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

Uma stream broadcast não usa buffer: um ouvinte só recebe os eventos emitidos **depois** de ele se inscrever. No exemplo, os dois ouvintes se inscrevem antes do primeiro `await`, então ambos recebem todos os eventos.

---

Um controlador pode criar uma stream broadcast diretamente com o construtor nomeado `StreamController<T>.broadcast()`. Sua `stream` aceita qualquer número de ouvintes, e cada evento é entregue a todos eles, na ordem em que se inscreveram:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

Como toda stream broadcast, ela não usa buffer: eventos adicionados antes de um ouvinte se inscrever são perdidos para esse ouvinte.

---

Uma stream pode carregar **erros** além de valores. Dentro de um gerador `async*`, um `throw` envia um evento de erro e encerra a stream; um `StreamController` pode enviar um com `addError`.

Do lado de quem consome, um laço `await for` relança o erro no ponto onde o laço está, então você o trata com um `try`/`catch` comum em volta do laço:

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

Com `listen`, passe em vez disso um callback `onError`: `stream.listen(print, onError: (e) => print('caught: $e'));`
