---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Trójka pitagorejska to zbiór trzech liczb naturalnych a < b < c, dla których a² + b² = c².

Na przykład 3² + 4² = 9 + 16 = 25 = 5². Istnieje dokładnie jedna trójka pitagorejska, dla której a + b + c = 1000.

# --instructions--

Napisz funkcję, która znajduje trójkę pitagorejską, gdzie a + b + c wynosi `n`, i zwraca iloczyn a × b × c.

Przykład wywołania funkcji:
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

Iloczyn trójki pitagorejskiej, gdzie a+b+c=12, musi być równy 60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

Iloczyn trójki pitagorejskiej, gdzie a+b+c=1000, musi być równy 31875000

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
