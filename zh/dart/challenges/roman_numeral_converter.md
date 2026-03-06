---
language: dart
exerciseType: 1
difficulty: 3
title: 罗马数字转换器
---

# --description--

创建一个函数，接受一个正整数作为参数，返回包含该整数的罗马数字表示的字符串。现代罗马数字的书写方式是分别表示每个数位，从最左边的数位开始，跳过值为零的数位。

# --instructions--

示例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 所有罗马数字应以大写形式返回。
- 此记数法可表示的最大数字为 3,999。

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

数字 `2` 必须等于 `II`

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

数字 `12` 必须等于 `XII`

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

数字 `16` 必须等于 `XVI`

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

数字 `44` 必须等于 `XLIV`

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

数字 `68` 必须等于 `LXVIII`

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

数字 `400` 必须等于 `CD`

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

数字 `798` 必须等于 `DCCXCVIII`

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

数字 `1000` 必须等于 `M`

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

数字 `3999` 必须等于 `MMMCMXCIX`

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

数字 `649` 必须等于 `DCXLIX`

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

数字 `1666` 必须等于 `MDCLXVI`

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
