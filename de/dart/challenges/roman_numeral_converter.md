---
language: dart
exerciseType: 1
difficulty: 3
title: Römischer Zahlenkonverter
---

# --description--

Erstellen Sie eine Funktion, die eine positive ganze Zahl als Parameter nimmt und einen String zurückgibt, der die römische Zahlendarstellung dieser Ganzzahl enthält. Moderne römische Zahlen werden geschrieben, indem jede Ziffer separat ausgedrückt wird, beginnend mit der linken Ziffer und überspring jede Ziffer mit einem Wert von Null.

# --instructions--

Beispiele:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Alle römischen Zahlen sollten in Großbuchstaben zurückgegeben werden.
- Die größte Zahl, die mit dieser Notation dargestellt werden kann, ist 3.999.

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

Die Nummer `2` muss gleich `II` sein

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

Die Nummer `12` muss gleich `XII` sein

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

Die Nummer `16` muss gleich `XVI` sein

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

Die Nummer `44` muss gleich `XLIV` sein

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

Die Nummer `68` muss gleich `LXVIII` sein

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

Die Nummer `400` muss gleich `CD` sein

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

Die Nummer `798` muss gleich `DCCXCVIII` sein

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

Die Nummer `1000` muss gleich `M` sein

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

Die Nummer `3999` muss gleich `MMMCMXCIX` sein

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

Die Nummer `649` muss gleich `DCXLIX` sein

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

Die Nummer `1666` muss gleich `MDCLXVI` sein

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
