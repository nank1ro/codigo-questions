---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La suma de los cuadrados de los primeros diez números naturales es 1² + 2² + ... + 10² = 385.

El cuadrado de la suma de los primeros diez números naturales es (1 + 2 + ... + 10)² = 55² = 3025.

La diferencia entre el cuadrado de la suma y la suma de los cuadrados para el 1 al 10 es 3025 − 385 = 2640.

# --instructions--

Escribe una función que devuelva la diferencia entre el cuadrado de la suma y la suma de los cuadrados de los primeros `n` números naturales.

Ejemplo de llamada a la función:
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

La diferencia entre el cuadrado de la suma y la suma de los cuadrados para n=10 debe ser igual a 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

La diferencia entre el cuadrado de la suma y la suma de los cuadrados para n=20 debe ser igual a 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

La diferencia entre el cuadrado de la suma y la suma de los cuadrados para n=100 debe ser igual a 25164150

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
