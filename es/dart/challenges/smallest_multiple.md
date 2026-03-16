---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 es el número más pequeño que puede dividirse por cada uno de los números del 1 al 10 sin dejar resto.

# --instructions--

Escribe una función que devuelva el número positivo más pequeño que sea divisible de manera exacta por todos los números del 1 al `n`.

Ejemplo de llamada a la función:
```dart
print(smallestMultiple(10));
// prints 2520
```

# --seed--

```dart
int smallestMultiple(int n) {

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

El mínimo común múltiplo de 1 a 5 debe ser igual a 60

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

El mínimo común múltiplo de 1 a 10 debe ser igual a 2520

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

El mínimo común múltiplo de 1 a 20 debe ser igual a 232792560

```dart
  test('test3', () {
    expect(smallestMultiple(20), 232792560, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

int _lcm(int a, int b) => a ~/ _gcd(a, b) * b;

int smallestMultiple(int n) {
  int result = 1;
  for (int i = 2; i <= n; i++) {
    result = _lcm(result, i);
  }
  return result;
}
```
