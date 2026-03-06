---
language: dart
exerciseType: 1
difficulty: 1
title: 数字之和
---

# --description--

给定一个整数 `N`。
编写一个程序来计算 N 的所有数字之和

# --instructions--

返回 `N` 的数字之和。

函数调用示例：
```dart
print(sumDigits(28))
// prints 10
```

# --seed--

```dart
int sumDigits() {

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

12345 的数字之和为 15

```dart
  test('test1', () {
    expect(sumDigits(12345), 15, reason: '--err-t1--');
  });
```

57253 的数字之和为 22

```dart
  test('test2', () {
    expect(sumDigits(57253), 22, reason: '--err-t2--');
  });
```

122 的数字之和为 5

```dart
  test('test3', () {
    expect(sumDigits(122), 5, reason: '--err-t3--');
  });
```

91979997 的数字之和为 60

```dart
  test('test4', () {
    expect(sumDigits(91979997), 60, reason: '--err-t4--');
  });
```

2147483647 的数字之和为 46

```dart
  test('test5', () {
    expect(sumDigits(2147483647), 46, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumDigits(int number) {
  var n = number;
  var result = 0;
  while (n > 0) {
    result += n % 10;
    n = n ~/ 10;
  }
  return result;
}
```

