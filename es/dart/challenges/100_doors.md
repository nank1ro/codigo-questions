---
language: dart
exerciseType: 1
difficulty: 1
title: 100 puertas
---

# --description--

Hay 100 puertas en una fila que todas estan inicialmente cerradas.
Haces 100 pasadas por las puertas.
La primera vez, visita cada puerta y "alternala" (si la puerta esta cerrada, abrela; si esta abierta, cierrala).
La segunda vez, solo visita cada 2a puerta (es decir, puerta #2, #4, #6, ...) y alternala.
La tercera vez, visita cada 3a puerta (es decir, puerta #3, #6, #9, ...), etc., hasta que solo visites la puerta 100.

# --instructions--

Implementa una funcion para determinar el estado de las puertas despues de la ultima pasada.
Devuelve el resultado final en un arreglo, solo con el numero de puerta incluido en el arreglo si esta abierta.
> El metodo debe ser capaz de funcionar con un numero variable de puertas.

# --seed--

```dart
import 'dart:math';

List<int> getFinalOpenedDoors(numDoors: Int) {

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

Dadas 100 puertas, devuelve la lista correcta de puertas abiertas

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Dadas 10 puertas, devuelve la lista correcta de puertas abiertas

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Dadas 950 puertas, devuelve la lista correcta de puertas abiertas

```dart
    test("test3", () {
      const solution3 = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
      expect(getFinalOpenedDoors(950), solution3, reason: "--err-t3--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
import 'dart:math';

int square(int number) => pow(number.toDouble(), 2.0).toInt();

List<int> getFinalOpenedDoors(int numDoors) {
    final openDoors = <int>[];
    var i = 1;
    while (square(i) <= numDoors) {
        openDoors.add(square(i));
        i += 1;
    }
    return openDoors;
}
```
