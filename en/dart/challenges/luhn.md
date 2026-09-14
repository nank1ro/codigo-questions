---
language: dart
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

The Luhn algorithm is a simple checksum used to validate identification numbers, such as credit card numbers.

Before checking a number, strip every space from the string. The string is valid only if what remains is longer than one character and the original string contains nothing but digits and spaces.

To run the check, start from the rightmost digit and move left, doubling every second digit. When doubling produces a number greater than 9, subtract 9 from it. Then sum all the digits: the number is valid only if the sum is divisible by 10.

For example, `"059"` gives `0`, then `5` doubled is `10` which becomes `1`, then `9`. Their sum is `10`, which is divisible by 10, so the number is valid.

# --instructions--

Write a function `isValid` that takes a string and returns `true` when the number is valid, `false` otherwise.

- `"4539 3195 0343 6467"` passes the checksum, so the result is `true`.
- `"8273 1232 7352 0569"` fails the checksum, so the result is `false`.
- `"0"` is only one character long, so the result is `false`.
- `"055-444-285"` contains a character that is not a digit or a space, so the result is `false`.

Example of function call:
```dart
print(isValid("095 245 88"));
// prints true
```

# --seed--

```dart
bool isValid(String value) {
  
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

A single digit is not valid.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

A single digit with a leading space is not valid.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

The number `"059"` is valid.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

The number `"59"` is valid.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

The number `"055 444 285"` is valid.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

The number `"055 444 286"` is not valid.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

The number `"8273 1232 7352 0569"` is not valid.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

The number `"4539 3195 0343 6467"` is valid.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

The number `"1 2345 6789 1234 5678 9012"` is not valid.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

The number `"095 245 88"` is valid.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

A letter makes the number invalid.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

Dashes make the number invalid.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

A punctuation character makes the number invalid.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

Symbols make the number invalid.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

An empty string is not valid.

```dart
  test('test15', () {
    expect(isValid(""), false, reason: '--err-t15--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isValid(String value) {
  var sum = 0;
  var count = 0;
  for (var i = value.length - 1; i >= 0; i--) {
    final code = value.codeUnitAt(i);
    if (code == 32) {
      continue;
    }
    if (code < 48 || code > 57) {
      return false;
    }
    var digit = code - 48;
    if (count % 2 == 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
    count++;
  }
  return count > 1 && sum % 10 == 0;
}
```
