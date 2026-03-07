---
language: dart
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Dana jest liczba całkowita `N`.
Napisz program, który oblicza sumę wszystkich cyfr liczby N.

# --instructions--

Zwróć sumę cyfr liczby `N`.

Przykład wywołania funkcji:
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

Suma cyfr liczby 12345 wynosi 15

```dart
  test('test1', () {
    expect(sumDigits(12345), 15, reason: '--err-t1--');
  });
```

Suma cyfr liczby 57253 wynosi 22

```dart
  test('test2', () {
    expect(sumDigits(57253), 22, reason: '--err-t2--');
  });
```

Suma cyfr liczby 122 wynosi 5

```dart
  test('test3', () {
    expect(sumDigits(122), 5, reason: '--err-t3--');
  });
```

Suma cyfr liczby 91979997 wynosi 60

```dart
  test('test4', () {
    expect(sumDigits(91979997), 60, reason: '--err-t4--');
  });
```

Suma cyfr liczby 2147483647 wynosi 46

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

