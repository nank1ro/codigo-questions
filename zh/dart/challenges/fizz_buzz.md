---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

创建一个以数字作为参数的函数，返回 `"Fizz"`、`"Buzz"` 或 `"FizzBuzz"`。

# --instructions--

- 如果数字是 `3` 的倍数，输出应为 `"Fizz"`
- 如果给定的数字是 `5` 的倍数，输出应为 `"Buzz"`。
- 如果给定的数字同时是 `3` 和 `5` 的倍数，输出应为 `"FizzBuzz"`。
- 如果数字既不是 `3` 也不是 `5` 的倍数，则应按如下示例输出数字本身。
- 输出应始终为字符串，即使它不是 `3` 或 `5` 的倍数。

示例：
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
```

# --seed--

```dart
String fizzBuzz() {
  
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

数字 `3` 必须等于 `"Fizz"`

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

数字 `5` 必须等于 `"Buzz"`

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

数字 `15` 必须等于 `"FizzBuzz"`

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

数字 `10` 必须等于 `"Buzz"`

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

数字 `98` 必须等于 `"98"`

```dart
  test('test5', () {
    expect(fizzBuzz(98), '98', reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String fizzBuzz(int number) {
  if (number % 3 == 0 && number % 5 == 0) {
    return 'FizzBuzz';
  }
  if (number % 3 == 0) {
    return 'Fizz';
  }
  if (number % 5 == 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
