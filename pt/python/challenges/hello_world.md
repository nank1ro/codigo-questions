---
language: python
exerciseType: 1
difficulty: 1
title: Olá Mundo!
---

# --description--

__"Hello, World!"__ é o programa tradicional inicial para começar a programar em uma nova linguagem ou ambiente.

# --instructions--

Escreva uma função que retorne a string "Hello, World!".

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

A função deve retornar "Hello, World!".

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
