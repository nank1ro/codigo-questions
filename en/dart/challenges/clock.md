---
language: dart
exerciseType: 1
difficulty: 2
title: Clock
---

# --description--

A 24-hour clock shows the time of day as `HH:MM`, starting at `00:00` just after midnight and ending at `23:59` one minute before the next midnight. Both parts are always written with two digits, so nine minutes past eleven in the morning reads `11:09`.

A whole day lasts 1440 minutes. Once the clock passes `23:59` it rolls over to `00:00` and starts the day again, and winding it backwards past `00:00` lands on `23:59`.

# --instructions--

Write a function `clockTime` that takes two whole numbers, `hours` and `minutes`, and returns the reading of a 24-hour clock as the string `"HH:MM"`, with both parts padded to two digits.

Examples:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Either number may be negative, or larger than a real clock allows.
- Work out the total number of minutes as `hours * 60 + minutes`, then wrap that total into the range `0` to `1439` so the clock rolls over in both directions.
- `clockTime(24, 0)` is exactly one day, so it reads `"00:00"`.

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

Eight in the morning reads `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Single digits are padded to two, so nine minutes past eleven reads `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Exactly one full day of hours rolls over to `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

Minutes over 60 carry into the hours

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

A negative hour winds the clock backwards past midnight

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

A negative minute count also winds the clock backwards

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

More than a whole day backwards keeps rolling over

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
  // Dart's % is the Euclidean modulo, so a negative total already wraps
  // forward into 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
