---
language: dart
exerciseType: 1
difficulty: 1
title: Gotas de lluvia
---

# --description--

Tu tarea es convertir un numero en una cadena que contiene sonidos de gotas de lluvia correspondientes a ciertos factores potenciales.
Un factor es un numero que divide uniformemente en otro numero, sin dejar residuo.
La forma mas simple de probar si un numero es factor de otro es usar la operacion modulo.
Las reglas de las gotas de lluvia son que si un numero dado:

- tiene 3 como factor, añade 'Pling' al resultado.
- tiene 5 como factor, añade 'Plang' al resultado.
- tiene 7 como factor, añade 'Plong' al resultado.
- no tiene ninguno de 3, 5 o 7 como factor, el resultado deberian ser los digitos del numero.

# --instructions--

Escribe una funcion que devuelva la cadena correcta, ejemplos:

- 28 tiene 7 como factor, pero no 3 o 5, entonces el resultado seria `"Plong"`.
- 30 tiene tanto 3 como 5 como factores, pero no 7, entonces el resultado seria `"PlingPlang"`.
- 34 no es factorizable por 3, 5 o 7, entonces el resultado seria `"34"`.

Ejemplo de llamada a la funcion:
```dart
print(raindrops(28))
// imprime "Plong"
```

# --seed--

```dart
String raindrops() {

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

El sonido para 1 es "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

El sonido para 3 es "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

El sonido para 5 es "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

El sonido para 7 es "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

El sonido para 6 es "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

El sonido para 8 es "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

El sonido para 9 es "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

El sonido para 10 es "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

El sonido para 14 es "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

El sonido para 15 es "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

El sonido para 21 es "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

El sonido para 25 es "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

El sonido para 27 es "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

El sonido para 35 es "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

El sonido para 49 es "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

El sonido para 52 es "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

El sonido para 105 es "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

El sonido para 3125 es "Plang"

```dart
  test('test18', () {
    expect(raindrops(3125), "Plang", reason: '--err-t18--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String raindrops(int number) {
  var result = "";
  if (number % 3 == 0) {
    result += "Pling";
  }
  if (number % 5 == 0) {
    result += "Plang";
  }
  if (number % 7 == 0) {
    result += "Plong";
  }
  if (result.isEmpty) {
    result = number.toString();
  }
  return result;
}
```
