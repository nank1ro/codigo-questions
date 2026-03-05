---
language: python
exerciseType: 1
difficulty: 1
title: Deux pour un
---

# --description--

Étant donné un nom, retournez une chaîne avec le message:
`One for X, one for me.`
Où `X` est le nom donné.
Cependant, si le nom est manquant, retournez la chaîne:
`One for you, one for me.`

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples:

**entrée**: `Walter`
**sortie**: `One for Walter, one for me.`

**entrée**:
**sortie**: `One for you, one for me.`

**entrée**: `David`
**sortie**: `One for David, one for me.`

# --seed--

```python
def two_for_one(name):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Aucun nom donné

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

Passer "James" comme nom

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


Passer "Martha" comme nom

```python
    def test_another_name_given(self):
        self.assertEqual(two_for_one("Martha"), "One for Martha, one for me.", "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def two_for_one(name = None):
    if not name:
      return "One for you, one for me."
    return f"One for {name}, one for me."
```
