---
language: dart
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Create a function taking a positive integer as its parameter and returning a string containing the Roman numeral representation of that integer. Modern Roman numerals are written by expressing each digit separately, starting with the left most digit and skipping any digit with a value of zero.

# --instructions--

Examples:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- All roman numerals should be returned as uppercase.
- The largest number that can be represented in this notation is 3,999.

# --seed--

```dart
String convertToRoman(int n) {
  
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

The number `2` must equal `II` 

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

The number `12` must equal `XII` 

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

The number `16` must equal `XVI` 

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

The number `44` must equal `XLIV` 

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

The number `68` must equal `LXVIII` 

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

The number `400` must equal `CD` 

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

The number `798` must equal `DCCXCVIII` 

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

The number `1000` must equal `M` 

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

The number `3999` must equal `MMMCMXCIX` 

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

The number `649` must equal `DCXLIX` 

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

The number `1666` must equal `MDCLXVI` 

```dart
  test('test11', () {
    expect(convertToRoman(1666), 'MDCLXVI', reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String convertToRoman(int n) {
  var result = "";

  final values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
  ];

  for (var i = 0; i < values.length; i++) {
    final value = values[i].$1;
    final letter = values[i].$2;

    while (n >= value) {
      result += letter;
      n -= value;
    }
  }
}
```
