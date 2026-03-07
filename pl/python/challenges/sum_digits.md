---
language: python
exerciseType: 1
difficulty: 1
title: Suma cyfr
---

# --description--

Dana jest liczba całkowita `num`.
Napisz program obliczający sumę wszystkich cyfr liczby `num`

# --instructions--

Zwróć sumę cyfr liczby `num`

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

Suma cyfr liczby 12345 wynosi 15

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

Suma cyfr liczby 57253 wynosi 22

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

Suma cyfr liczby 122 wynosi 5

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

Suma cyfr liczby 91979997 wynosi 60

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

Suma cyfr liczby 2147483647 wynosi 46

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
