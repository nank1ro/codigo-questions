---
language: dart
exerciseType: 1
difficulty: 1
title: Funcion de Ackermann
---

# --description--

La funcion de Ackermann es un ejemplo clasico de una funcion recursiva, notable especialmente porque no es una funcion primitiva recursiva. Creci muy rapidamente en valor, al igual que el tamaño de su arbol de llamadas.

La funcion de Ackermann generalmente se define de la siguiente manera:

![ackermann_function](https://bit.ly/3z9u4zh)

Sus argumentos nunca son negativos y siempre termina

# --instructions--

Escribe una funcion que devuelva el valor de la funcion de Ackermann.

# --seed--

```dart
int ack(int m, int n) {

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

`ack(0, 0)` deberia devolver 1.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` deberia devolver 3.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` deberia devolver 13.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` deberia devolver 61.

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
