---
language: python
exerciseType: 1
title: Suma
difficulty: 1
---

# --description--

Dados dos enteros `numero1` y `numero2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números

# --seed--

```python
def suma():
    pass
```

# --before-asserts--

```python
import unittest

class PruebasCodigo(unittest.TestCase):
```

# --asserts--

La suma de 1 y 3 debe ser igual a 4

```python
    def test1(self):
        self.assertEqual(suma(1, 3), 4, "--err-t1--")
```

La suma de 200 y 210 debe ser igual a 410

```python
    def test2(self):
        self.assertEqual(suma(200, 210), 410, "--err-t2--")
```

La suma de 15 y 35 debe ser igual a 50

```python
    def test3(self):
        self.assertEqual(suma(15, 35), 50, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def suma(numero1, numero2):
	return numero1 + numero2
```
