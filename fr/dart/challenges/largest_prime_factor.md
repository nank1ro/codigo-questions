---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Les facteurs premiers de 13195 sont 5, 7, 13 et 29.

# --instructions--

Écris une fonction qui retourne le plus grand facteur premier de `number`.

Exemple d'appel de fonction :
```dart
print(largestPrimeFactor(13195));
// prints 29
```

# --seed--

```dart
int largestPrimeFactor(int number) {

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

Le plus grand facteur premier de 2 doit être égal à 2

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

Le plus grand facteur premier de 3 doit être égal à 3

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

Le plus grand facteur premier de 13195 doit être égal à 29

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

Le plus grand facteur premier de 600851475143 doit être égal à 6857

```dart
  test('test4', () {
    expect(largestPrimeFactor(600851475143), 6857, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int largestPrimeFactor(int number) {
  int largest = 1;
  int n = number;
  int factor = 2;
  while (factor * factor <= n) {
    while (n % factor == 0) {
      largest = factor;
      n ~/= factor;
    }
    factor++;
  }
  if (n > 1) {
    largest = n;
  }
  return largest;
}
```
