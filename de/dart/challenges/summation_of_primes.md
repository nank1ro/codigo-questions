---
language: dart
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

Die Summe der Primzahlen unter 10 beträgt 2 + 3 + 5 + 7 = 17.

# --instructions--

Schreibe eine Funktion, die die Summe aller Primzahlen unterhalb von `n` zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Die Summe aller Primzahlen unterhalb von 10 muss 17 ergeben

```dart
  test('test1', () {
    expect(primeSummation(10), 17, reason: '--err-t1--');
  });
```

Die Summe aller Primzahlen unterhalb von 1000 muss 76127 ergeben

```dart
  test('test2', () {
    expect(primeSummation(1000), 76127, reason: '--err-t2--');
  });
```

Die Summe aller Primzahlen unterhalb von 100000 muss 454396537 ergeben

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
