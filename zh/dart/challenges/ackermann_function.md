---
language: dart
exerciseType: 1
difficulty: 1
title: 阿克曼函数
---

# --description--

阿克曼函数是递归函数的经典示例，特别值得注意的是它不是原始递归函数。它的值增长非常快，其调用树的规模也是如此。

阿克曼函数通常定义如下：

![ackermann_function](https://bit.ly/3z9u4zh)

它的参数永远不会为负数，并且总是会终止

# --instructions--

编写一个返回阿克曼函数值的函数。

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)` 应返回 1。

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` 应返回 3。

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` 应返回 13。

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` 应返回 61。

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
