---
language: dart
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

10 未満の素数の和は 2 + 3 + 5 + 7 = 17 です。

# --instructions--

`n` 未満のすべての素数の和を返す関数を書いてください。

関数呼び出しの例:
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

10 未満のすべての素数の和は 17 と等しくなければならない

```dart
  test('test1', () {
    expect(primeSummation(10), 17, reason: '--err-t1--');
  });
```

1000 未満のすべての素数の和は 76127 と等しくなければならない

```dart
  test('test2', () {
    expect(primeSummation(1000), 76127, reason: '--err-t2--');
  });
```

100000 未満のすべての素数の和は 454396537 と等しくなければならない

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
