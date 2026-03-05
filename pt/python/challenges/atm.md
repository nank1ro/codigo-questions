---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James gostaria de sacar N dólares de um caixa eletrônico (ATM).
O caixa eletrônico só aceitará a transação se N for um múltiplo de 5, e a conta de James tiver dinheiro suficiente para realizar a transação de saque (incluindo taxas bancárias).
Para cada saque bem-sucedido, o banco cobra `0.50$`.
Calcule o saldo da conta de James após uma tentativa de transação.
As entradas estão na seguinte ordem:
1. o valor em dinheiro que James deseja sacar está no seguinte intervalo: `0 < N <= 2000`.
2. o saldo inicial de James é dado com duas casas decimais e está no seguinte intervalo: `0 < B <= 2000`.

# --instructions--

Retorne o saldo da conta após a tentativa de transação, dado como um número com duas casas decimais.
Se não houver dinheiro suficiente na conta para completar a transação, retorne o saldo bancário atual.

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

Realizar uma transação bem-sucedida

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Fundos insuficientes

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Transação recusada, valor inválido

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Sacar todo o dinheiro com sucesso

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
