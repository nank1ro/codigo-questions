---
language: python
exerciseType: 1
difficulty: 1
title: Due per uno
---

# --description--

Dato un nome, restituire una stringa con il messaggio:
`Uno per X, uno per me.`
Dove `X` e' il nome dato.
Tuttavia, se il nome manca, restituire la stringa:
`Uno per te, uno per me.`

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

**input**: `Walter`
**output**: `Uno per Walter, uno per me.`

**input**:
**output**: `Uno per te, uno per me.`

**input**: `Davide`
**output**: `Uno per Davide, uno per me.`

# --seed--

```python
def due_per_uno(nome):
    pass
```

# --before-asserts--

```python
import unittest

class TwoForOneTest(unittest.TestCase):
```

# --asserts--

Dividi con qualcuno

```python
    def test_no_name_given(self):
        self.assertEqual(due_per_uno(), "Uno per te, uno per me.", "--err-t1--")
```

Dividi con "Daniele"

```python
    def test_a_name_given(self):
        self.assertEqual(due_per_uno("Daniele"), "Uno per Daniele, uno per me.", "--err-t2--")
```


Dividi con "Marta"

```python
    def test_another_name_given(self):
        self.assertEqual(due_per_uno("Marta"), "Uno per Marta, uno per me.", "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def due_per_uno(nome = None):
    if not nome:
      return "Uno per te, uno per me."
    return f"Uno per {nome}, uno per me."
```
