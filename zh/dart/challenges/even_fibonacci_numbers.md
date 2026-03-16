---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

斐波那契数列中的每个新项都是由前两项相加得到的。从1和2开始，前10项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

编写一个函数，返回所有不超过 `n` 的偶数斐波那契项之和。

函数调用示例：
```dart
print(fibonacciEvenSum(8));
// prints 10
```

# --seed--

```dart
int fibonacciEvenSum(int n) {

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

不超过8的偶数斐波那契项之和必须等于10

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

不超过10的偶数斐波那契项之和必须等于10

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

不超过34的偶数斐波那契项之和必须等于44

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

不超过1000的偶数斐波那契项之和必须等于798

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

不超过4000000的偶数斐波那契项之和必须等于4613732

```dart
  test('test5', () {
    expect(fibonacciEvenSum(4000000), 4613732, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int fibonacciEvenSum(int n) {
  int sum = 0;
  int a = 1, b = 2;
  while (a <= n) {
    if (a % 2 == 0) {
      sum += a;
    }
    int temp = a + b;
    a = b;
    b = temp;
  }
  return sum;
}
```
