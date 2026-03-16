---
language: dart
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

La somme des nombres premiers inférieurs à 10 est 2 + 3 + 5 + 7 = 17.

# --instructions--

Écris une fonction qui retourne la somme de tous les nombres premiers inférieurs à `n`.

Exemple d'appel de fonction :
```dart
print(primeSummation(10));
// prints 17
```

# --seed--

```dart
int primeSummation(int n) {

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

La somme de tous les nombres premiers inférieurs à 10 doit être égale à 17

```dart
  test('test1', () {
    expect(primeSummation(10), 17, reason: '--err-t1--');
  });
```

La somme de tous les nombres premiers inférieurs à 1000 doit être égale à 76127

```dart
  test('test2', () {
    expect(primeSummation(1000), 76127, reason: '--err-t2--');
  });
```

La somme de tous les nombres premiers inférieurs à 100000 doit être égale à 454396537

```dart
  test('test3', () {
    expect(primeSummation(100000), 454396537, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 2)));
}
```

# --solutions--

```dart
int primeSummation(int n) {
  if (n < 2) return 0;
  // Sieve of Eratosthenes
  final List<bool> sieve = List.filled(n, true);
  sieve[0] = false;
  sieve[1] = false;
  for (int i = 2; i * i < n; i++) {
    if (sieve[i]) {
      for (int j = i * i; j < n; j += i) {
        sieve[j] = false;
      }
    }
  }
  int sum = 0;
  for (int i = 2; i < n; i++) {
    if (sieve[i]) sum += i;
  }
  return sum;
}
```
