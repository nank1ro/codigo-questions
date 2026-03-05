---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crie uma função que receba um número como argumento e retorne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Se o número for um múltiplo de `3`, a saída deve ser `"Fizz"`
- Se o número fornecido for um múltiplo de `5`, a saída deve ser `"Buzz"`.
- Se o número fornecido for um múltiplo de ambos `3` e `5`, a saída deve ser `"FizzBuzz"`.
- Se o número não for um múltiplo de `3` nem de `5`, o número deve ser exibido por si só, como mostrado nos exemplos abaixo.
- A saída deve ser sempre uma string, mesmo que não seja um múltiplo de `3` ou `5`.

Exemplos:
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

O número `3` deve ser igual a `"Fizz"`

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

O número `5` deve ser igual a `"Buzz"`

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

O número `15` deve ser igual a `"FizzBuzz"`

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

O número `10` deve ser igual a `"Buzz"`

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

O número `98` deve ser igual a `"98"`

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
