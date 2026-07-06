---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Ein pythagoreisches Tripel ist eine Menge aus drei natürlichen Zahlen a < b < c, für die a² + b² = c² gilt.

Zum Beispiel: 3² + 4² = 9 + 16 = 25 = 5². Es gibt genau ein pythagoreisches Tripel, für das a + b + c = 1000 gilt.

# --instructions--

Schreibe eine Funktion, die das pythagoreische Tripel findet, bei dem a + b + c gleich `n` ist, und das Produkt a × b × c zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Das Produkt des pythagoreischen Tripels, bei dem a+b+c=12, muss 60 ergeben

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

Das Produkt des pythagoreischen Tripels, bei dem a+b+c=1000, muss 31875000 ergeben

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
