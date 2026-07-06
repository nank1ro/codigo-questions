---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La somme des carrés des dix premiers nombres naturels est 1² + 2² + ... + 10² = 385.

Le carré de la somme des dix premiers nombres naturels est (1 + 2 + ... + 10)² = 55² = 3025.

La différence entre le carré de la somme et la somme des carrés pour 1 à 10 est 3025 − 385 = 2640.

# --instructions--

Écris une fonction qui retourne la différence entre le carré de la somme et la somme des carrés des `n` premiers nombres naturels.

Exemple d'appel de fonction :
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

La différence entre le carré de la somme et la somme des carrés pour n=10 doit être égale à 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

La différence entre le carré de la somme et la somme des carrés pour n=20 doit être égale à 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

La différence entre le carré de la somme et la somme des carrés pour n=100 doit être égale à 25164150

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
