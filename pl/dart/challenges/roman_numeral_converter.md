---
language: dart
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Utwórz funkcję przyjmującą dodatnią liczbę całkowitą jako parametr i zwracającą ciąg znaków zawierający reprezentację tej liczby w zapisie rzymskim. Współczesne cyfry rzymskie zapisuje się, wyrażając każdą cyfrę osobno, zaczynając od cyfry najbardziej na lewo i pomijając cyfry o wartości zero.

# --instructions--

Przykłady:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Wszystkie cyfry rzymskie powinny być zwracane jako wielkie litery.
- Największa liczba, którą można przedstawić w tym zapisie, to 3 999.

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

Liczba `2` musi być równa `II`

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

Liczba `12` musi być równa `XII`

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

Liczba `16` musi być równa `XVI`

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

Liczba `44` musi być równa `XLIV`

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

Liczba `68` musi być równa `LXVIII`

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

Liczba `400` musi być równa `CD`

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

Liczba `798` musi być równa `DCCXCVIII`

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

Liczba `1000` musi być równa `M`

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

Liczba `3999` musi być równa `MMMCMXCIX`

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

Liczba `649` musi być równa `DCXLIX`

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

Liczba `1666` musi być równa `MDCLXVI`

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
