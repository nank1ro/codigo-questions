---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Erstellen Sie eine Funktion, die eine Zahl als Argument nimmt und `"Fizz"`, `"Buzz"` oder `"FizzBuzz"` zurückgibt.

# --instructions--

- Wenn die Zahl ein Vielfaches von `3` ist, sollte die Ausgabe `"Fizz"` sein
- Wenn die gegebene Zahl ein Vielfaches von `5` ist, sollte die Ausgabe `"Buzz"` sein.
- Wenn die gegebene Zahl ein Vielfaches von `3` und `5` ist, sollte die Ausgabe `"FizzBuzz"` sein.
- Wenn die Zahl kein Vielfaches von `3` oder `5` ist, sollte die Zahl wie in den folgenden Beispielen gezeigt selbst ausgegeben werden.
- Die Ausgabe sollte immer ein String sein, auch wenn es kein Vielfaches von `3` oder `5` ist.

Beispiele:
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

Die Zahl `3` muss gleich `"Fizz"` sein

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

Die Zahl `5` muss gleich `"Buzz"` sein

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

Die Zahl `15` muss gleich `"FizzBuzz"` sein

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

Die Zahl `10` muss gleich `"Buzz"` sein

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

Die Zahl `98` muss gleich `"98"` sein

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
