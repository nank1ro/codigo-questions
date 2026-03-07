---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

Джеймс хочет снять N долларов в ATM.
Банкомат примет транзакцию только в том случае, если N кратно 5, и на счёте Джеймса достаточно средств для выполнения операции снятия (включая банковскую комиссию).
За каждое успешное снятие банк взимает комиссию `0.50$`.
Рассчитайте баланс счёта Джеймса после попытки транзакции.
Входные данные задаются в следующем порядке:
1. сумма, которую Джеймс хочет снять, находится в диапазоне: `0 < N <= 2000`.
2. начальный баланс Джеймса задаётся с точностью до двух знаков после запятой и находится в диапазоне: `0 < B <= 2000`.

# --instructions--

Верните баланс счёта после попытки транзакции в виде числа с точностью до двух знаков после запятой.
Если на счёте недостаточно средств для выполнения транзакции, верните текущий баланс.

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

Выполнить успешную транзакцию

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Недостаточно средств

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Отклонённая транзакция, недопустимая сумма

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Успешно снять все средства

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
