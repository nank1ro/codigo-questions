---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James desea retirar N dólares de un cajero automático.
La máquina expendedora solo aceptará la transacción si N es un múltiplo de 5, y la cuenta de James tiene suficiente efectivo para realizar la transacción de retiro (incluidos los cargos bancarios).
Por cada retiro exitoso el banco cobra `0.50$`.
Calcula el saldo de la cuenta de James después de un intento de transacción.
Las entradas están en el siguiente orden:
1. la cantidad de efectivo que James desea retirar está en el siguiente rango: `0 < N <= 2000`.
2. El saldo inicial de James se da con dos dígitos de precisión y está en el siguiente rango: `0 < B <= 2000`.

# --instructions--

Devuelve el saldo de la cuenta después del intento de transacción, dado como un número con dos dígitos de precisión.
Si no hay suficiente dinero en la cuenta para completar la transacción, devuelve el saldo bancario actual.

# --seed--

```python
def account_balance():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Realizar una transacción exitosa

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Fondos insuficientes

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Transacción rechazada, cantidad inválida

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Retirar todo el dinero exitosamente

```python
    def test_withdraw_all(self):
        self.assertEqual(account_balance(95, 95.50), 0.00, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def account_balance(withdraw, balance):
    if (withdraw % 5 == 0) and (balance >= (withdraw + 0.50)):
        return balance - withdraw - 0.50
    return balance
```
