---
language: dart
exerciseType: 1
difficulty: 1
title: 加法
---

# --description--

给定两个整数 `num1` 和 `num2`，编写一个程序将这两个数相加

# --instructions--

编写一个返回两个数之和的函数。

函数调用示例：
```dart
print(addition(1, 2));
// prints 3
```

# --seed--

```dart
int addition() {
  
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

1 和 3 的和必须等于 4

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

200 和 210 的和必须等于 410

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

15 和 35 的和必须等于 50

```dart
  test('test3', () {
    expect(addition(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int addition(int num1, int num2) {
  return num1 + num2;
}
```
