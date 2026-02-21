---
language: dart
exerciseType: 1
difficulty: 3
title: Año bisiesto
---

# --description--

En un año calendario hay exactamente 365.25 dias. Pero, eventualmente, esto llevara a confusion porque los humanos normalmente cuentan por divisibilidad exacta de 1 y no con puntos decimales. Entonces, para evitar esto ultimo, se decidio sumar todos los 0.25 dias cada ciclo de cuatro años y darle a ese año 366 dias (incluyendo el 29 de febrero como dia intercalar) y llamarlo __año bisiesto__. Los otros tres años en el ciclo de cuatro años solo contendrian 365 dias y __no serian años bisiestos__.

# --instructions--

En este desafio lo llevaremos a un nuevo nivel, donde debes determinar si es un año bisiesto o no sin el uso de la clase `DateTime`, declaraciones `switch`, __bloques if__, __bloques if-else__ u __operacion ternaria__ (`x ? a : b`) ni los operadores logicos __AND__ (`&&`) y __OR__ (`||`) con la excepcion del operador __NOT__ (`!`).

Devuelve `true` si es un año bisiesto, `false` en caso contrario.

Ejemplo de llamada a la funcion:
```dart
print(leapYear(2000));
// imprime true
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

El uso de `DateTime`, `switch`, `if`, `else`, `&&`, `||` o `?` no esta permitido.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

El año `2016` es un año bisiesto.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

El año `1996` es un año bisiesto.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

El año `1600` es un año bisiesto.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

El año `2020` es un año bisiesto.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

El año `2000` es un año bisiesto.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

El año `2008` es un año bisiesto.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

El año `1521` no es un año bisiesto.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

El año `1800` no es un año bisiesto.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

El año `2007` no es un año bisiesto.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

El año `2002` no es un año bisiesto.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

El año `1979` no es un año bisiesto.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

El año `2006` no es un año bisiesto.

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

```dart
bool leapYear(int year) {
  while (year % 100 == 0) {
    year = year ~/ 100;
  }
  return year % 4 == 0;
}
```
