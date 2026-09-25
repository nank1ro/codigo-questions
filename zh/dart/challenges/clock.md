---
language: dart
exerciseType: 1
difficulty: 2
title: 时钟
---

# --description--

24 小时制时钟以 `HH:MM` 的形式显示一天中的时间，从午夜刚过的 `00:00` 开始，到下一个午夜前一分钟的 `23:59` 结束。两部分始终写成两位数字，所以上午十一点零九分显示为 `11:09`。

一整天共有 1440 分钟。时钟一旦走过 `23:59` 就会回到 `00:00` 重新开始一天，而向后拨过 `00:00` 则会落在 `23:59`。

# --instructions--

编写一个函数 `clockTime`，它接收两个整数 `hours` 和 `minutes`，并返回 24 小时制时钟的读数，即字符串 `"HH:MM"`，两部分都补足成两位数字。

示例：
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- 两个数都可能是负数，也可能大于真实时钟所允许的范围。
- 先按 `hours * 60 + minutes` 算出总分钟数，再把这个总数折回 `0` 到 `1439` 的范围内，让时钟向两个方向都能回绕。
- `clockTime(24, 0)` 正好是一天，所以读数是 `"00:00"`。

# --seed--

```dart
String clockTime(int hours, int minutes) {
  
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

早上八点显示为 `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

个位数字会补足成两位，所以十一点零九分显示为 `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

正好一整天的小时会回绕到 `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

超过 60 的分钟数会进位到小时

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

负的小时数会把时钟向后拨过午夜

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

负的分钟数同样会把时钟向后拨

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

向后超过一整天也会继续回绕

```dart
  test('test7', () {
    expect(clockTime(-25, 0), "23:00", reason: '--err-t7--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String clockTime(int hours, int minutes) {
  // Dart 的 % 是欧几里得取模，所以负的总数已经
  // 向前回绕到 0..1439。
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
