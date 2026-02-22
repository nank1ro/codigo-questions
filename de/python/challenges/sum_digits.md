---
language: python
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

You're given an integer `num`.
Write a program to calculate the sum of all the digits of `num`

# --instructions--

Return the sum of digits of `num`

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

The sum of the digits of 12345 is 15

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

The sum of the digits of 57253 is 22

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

The sum of the digits of 122 is 5

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

The sum of the digits of 91979997 is 60

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

The sum of the digits of 2147483647 is 46

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
