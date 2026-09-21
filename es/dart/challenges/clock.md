---
language: dart
exerciseType: 1
difficulty: 2
title: Reloj
---

# --description--

Un reloj de 24 horas muestra la hora del día como `HH:MM`, empezando en `00:00` justo después de la medianoche y terminando en `23:59`, un minuto antes de la siguiente medianoche. Ambas partes se escriben siempre con dos dígitos, así que nueve minutos después de las once de la mañana se lee `11:09`.

Un día completo dura 1440 minutos. Cuando el reloj pasa de `23:59`, vuelve a `00:00` y empieza el día de nuevo, y girarlo hacia atrás más allá de `00:00` cae en `23:59`.

# --instructions--

Escribe una función `clockTime` que reciba dos números enteros, `hours` y `minutes`, y devuelva la lectura de un reloj de 24 horas como la cadena `"HH:MM"`, con ambas partes rellenas con dos dígitos.

Ejemplos:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Cualquiera de los dos números puede ser negativo, o mayor de lo que permite un reloj real.
- Calcula el número total de minutos como `hours * 60 + minutes` y después encaja ese total en el rango de `0` a `1439` para que el reloj dé la vuelta en ambas direcciones.
- `clockTime(24, 0)` es exactamente un día, así que se lee `"00:00"`.

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

A las ocho de la mañana se lee `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Los números de un solo dígito se rellenan con dos, así que nueve minutos después de las once se lee `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Exactamente un día completo de horas da la vuelta a `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

Los minutos por encima de 60 se trasladan a las horas

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

Una hora negativa gira el reloj hacia atrás más allá de la medianoche

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

Una cantidad negativa de minutos también gira el reloj hacia atrás

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

Más de un día completo hacia atrás sigue dando la vuelta

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
  // El % de Dart es el módulo euclidiano, así que un total negativo ya
  // vuelve hacia adelante al rango 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
