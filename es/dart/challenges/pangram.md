---
language: dart
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Un pangrama es una frase que usa cada letra del alfabeto inglés al menos una vez. El ejemplo más conocido es "the quick brown fox jumps over the lazy dog", que encaja las 26 letras en nueve palabras cortas.

La comprobación no distingue entre mayúsculas y minúsculas, por lo que `A` y `a` cuentan como la misma letra. Los dígitos, los signos de puntuación y los espacios se ignoran: no son letras, pero tampoco son motivo para rechazar una frase.

# --instructions--

Escribe una función `isPangram` que reciba una frase y devuelva `true` si la frase es un pangrama y `false` en caso contrario.

Ejemplos:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Una frase vacía no es un pangrama.
- Solo cuentan las 26 letras de la `a` a la `z`.

# --seed--

```dart
bool isPangram(String sentence) {
  
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

Una frase vacía no es un pangrama

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

La frase clásica "the quick brown fox jumps over the lazy dog" es un pangrama

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Una frase a la que le falta la letra `x` no es un pangrama

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

La frase "the five boxing wizards jump quickly" es un pangrama

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Los guiones bajos se ignoran, por lo que la frase sigue siendo un pangrama

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Los dígitos se ignoran, por lo que la frase sigue siendo un pangrama

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Los dígitos no reemplazan a las letras `e`, `i` y `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Una frase en mayúsculas también es un pangrama

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Mezclar mayúsculas y minúsculas de la misma mitad del alfabeto no es suficiente

```dart
  test('test9', () {
    expect(isPangram('abcdefghijklm ABCDEFGHIJKLM'), false, reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isPangram(String sentence) {
  final letters = <String>{};

  for (final char in sentence.toLowerCase().split('')) {
    if (char.compareTo('a') >= 0 && char.compareTo('z') <= 0) {
      letters.add(char);
    }
  }

  return letters.length == 26;
}
```
