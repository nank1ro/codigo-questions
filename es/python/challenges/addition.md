---
language: python
exerciseType: 1
title: Addition
difficulty: 1
---

# --description--

Dados dos enteros `num1` y `num2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números

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

La suma de 1 y 3 debe igual 4

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

La suma de 200 y 210 debe igual 410

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

La suma de 15 y 35 debe igual 50

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
