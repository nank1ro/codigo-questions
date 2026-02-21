---
language: dart
exerciseType: 1
difficulty: 1
title: Suma
---

# --description--

Dados dos enteros `numero1` y `numero2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números.

Ejemplo de llamada a la función:
```dart
print(suma(1, 2));
// imprime 3
```

# --seed--

```dart
int suma() {

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

La suma de 1 y 3 debe ser igual a 4

```dart
  test('test1', () {
    expect(suma(1, 3), 4, reason: '--err-t1--');
  });
```

La suma de 200 y 210 debe ser igual a 410

```dart
  test('test2', () {
    expect(suma(200, 210), 410, reason: '--err-t2--');
  });
```

La suma de 15 y 35 debe ser igual a 50

```dart
  test('test3', () {
    expect(suma(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int suma(int numero1, int numero2) {
  return numero1 + numero2;
}
```
