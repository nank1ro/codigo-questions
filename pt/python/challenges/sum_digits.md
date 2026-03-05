---
language: python
exerciseType: 1
difficulty: 1
title: Soma dos dígitos
---

# --description--

Você recebe um inteiro `num`.
Escreva um programa para calcular a soma de todos os dígitos de `num`

# --instructions--

Retorne a soma dos dígitos de `num`

# --seed--

```python
def sum_digits(num: int):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

A soma dos dígitos de 12345 é 15

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

A soma dos dígitos de 57253 é 22

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

A soma dos dígitos de 122 é 5

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

A soma dos dígitos de 91979997 é 60

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

A soma dos dígitos de 2147483647 é 46

```python
    def test_sum_of_digits_5(self):
        self.assertEqual(sum_digits(2147483647), 46, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def sum_digits(num: int):
    result = 0
    while num > 0:
      result += num % 10
      num //= 10
    return result
```
