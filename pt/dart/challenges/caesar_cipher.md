---
language: dart
exerciseType: 1
difficulty: 2
title: Cifra de César
---

# --description--

Júlio César protegia as suas cartas particulares com um dos truques mais antigos da criptografia: ele substituía cada letra de uma mensagem pela letra que está um número fixo de posições à frente no alfabeto. Com um deslocamento de 3, `a` vira `d`, `b` vira `e` e `c` vira `f`.

O alfabeto funciona como um círculo, então as letras no final voltam para o começo: com um deslocamento de 3, `x` vira `a`, `y` vira `b` e `z` vira `c`.

Qualquer coisa que não seja uma letra, como um espaço, uma vírgula, um ponto de exclamação ou um dígito, atravessa a cifra sem sofrer alterações.

# --instructions--

Escreva uma função `caesarCipher` que receba uma mensagem `text` e um número inteiro `shift`, e retorne a mensagem codificada.

Exemplos:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- A mensagem está sempre em minúsculas, então você nunca precisa lidar com letras maiúsculas.
- Os caracteres que não são letras mantêm o seu lugar e o seu valor.
- O deslocamento nunca é negativo. Um deslocamento de `0` deixa a mensagem inalterada, e o mesmo acontece com um deslocamento de `26`.

# --seed--

```dart
String caesarCipher(String text, int shift) {
  
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

Um deslocamento de 3 transforma "hello" em "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

O final do alfabeto dá a volta, então "xyz" vira "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

Um deslocamento de 0 deixa a mensagem inalterada

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

Um deslocamento de 26 é uma volta completa no alfabeto, então a mensagem fica inalterada

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

A pontuação e os espaços passam sem sofrer alterações

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

Uma mensagem vazia continua vazia

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Os espaços entre letras isoladas são preservados

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Os dígitos não são deslocados, mesmo com um deslocamento de 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

Um deslocamento de 13 codifica uma frase inteira

```dart
  test('test9', () {
    expect(caesarCipher('the quick brown fox jumps over the lazy dog', 13), 'gur dhvpx oebja sbk whzcf bire gur ynml qbt', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String caesarCipher(String text, int shift) {
  final a = 'a'.codeUnitAt(0);
  final z = 'z'.codeUnitAt(0);
  final encoded = <int>[];

  for (final code in text.codeUnits) {
    if (code >= a && code <= z) {
      encoded.add(a + (code - a + shift) % 26);
    } else {
      encoded.add(code);
    }
  }

  return String.fromCharCodes(encoded);
}
```
