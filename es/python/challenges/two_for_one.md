---
language: python
exerciseType: 1
title: Dos por uno
difficulty: 1
---

# --description--

Dado un nombre, devuelve una cadena con el mensaje:
`Uno para X, uno para mí.`
Donde `X` es el nombre dado.
Sin embargo, si falta el nombre, devuelve la cadena:
`Uno para ti, uno para mí.`

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

**entrada**: `Walter`
**salida**: `Uno para Walter, uno para mí.`

**entrada**:
**salida**: `Uno para ti, uno para mí.`

**entrada**: `David`
**salida**: `Uno para David, uno para mí.`

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

No se da ningún nombre

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

Pasar "James" como nombre

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```

Pasar "Martha" como nombre

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
