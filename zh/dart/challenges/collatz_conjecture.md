---
language: dart
exerciseType: 1
difficulty: 1
title: 考拉兹猜想
---

# --description--

考拉兹猜想从任意正整数 `n` 出发，重复一条简单的规则：如果 `n` 是偶数，就把它减半；如果 `n` 是奇数，就把它替换为 `3n + 1`。这个序列迟早会到达 1。

例如，从 16 开始，序列是 `16 -> 8 -> 4 -> 2 -> 1`，因此需要 4 步。

从来没有人证明过这一规律总是成立，但对于每一个被测试过的数它都成立。

# --instructions--

编写一个函数 `collatzSteps`，它接收一个正整数 `n`，并返回到达 1 所需的步数。

`collatzSteps(1)` 为 0，因为 1 已经是序列的终点。`collatzSteps(12)` 为 9，而 `collatzSteps(27)` 为 111。

函数调用示例：
```dart
print(collatzSteps(16));
// 打印 4
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` 应返回 0，因为 1 已经是序列的终点。

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` 应返回 1。

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` 应返回 8。

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` 应返回 16。

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` 应返回 4。

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` 应返回 9。

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` 应返回 111。

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` 应返回 118。

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
