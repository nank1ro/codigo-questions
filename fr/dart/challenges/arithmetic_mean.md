---
language: dart
exerciseType: 1
difficulty: 1
title: Moyenne arithmétique
---

# --description--

Écrivez une fonction appelée `mean` pour trouver la _moyenne arithmétique_ d'un vecteur numérique.

# --instructions--

Write a function that returns the mean of a numeric vector.

Exemple d'appel de fonction :
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

La moyenne de `[1, 2, 3, 4, 5, 6, 7]` doit être égale à 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

La moyenne de `[4, 5, 6]` doit être égale à 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

La moyenne de `[12, 34, 56, 78]` doit être égale à 45.0

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
