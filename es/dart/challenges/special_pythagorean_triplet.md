---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Una terna pitagórica es un conjunto de tres números naturales a < b < c, para los cuales se cumple a² + b² = c².

Por ejemplo, 3² + 4² = 9 + 16 = 25 = 5². Existe exactamente una terna pitagórica para la cual a + b + c = 1000.

# --instructions--

Escribe una función que encuentre la terna pitagórica donde a + b + c es igual a `n`, y devuelva el producto a × b × c.

Ejemplo de llamada a la función:
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

El producto de la terna pitagórica donde a+b+c=12 debe ser igual a 60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

El producto de la terna pitagórica donde a+b+c=1000 debe ser igual a 31875000

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
