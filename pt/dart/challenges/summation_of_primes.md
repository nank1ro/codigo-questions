---
language: dart
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

A soma dos números primos abaixo de 10 é 2 + 3 + 5 + 7 = 17.

# --instructions--

Escreva uma função que retorna a soma de todos os números primos abaixo de `n`.

Exemplo de chamada de função:
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

A soma de todos os números primos abaixo de 10 deve ser igual a 17

```dart
  test('test1', () {
    expect(primeSummation(10), 17, reason: '--err-t1--');
  });
```

A soma de todos os números primos abaixo de 1000 deve ser igual a 76127

```dart
  test('test2', () {
    expect(primeSummation(1000), 76127, reason: '--err-t2--');
  });
```

A soma de todos os números primos abaixo de 100000 deve ser igual a 454396537

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
