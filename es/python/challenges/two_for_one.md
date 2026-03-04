---
language: python
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Dado un nombre, devuelve una cadena con el mensaje:
`One for X, one for me.`
Donde `X` es el nombre dado.
Sin embargo, si falta el nombre, devuelve la cadena:
`One for you, one for me.`

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

**entrada**: `Walter`
**salida**: `One for Walter, one for me.`

**entrada**:
**salida**: `One for you, one for me.`

**entrada**: `David`
**salida**: `One for David, one for me.`

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

No se da nombre

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

Pasa "James" como nombre

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


Pasa "Martha" como nombre

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
