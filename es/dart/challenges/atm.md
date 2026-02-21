---
language: dart
exerciseType: 1
difficulty: 1
title: "Cajero automatico"
---

# --description--

A James le gustaria retirar N dolares de un cajero automatico.
El cajero solo aceptara la transaccion si N es multiplo de 5, y la cuenta de James tiene suficiente efectivo para realizar la transaccion de retiro (incluyendo los cargos bancarios).
Por cada retiro exitoso el banco cobrara `0.50$`.
Calcula el saldo de la cuenta de James despues de una transaccion intentada.
Las entradas estan en el siguiente orden:
1. el monto de efectivo que James desea retirar esta en el siguiente rango: `0 < N <= 2000`.
2. El saldo inicial de James se da con dos digitos de precision y esta en el siguiente rango: `0 < B <= 2000`.

# --instructions--

Devuelve el saldo de la cuenta despues de la transaccion intentada, dado como un numero con dos digitos de precision.
Si no hay suficiente dinero en la cuenta para completar la transaccion, devuelve el saldo bancario actual.

Ejemplo de llamada a la funcion:
```dart
print(accountBalance(10, 20.00))
// imprime 9.5
```

# --seed--

```dart
double accountBalance() {
    return
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

Realizar una transaccion exitosa

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Fondos insuficientes

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Transaccion rechazada, monto invalido

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Retirar todo el dinero exitosamente

```dart
    test('test4', () {
      expect(accountBalance(95, 95.50), 0.00, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
double accountBalance(int withdraw, double balance) {
  final isMultipleOf5 = withdraw % 5 == 0;
  final isAmountAvailable = balance >= (withdraw + 0.50);
  if (isMultipleOf5 && isAmountAvailable) {
    return balance - withdraw - 0.50;
  }
  return balance;
}
```
