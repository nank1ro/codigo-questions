---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una funcion que tome un numero como argumento y devuelva `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Si el numero es multiplo de `3` la salida deberia ser `"Fizz"`
- Si el numero dado es multiplo de `5`, la salida deberia ser `"Buzz"`.
- Si el numero dado es multiplo de ambos `3` y `5`, la salida deberia ser `"FizzBuzz"`.
- Si el numero no es multiplo de `3` o `5`, el numero deberia salir por su cuenta como se muestra en los ejemplos a continuacion.
- La salida siempre debe ser una cadena incluso si no es multiplo de `3` o `5`.

Ejemplos:
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
```

# --seed--

```dart
String fizzBuzz() {

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

El numero `3` debe ser igual a `"Fizz"`

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

El numero `5` debe ser igual a `"Buzz"`

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

El numero `15` debe ser igual a `"FizzBuzz"`

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

El numero `10` debe ser igual a `"Buzz"`

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

El numero `98` debe ser igual a `"98"`

```dart
  test('test5', () {
    expect(fizzBuzz(98), '98', reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String fizzBuzz(int number) {
  if (number % 3 == 0 && number % 5 == 0) {
    return 'FizzBuzz';
  }
  if (number % 3 == 0) {
    return 'Fizz';
  }
  if (number % 5 == 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
