---
language: dart
exerciseType: 1
difficulty: 3
title: Convertidor de numeros romanos
---

# --description--

Crea una funcion que tome un entero positivo como parametro y devuelva una cadena que contenga la representacion en numeros romanos de ese entero. Los numeros romanos modernos se escriben expresando cada digito por separado, comenzando con el digito mas a la izquierda y omitiendo cualquier digito con un valor de cero.

# --instructions--

Ejemplos:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Todos los numeros romanos deben devolverse en mayusculas.
- El numero mas grande que se puede representar en esta notacion es 3,999.

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

El numero `2` debe ser igual a `II`

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

El numero `12` debe ser igual a `XII`

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

El numero `16` debe ser igual a `XVI`

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

El numero `44` debe ser igual a `XLIV`

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

El numero `68` debe ser igual a `LXVIII`

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

El numero `400` debe ser igual a `CD`

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

El numero `798` debe ser igual a `DCCXCVIII`

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

El numero `1000` debe ser igual a `M`

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

El numero `3999` debe ser igual a `MMMCMXCIX`

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

El numero `649` debe ser igual a `DCXLIX`

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

El numero `1666` debe ser igual a `MDCLXVI`

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
