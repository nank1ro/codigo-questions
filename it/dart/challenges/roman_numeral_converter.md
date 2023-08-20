---
language: dart
exerciseType: 1
difficulty: 3
title: Convertitore numerico romano
---

# --description--

Crea una funzione che prenda come parametro un numero intero positivo e restituisca una stringa contenente la rappresentazione in numeri romani di quel numero intero. I numeri romani moderni sono scritti esprimendo ogni cifra separatamente, partendo dalla cifra più a sinistra e saltando qualsiasi cifra con valore zero.

# --instructions--

Esempi:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Tutti i numeri romani devono essere riportati in maiuscolo.
- Il numero più grande che può essere rappresentato con questa notazione è 3.999.

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

Il numero `2` deve essere uguale a `II` 

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

Il numero `12` deve essere uguale a `XII` 

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

Il numero `16` deve essere uguale a `XVI` 

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

Il numero `44` deve essere uguale a `XLIV` 

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

Il numero `68` deve essere uguale a `LXVIII` 

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

Il numero `400` deve essere uguale a `CD` 

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

Il numero `798` deve essere uguale a `DCCXCVIII` 

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

Il numero `1000` deve essere uguale a `M` 

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

Il numero `3999` deve essere uguale a `MMMCMXCIX` 

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

Il numero `649` deve essere uguale a `DCXLIX` 

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

Il numero `1666` deve essere uguale a `MDCLXVI` 

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
