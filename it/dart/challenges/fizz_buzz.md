---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una funzione che prenda un numero come argomento e restituisca `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Se il numero è un multiplo di `3`, l'output deve essere `"Fizz"`.
- Se il numero è un multiplo di `5`, l'output deve essere `"Buzz"`.
- Se il numero è un multiplo sia di `3` che di `5`, l'output deve essere `"FizzBuzz"`.
- Se il numero non è un multiplo né di `3` né di `5`, il numero deve essere stampato come stringa, come mostrato negli esempi seguenti.
- L'output deve sempre essere una stringa, anche se non è un multiplo di `3` o `5`.

Esempi:
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

Il numero `3` deve essere uguale a `"Fizz"`

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

Il numero `5` deve essere uguale a `"Buzz"`

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

Il numero `15` deve essere uguale a `"FizzBuzz"`

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

Il numero `10` deve essere uguale a `"Buzz"`

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

Il numero `98` deve essere uguale a `"98"`

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
