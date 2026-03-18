---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Пифагорова тройка — это набор трёх натуральных чисел a < b < c, для которых a² + b² = c².

Например, 3² + 4² = 9 + 16 = 25 = 5². Существует ровно одна пифагорова тройка, для которой a + b + c = 1000.

# --instructions--

Напишите функцию, которая находит пифагорову тройку, где a + b + c равно `n`, и возвращает произведение a × b × c.

Пример вызова функции:
```dart
print(specialPythagoreanTriplet(12));
// prints 60
```

# --seed--

```dart
int specialPythagoreanTriplet(int n) {

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

Произведение пифагоровой тройки, где a+b+c=12, должно быть равно 60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

Произведение пифагоровой тройки, где a+b+c=1000, должно быть равно 31875000

```dart
  test('test2', () {
    expect(specialPythagoreanTriplet(1000), 31875000, reason: '--err-t2--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int specialPythagoreanTriplet(int n) {
  for (int a = 1; a < n; a++) {
    for (int b = a + 1; b < n - a; b++) {
      int c = n - a - b;
      if (c > b && a * a + b * b == c * c) {
        return a * b * c;
      }
    }
  }
  return -1;
}
```
