---
language: python
exerciseType: 1
title: Сложение
difficulty: 1
---

# --description--

Даны два целых числа `num1` и `num2`, напишите программу для сложения этих двух чисел

# --instructions--

Напишите функцию, которая возвращает сумму двух чисел

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

Сумма 1 и 3 должна быть равна 4

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

Сумма 200 и 210 должна быть равна 410

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

Сумма 15 и 35 должна быть равна 50

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
