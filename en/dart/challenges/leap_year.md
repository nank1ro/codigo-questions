---
language: dart
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In a calendar year there are exactly 365.25 days. But, eventually, this will lead to confusion because humans normally count by exact divisibility of 1 and not with decimal points. So, to avoid the latter, it was decided to add up all 0.25 days every four-year cycle and give that year 366 days (including February 29 as an intercalary day) and call it a __leap year__. The other three years in the four-year cycle would only contain 365 days and __wouldn't be leap years__.

# --instructions--

In this challenge we'll take it to a new level, where you are to determine if it's a leap year or not without the use of the `DateTime` class, `switch` statements, __if blocks__, __if-else blocks__ or __ternary operation__ (`x ? a : b`) nor the logical operators __AND__ (`&&`) and __OR__ (`||`) with the exemption of the __NOT__ (`!`) operator.

Return `true` if it's a leap year, `false` otherwise.

Example of function call:
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

The use of `DateTime`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

The year `1996` is a leap year.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

The year `1600` is a leap year.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

The year `2020` is a leap year.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

The year `2000` is a leap year.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

The year `2008` is a leap year.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

The year `1521` is not a leap year.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

The year `1800` is not a leap year.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

The year `2007` is not a leap year.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

The year `2002` is not a leap year.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

The year `1979` is not a leap year.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

The year `2006` is not a leap year.

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
