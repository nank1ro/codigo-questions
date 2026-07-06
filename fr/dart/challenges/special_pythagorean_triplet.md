---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Un triplet pythagoricien est un ensemble de trois nombres naturels a < b < c pour lesquels a² + b² = c².

Par exemple, 3² + 4² = 9 + 16 = 25 = 5². Il existe exactement un triplet pythagoricien pour lequel a + b + c = 1000.

# --instructions--

Écris une fonction qui trouve le triplet pythagoricien où a + b + c est égal à `n`, et retourne le produit a × b × c.

Exemple d'appel de fonction :
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

Le produit du triplet pythagoricien où a+b+c=12 doit être égal à 60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

Le produit du triplet pythagoricien où a+b+c=1000 doit être égal à 31875000

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
