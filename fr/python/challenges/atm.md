---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James souhaite retirer N dollars d'un guichet automatique.
La machine à sous n'acceptera la transaction que si N est un multiple de 5, et le compte de James dispose de suffisamment de liquidités pour effectuer la transaction de retrait (y compris les frais bancaires).
Pour chaque retrait réussi, la banque facture `0,50 $`.
Calculez le solde du compte de James après une tentative de transaction.
Les entrées sont dans l'ordre suivant:
1. le montant en espèces que James souhaite retirer est dans la plage suivante: `0 < N <= 2000`.
2. Le solde initial de James est donné avec deux décimales et est dans la plage suivante: `0 < B <= 2000`.

# --instructions--

Retournez le solde du compte après la tentative de transaction, exprimé en nombre avec deux décimales.
S'il n'y a pas assez d'argent sur le compte pour effectuer la transaction, retournez le solde bancaire actuel.

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

Effectuer une transaction réussie

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Fonds insuffisants

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Transaction refusée, montant invalide

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Retirer tout l'argent avec succès

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
