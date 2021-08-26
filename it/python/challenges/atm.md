---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James vorrebbe prelevare N euro da un bancomat.
Il bancomat accetterà la transazione solo se N è un multiplo di 5 e il conto di James ha abbastanza contante per eseguire il prelievo (incluse le commissioni bancarie).
Per ogni prelievo effettuato con successo, la banca addebita 0.50€.
Calcola il saldo del conto di James dopo un tentativo di transazione.
Gli input sono nell'ordine seguente:
1. la quantità di contanti che James desidera prelevare è nel seguente intervallo: `0 < N <= 2000`.
2. Il saldo iniziale di James viene fornito con due cifre decimali ed è nel seguente intervallo: `0 < B <= 2000`.

# --instructions--

Restituisci il saldo del conto, con due cifre decimali, dopo il tentativo di transazione.
Se non c'è abbastanza denaro nel conto per completare l'operazione, restituire il saldo bancario corrente.

# --seed--

```python
def saldo_conto():
    return
```

# --before-asserts--

```python
import unittest

class ATMTest(unittest.TestCase):
```

# --asserts--

Esegui una transazione con successo

```python
    def test_successful_transaction(self):
        self.assertEqual(saldo_conto(50, 120.00), 69.50, "--err-t1--")
```

Fondi insufficienti

```python
    def test_insufficient_funds(self):
        self.assertEqual(saldo_conto(200, 120.00), 120.00, "--err-t2--")
```

Transazione rifiutata, importo non valido

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(saldo_conto(22, 120.00), 120.00, "--err-t3--")
```

Preleva tutti i soldi con successo

```python
	def test_withdraw_all(self):
		self.assertEqual(saldo_conto(95, 95.50), 0.00, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def saldo_conto(prelievo, bilancio):
	if (prelievo % 5 == 0) and (bilancio >= (prelievo + 0.50)):
		return bilancio - prelievo - 0.50
	return bilancio
```

