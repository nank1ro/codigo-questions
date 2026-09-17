Algumas instruções não podem ser executadas: ler um texto que não é um número, pegar um elemento além do fim de uma lista, pedir o primeiro item de uma lista vazia. Quando isso acontece, o Dart **lança** um objeto que descreve a falha.

Você mesmo pode lançar um com a palavra-chave `throw`. `Exception('message')` constrói um objeto pronto que carrega uma explicação curta:

```dart
throw Exception('no fuel');
```

Um lançamento não é um `return`. Ele abandona a instrução, a função e todo chamador acima dela, procurando algo que trate a falha. Quando nada faz isso, o programa para e imprime a falha:

```
Unhandled exception:
Exception: no fuel
```

Tudo depois do lançamento é pulado, então as linhas que rodariam nunca rodam. É disso que trata este tópico: decidir onde uma falha é tratada em vez de deixá-la encerrar o programa.

---

Para manter o programa vivo, envolva a instrução arriscada em um bloco `try` e descreva a recuperação em um bloco `catch`:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` lança quando o texto não descreve um número inteiro. O Dart sai do bloco `try` na primeira instrução que lança, pula o restante dele, executa o bloco `catch` e então segue com o código que vem depois. A variável entre parênteses, `e` aqui, é o próprio objeto lançado.

Nada dentro do bloco `try` é desfeito, então mantenha-o tão curto quanto a falha que você espera.

---

Um `catch` simples captura tudo, o que também esconde as falhas que você não planejou. Para tratar exatamente um tipo, nomeie o tipo dele em uma cláusula `on`:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` lança uma **`FormatException`** quando o texto não é um número inteiro, então esse é o tipo a nomear ao ler entrada. Uma cláusula `on` corresponde a esse tipo e aos subtipos dele, e a nada mais: qualquer outra falha continua se propagando para fora e ainda aparece, em vez de ser engolida por uma recuperação que nunca foi feita para ela.

---

Um bloco `try` pode ser seguido por **várias** cláusulas, cada uma se recuperando de uma falha diferente. O Dart compara o objeto lançado com elas de cima para baixo e executa a **primeira** que corresponde:

```dart
try {
  return names[int.parse(text)];
} on FormatException {
  return 'not a number';
} on RangeError {
  return 'out of range';
} catch (e) {
  return 'unknown problem';
}
```

Ler uma lista com um índice que não existe lança um **`RangeError`**, então as duas falhas dessa única linha recebem respostas diferentes.

Como a primeira correspondência vence, a ordem importa: uma cláusula para um tipo geral colocada acima de uma mais específica sempre venceria, deixando a cláusula específica inalcançável. Escreva as cláusulas específicas primeiro, e um `catch` simples por último se você quiser uma rede de segurança.

A cláusula `on RangeError` acima está aqui apenas para mostrar como várias cláusulas são ordenadas. Um `RangeError` sinaliza um erro no código em vez de uma condição que o programa não podia controlar, e um exercício posterior explica por que essa falha deve ser prevenida em vez de capturada.

---

Muitas vezes a recuperação não precisa do objeto lançado: o tipo já diz tudo. Nesse caso, descarte a parte `catch` e mantenha apenas a cláusula `on`:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

As duas formas diferem apenas em se você recebe uma variável:

- `on FormatException catch (e)` — corresponde a esse tipo e te dá o objeto como `e`
- `on FormatException` — corresponde a esse tipo, sem variável
- `catch (e)` — corresponde a tudo e te dá o objeto

Omitir uma variável não usada mantém o tratamento honesto sobre o que ele realmente usa.

---

Um terceiro bloco pode seguir os blocos de tratamento. O `finally` executa **em todos os casos**: depois que o bloco `try` termina normalmente, depois que um bloco de tratamento recupera, e também quando nada corresponde e a falha ainda está se propagando para fora.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

Ele roda até antes de um `return` entregar o valor de volta, e é por isso que a mensagem acima é impressa antes de o chamador ver o resultado. Isso torna o `finally` o lugar para o trabalho que deve acontecer de qualquer forma, como fechar o que você abriu.

---

Seu próprio código lança da mesma forma que a biblioteca. `Exception('message')` constrói uma exceção simples que carrega uma explicação curta, e o `throw` a envia a caminho:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

A mensagem não se perde: `toString()` junta a palavra `Exception`, dois-pontos e a mensagem, que é exatamente o que o relatório de exceção não tratada imprime.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Lançar é melhor do que retornar um valor inventado como `-1`: o chamador não pode esquecer de olhar para ele, e o motivo viaja junto.

---

