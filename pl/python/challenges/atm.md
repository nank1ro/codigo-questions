---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James chciałby wypłacić N dolarów z bankomatu.
Maszyna zaakceptuje transakcję tylko wtedy, gdy N jest wielokrotnością 5 i James ma wystarczającą ilość gotówki, aby wykonać transakcję wypłaty (wliczając opłaty bankowe).
Za każdą udaną wypłatę bank pobiera `0.50$`.
Oblicz saldo konta Jamesa po próbie wykonania transakcji.
Dane wejściowe są w następującej kolejności:
1. kwota gotówki, którą James chce wypłacić, mieści się w następującym zakresie: `0 < N <= 2000`.
2. początkowe saldo Jamesa jest podane z dokładnością do dwóch miejsc dziesiętnych i mieści się w zakresie: `0 < B <= 2000`.

# --instructions--

Zwróć saldo konta po próbie wykonania transakcji, jako liczbę z dokładnością do dwóch miejsc dziesiętnych.
Jeśli na koncie nie ma wystarczających środków do realizacji transakcji, zwróć aktualne saldo bankowe.

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

Wykonaj udaną transakcję

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Niewystarczające środki

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Odrzucona transakcja, nieprawidłowa kwota

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Wypłać wszystkie środki pomyślnie

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
