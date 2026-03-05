---
language: dart
exerciseType: 1
difficulty: 1
title: Summe der Ziffern
---

# --description--

Ihnen wird eine ganze Zahl `N` gegeben.
Schreiben Sie ein Programm, um die Summe aller Ziffern von N zu berechnen

# --instructions--

Geben Sie die Summe der Ziffern von `N` zurück.

Example of function call:
```dart
print(sumDigits(28))
// prints 10
```

# --seed--

```dart
int sumDigits() {

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

Die Summe der Ziffern von 12345 ist 15

```dart
  test('test1', () {
    expect(sumDigits(12345), 15, reason: '--err-t1--');
  });
```

Die Summe der Ziffern von 57253 ist 22

```dart
  test('test2', () {
    expect(sumDigits(57253), 22, reason: '--err-t2--');
  });
```

Die Summe der Ziffern von 122 ist 5

```dart
  test('test3', () {
    expect(sumDigits(122), 5, reason: '--err-t3--');
  });
```

Die Summe der Ziffern von 91979997 ist 60

```dart
  test('test4', () {
    expect(sumDigits(91979997), 60, reason: '--err-t4--');
  });
```

Die Summe der Ziffern von 2147483647 ist 46

```dart
  test('test5', () {
    expect(sumDigits(2147483647), 46, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumDigits(int number) {
  var n = number;
  var result = 0;
  while (n > 0) {
    result += n % 10;
    n = n ~/ 10;
  }
  return result;
}
```

