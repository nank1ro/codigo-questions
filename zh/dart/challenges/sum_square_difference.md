---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

前十个自然数的平方和为1² + 2² + ... + 10² = 385。

前十个自然数之和的平方为(1 + 2 + ... + 10)² = 55² = 3025。

1到10的和的平方与平方和之差为3025 − 385 = 2640。

# --instructions--

编写一个函数，返回前 `n` 个自然数的和的平方与平方和之差。

函数调用示例：
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

n=10时的平方差必须等于2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

n=20时的平方差必须等于41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

n=100时的平方差必须等于25164150

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
