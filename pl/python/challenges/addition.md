---
language: python
exerciseType: 1
title: Dodawanie
difficulty: 1
---

# --description--

Dane są dwie liczby całkowite `num1` i `num2`, napisz program, który doda te dwie liczby

# --instructions--

Napisz funkcję, która zwraca sumę dwóch liczb

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

Suma 1 i 3 musi wynosić 4

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

Suma 200 i 210 musi wynosić 410

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

Suma 15 i 35 musi wynosić 50

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
