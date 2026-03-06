---
language: dart
exerciseType: 1
difficulty: 1
title: 算术平均值
---

# --description--

编写一个名为 `mean` 的函数来计算数值向量的_算术平均值_。

# --instructions--

编写一个返回数值向量平均值的函数。

函数调用示例：
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

`[1, 2, 3, 4, 5, 6, 7]` 的平均值必须等于 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

`[4, 5, 6]` 的平均值必须等于 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

`[12, 34, 56, 78]` 的平均值必须等于 45.0

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
