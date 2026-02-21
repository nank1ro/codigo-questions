---
language: python
exerciseType: 1
difficulty: 1
title: ¡Hola Mundo!
---

# --description--

__"¡Hola, Mundo!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.

# --instructions--

Escribe una función que devuelva la cadena "¡Hola, Mundo!".

# --seed--

```python
def hello():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

La función debe devolver "¡Hola, Mundo!".

```python
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!", "--err-t1--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def hello():
    return "Hello, World!"
```
