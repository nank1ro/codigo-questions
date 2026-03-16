---
language: dart
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

Elencando i primi sei numeri primi: 2, 3, 5, 7, 11 e 13, possiamo vedere che il 6° primo è 13.

# --instructions--

Scrivi una funzione che restituisca l'`n`-esimo numero primo.

Esempio di chiamata alla funzione:
```dart
print(nthPrime(6));
// prints 13
```

# --seed--

```dart
int nthPrime(int n) {

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

Il 6° numero primo deve essere uguale a 13

```dart
  test('test1', () {
    expect(nthPrime(6), 13, reason: '--err-t1--');
  });
```

Il 10° numero primo deve essere uguale a 29

```dart
  test('test2', () {
    expect(nthPrime(10), 29, reason: '--err-t2--');
  });
```

Il 1000° numero primo deve essere uguale a 7919

```dart
  test('test3', () {
    expect(nthPrime(1000), 7919, reason: '--err-t3--');
  });
```

Il 10001° numero primo deve essere uguale a 104743

```dart
  test('test4', () {
    expect(nthPrime(10001), 104743, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 5)));
}
```

# --solutions--

```dart
bool _isPrime(int n) {
  if (n < 2) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;
  for (int i = 3; i * i <= n; i += 2) {
    if (n % i == 0) return false;
  }
  return true;
}

int nthPrime(int n) {
  int count = 0;
  int candidate = 1;
  while (count < n) {
    candidate++;
    if (_isPrime(candidate)) {
      count++;
    }
  }
  return candidate;
}
```
