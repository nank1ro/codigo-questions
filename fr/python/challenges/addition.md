---
language: python
exerciseType: 1
title: Addition
difficulty: 1
---

# --description--

Étant donné deux entiers `num1` et `num2`, écrivez un programme pour ajouter ces deux nombres

# --instructions--

Écrivez une fonction qui retourne la somme de deux nombres

# --seed--

```python
def addition():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

La somme de 1 et 3 doit être égale à 4

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

La somme de 200 et 210 doit être égale à 410

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

La somme de 15 et 35 doit être égale à 50

```python
    def test_addition3(self):
        self.assertEqual(addition(15, 35), 50, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def addition(num1, num2):
    return num1 + num2
```
