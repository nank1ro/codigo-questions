---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 to najmniejsza liczba, którą można podzielić przez każdą z liczb od 1 do 10 bez reszty.

# --instructions--

Napisz funkcję, która zwraca najmniejszą dodatnią liczbę podzielną przez wszystkie liczby od 1 do `n`.

Przykład wywołania funkcji:
```dart
print(smallestMultiple(10));
// prints 2520
```

# --seed--

```dart
int smallestMultiple(int n) {

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

Najmniejsza wspólna wielokrotność dla liczb od 1 do 5 musi być równa 60

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

Najmniejsza wspólna wielokrotność dla liczb od 1 do 10 musi być równa 2520

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

Najmniejsza wspólna wielokrotność dla liczb od 1 do 20 musi być równa 232792560

```dart
  test('test3', () {
    expect(smallestMultiple(20), 232792560, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

int _lcm(int a, int b) => a ~/ _gcd(a, b) * b;

int smallestMultiple(int n) {
  int result = 1;
  for (int i = 2; i <= n; i++) {
    result = _lcm(result, i);
  }
  return result;
}
```