Às vezes um bloco de tratamento não é o lugar certo para se recuperar: você só quer *notar* a falha e deixá-la continuar para o chamador que realmente pode lidar com ela. A palavra-chave `rethrow` faz isso, dentro de um bloco `catch` ou `on ... catch`:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` envia o **mesmo** objeto adiante, então o chamador vê a falha original. Escrever `throw e` em vez disso também funcionaria, mas reinicia a jornada e perde onde a falha aconteceu primeiro.

Um bloco `finally` na mesma instrução ainda roda, mesmo na saída.

---

Uma cláusula `catch` aceita um **segundo** parâmetro:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

O primeiro é o objeto lançado, o segundo é um `StackTrace`: a cadeia de chamadas que estavam em execução no momento do lançamento. Ele responde *de onde* a falha veio, o que a mensagem sozinha raramente faz.

Um stack trace lista nomes de arquivos, números de linha e frames, e muda com o build e o caminho de chamadas. Imprima-o, anexe-o a um relatório, repasse-o — mas nunca o compare com um texto fixo, e nunca construa o comportamento do programa sobre o conteúdo dele. Peça-o apenas quando for registrá-lo.

---

`Exception` é uma interface, então a sua própria classe pode ser uma. Uma exceção personalizada dá à falha um nome que uma cláusula `on` pode selecionar, e campos que um bloco de tratamento pode ler:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Três partes valem a pena manter: `implements Exception` para que a classe pertença junto das outras falhas, um campo `final` carregando o detalhe, e um `toString()` sobrescrito para que o relatório de exceção não tratada seja legível. Sem essa sobrescrita, o Dart imprime o nome puro da classe e o detalhe se perde.

---

O Dart lança duas famílias de objetos, e elas significam coisas opostas.

Uma **`Exception`** descreve uma condição que o programa não podia controlar: um texto que não era um número, um arquivo que não estava lá, uma rede que não respondeu nada. `FormatException` é uma delas. Elas são esperadas, e capturá-las é a resposta normal.

Um **`Error`** descreve um erro no próprio código:

- `ArgumentError` — uma função foi chamada com um valor que ela documenta como inválido
- `StateError` — um objeto foi usado em um momento em que não pode fazer o que foi pedido
- `RangeError` — um índice ou um valor estava fora do intervalo permitido

Capturar um `Error` esconde o bug em vez de corrigi-lo. A resposta certa é mudar o código para que ele pare de ser lançado: verifique o argumento antes de chamar, ou use uma API que não lança. É por isso que uma cláusula `on FormatException` é uma boa prática, enquanto uma cláusula `on ArgumentError` quase nunca é.

---

Algumas bibliotecas oferecem uma versão que não lança nada. Ao lado de `int.parse`, o Dart tem **`int.tryParse`**: a mesma conversão, mas ela retorna `null` em vez de lançar quando o texto não é um número.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

O resultado é um `int?`, então o operador `??` o transforma direto em um padrão:

```dart
final port = int.tryParse(text) ?? 8080;
```

Quando a falha é comum e você só quer um fallback, isso é mais curto e mais claro do que um bloco `try`. Deixe `int.parse` para os casos em que texto ruim realmente é uma falha que alguém acima precisa saber.

---

`firstWhere` retorna o primeiro elemento que corresponde a um teste. Quando nada corresponde, não há elemento para retornar, então ele lança um `StateError`:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Como `int.tryParse`, a biblioteca oferece uma saída. O parâmetro nomeado `orElse` recebe uma função que produz o valor a usar quando nada correspondeu:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

A escolha é a mesma de antes: `orElse` quando "nada correspondeu" é um desfecho comum, a chamada simples quando significaria que os dados estão quebrados e alguém precisa saber.

---

O `throw` e o `try` não precisam viver na mesma função. Uma função que não pode fazer o trabalho dela lança, e o chamador que sabe o que fazer a respeito captura:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` não tem opinião sobre se uma idade ruim deve encerrar o programa, mostrar uma mensagem ou ser pulada — essa é a decisão do chamador, e o chamador é onde o bloco `try` pertence. Essa divisão é o motivo de lançar valer mais do que retornar `-1`: a falha chega ao único lugar que pode respondê-la.

Lembre-se de que o bloco `try` para na primeira falha, então as instruções depois da chamada que falha também são puladas.

---

Onde o bloco `try` fica decide quanto trabalho uma única falha destrói. Ao redor do laço, o primeiro elemento ruim encerra o lote inteiro; **dentro** do laço, apenas esse elemento se perde e o resto ainda é processado:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

Esta é a forma cotidiana para importar um arquivo, ler uma lista de configurações ou tratar uma fila de mensagens: uma linha danificada não deve descartar as boas. A regra continua a mesma de antes — mantenha o bloco `try` ao redor da instrução que pode falhar, e nada maior.

---

A última peça é lançar um `Error` de propósito. Uma função que documenta o que aceita deve recusar qualquer outra coisa ruidosamente, e `ArgumentError` é o objeto para isso:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

A mensagem é acessível como `e.message`, e `toString()` imprime `Invalid argument(s): ` seguido dela.

Isso não contradiz a regra de antes. Lançar um `ArgumentError` é certo, capturar um não é: ele diz ao autor do *chamador* que a chamada em si está errada, e a correção é uma verificação antes da chamada, não um tratamento ao redor dela.
