---
language: dart
exerciseType: 1
difficulty: 3
title: 闰年
---

# --description--

一个日历年恰好有 365.25 天。但是，这最终会导致混乱，因为人类通常按整数来计数，而不是用小数点。因此，为了避免这种情况，决定每四年将所有 0.25 天累加起来，使该年有 366 天（包括 2 月 29 日作为闰日），并称之为__闰年__。四年周期中的其他三年只有 365 天，__不是闰年__。

# --instructions--

在这个挑战中，我们将更进一步，要求你在不使用 `DateTime` 类、`switch` 语句、__if 代码块__、__if-else 代码块__或__三元运算符__（`x ? a : b`）以及逻辑运算符 __AND__（`&&`）和 __OR__（`||`）的情况下判断是否为闰年，但可以使用 __NOT__（`!`）运算符。

如果是闰年则返回 `true`，否则返回 `false`。

函数调用示例：
```dart
print(leapYear(2000));
// prints true
```

# --seed--

```dart
bool leapYear(int year) {
  
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

不允许使用 `DateTime`、`switch`、`if`、`else`、`&&`、`||` 或 `?`。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年份 `2016` 是闰年。

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

年份 `1996` 是闰年。

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

年份 `1600` 是闰年。

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

年份 `2020` 是闰年。

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

年份 `2000` 是闰年。

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

年份 `2008` 是闰年。

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

年份 `1521` 不是闰年。

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

年份 `1800` 不是闰年。

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

年份 `2007` 不是闰年。

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

年份 `2002` 不是闰年。

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

年份 `1979` 不是闰年。

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

年份 `2006` 不是闰年。

```dart
  test('test12', () {
    expect(leapYear(2006), false, reason: '--err-t12--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool leapYear(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```dart
bool leapYear(int year) {
  while (year % 100 == 0) {
    year = year ~/ 100;
  }
  return year % 4 == 0;
}
```
