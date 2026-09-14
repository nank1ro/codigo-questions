---
language: dart
exerciseType: 1
difficulty: 1
title: Conjetura de Collatz
---

# --description--

La conjetura de Collatz parte de cualquier entero positivo `n` y repite una única regla sencilla: si `n` es par, se reduce a la mitad; si `n` es impar, se sustituye por `3n + 1`. Tarde o temprano la sucesión llega a 1.

Por ejemplo, empezando en 16 la sucesión es `16 -> 8 -> 4 -> 2 -> 1`, así que se necesitan 4 pasos.

Nadie ha demostrado jamás que esto ocurra siempre, pero se cumple para todos los números probados hasta ahora.

# --instructions--

Escribe una función `collatzSteps` que reciba un entero positivo `n` y devuelva el número de pasos necesarios para llegar a 1.

`collatzSteps(1)` es 0, porque 1 ya es el final de la sucesión. `collatzSteps(12)` es 9, y `collatzSteps(27)` es 111.

Ejemplo de llamada a la función:
```dart
print(collatzSteps(16));
// prints 4
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` debe devolver 0, porque 1 ya es el final de la sucesión.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` debe devolver 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` debe devolver 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` debe devolver 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` debe devolver 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` debe devolver 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` debe devolver 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` debe devolver 118.

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
