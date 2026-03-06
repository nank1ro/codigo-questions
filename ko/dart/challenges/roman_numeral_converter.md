---
language: dart
exerciseType: 1
difficulty: 3
title: 로마 숫자 변환기
---

# --description--

양의 정수를 매개변수로 받아 해당 정수의 로마 숫자 표현을 포함하는 문자열을 반환하는 함수를 만드십시오. 현대 로마 숫자는 가장 왼쪽 자릿수부터 시작하여 각 자릿수를 별도로 표현하며, 값이 0인 자릿수는 건너뜁니다.

# --instructions--

예시:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 모든 로마 숫자는 대문자로 반환되어야 합니다.
- 이 표기법으로 표현할 수 있는 가장 큰 숫자는 3,999입니다.

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

숫자 `2`는 `II`와 같아야 합니다

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

숫자 `12`는 `XII`와 같아야 합니다

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

숫자 `16`은 `XVI`와 같아야 합니다

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

숫자 `44`는 `XLIV`와 같아야 합니다

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

숫자 `68`은 `LXVIII`와 같아야 합니다

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

숫자 `400`은 `CD`와 같아야 합니다

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

숫자 `798`은 `DCCXCVIII`와 같아야 합니다

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

숫자 `1000`은 `M`과 같아야 합니다

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

숫자 `3999`는 `MMMCMXCIX`와 같아야 합니다

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

숫자 `649`는 `DCXLIX`와 같아야 합니다

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

숫자 `1666`은 `MDCLXVI`와 같아야 합니다

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
