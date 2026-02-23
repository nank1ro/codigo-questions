---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James möchte N Dollar von einem Geldautomaten abheben.
Der Geldautomat akzeptiert die Transaktion nur, wenn N ein Vielfaches von 5 ist und James' Konto genug Geld hat, um die Abhebungstransaktion durchzuführen (einschließlich Bankgebühren).
Für jede erfolgreiche Abhebung berechnet die Bank `0,50 $`.
Berechnen Sie das Kontoguthaben von James nach einem Transaktionsversuch.
Die Eingaben sind in folgender Reihenfolge:
1. Der Betrag, den James abheben möchte, liegt im folgenden Bereich: `0 < N <= 2000`.
2. Das anfängliche Guthaben von James wird mit zwei Dezimalstellen angegeben und liegt im folgenden Bereich: `0 < B <= 2000`.

# --instructions--

Geben Sie das Kontoguthaben nach dem Transaktionsversuch zurück, angegeben als Zahl mit zwei Dezimalstellen.
Wenn nicht genug Geld auf dem Konto vorhanden ist, um die Transaktion abzuschließen, geben Sie das aktuelle Bankguthaben zurück.

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

Eine erfolgreiche Transaktion durchführen

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Unzureichende Mittel

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Abgelehnte Transaktion, ungültiger Betrag

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Erfolgreich alles Geld abheben

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
