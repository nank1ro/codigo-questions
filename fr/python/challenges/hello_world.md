---
language: python
exerciseType: 1
difficulty: 1
title: Bonjour le monde !
---

# --description--

__"Bonjour, le monde !"__ est le programme traditionnel du premier jour pour commencer la programmation dans un nouveau langage ou environnement.

# --instructions--

Écrivez une fonction qui retourne la chaîne "Hello, World!".

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

La fonction doit retourner "Hello, World!".

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
