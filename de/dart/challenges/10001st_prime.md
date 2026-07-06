---
language: dart
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

Wenn wir die ersten sechs Primzahlen auflisten: 2, 3, 5, 7, 11 und 13, sehen wir, dass die 6. Primzahl 13 ist.

# --instructions--

Schreibe eine Funktion, die die `n`-te Primzahl zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Die 6. Primzahl muss 13 ergeben

```dart
  test('test1', () {
    expect(nthPrime(6), 13, reason: '--err-t1--');
  });
```

Die 10. Primzahl muss 29 ergeben

```dart
  test('test2', () {
    expect(nthPrime(10), 29, reason: '--err-t2--');
  });
```

Die 1000. Primzahl muss 7919 ergeben

```dart
  test('test3', () {
    expect(nthPrime(1000), 7919, reason: '--err-t3--');
  });
```

Die 10001. Primzahl muss 104743 ergeben

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
