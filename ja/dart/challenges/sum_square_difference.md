---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

最初の 10 個の自然数の二乗の和は 1² + 2² + ... + 10² = 385 です。

最初の 10 個の自然数の和の二乗は (1 + 2 + ... + 10)² = 55² = 3025 です。

1 から 10 における和の二乗と二乗の和の差は 3025 − 385 = 2640 です。

# --instructions--

最初の `n` 個の自然数の和の二乗と二乗の和の差を返す関数を書いてください。

関数呼び出しの例:
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

n=10 の場合の和の二乗と二乗の和の差は 2640 と等しくなければならない

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

n=20 の場合の和の二乗と二乗の和の差は 41230 と等しくなければならない

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

n=100 の場合の和の二乗と二乗の和の差は 25164150 と等しくなければならない

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
