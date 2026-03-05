---
language: python
exerciseType: 1
difficulty: 1
title: 平方和の差
---

# --description--

最初の10個の自然数の二乗の和は、

12 + 22 + ... + 102 = 385
最初の10個の自然数の和の二乗は、

(1 + 2 + ... + 10)2 = 552 = 3025
したがって、最初の10個の自然数の二乗の和と和の二乗の差は3025 − 385 = 2640です。

# --instructions--

最初の`n`個の自然数の二乗の和と和の二乗の差を求めてください。

# --seed--

```python
def sum_square_difference(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`sum_square_difference(10)`は2640を返すべきです。

```python
    def test1(self):
        self.assertEqual(sum_square_difference(10), 2640, "--err-t1--")
```

`sum_square_difference(20)`は41230を返すべきです。

```python
    def test2(self):
        self.assertEqual(sum_square_difference(20), 41230, "--err-t2--")
```

`sum_square_difference(100)`は25164150を返すべきです。

```python
    def test3(self):
        self.assertEqual(sum_square_difference(100), 25164150, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def sum_square_difference(number):
    square_of_sum = pow(sum_of_arithmetic_series(1, 1, number), 2)
    sum_of_square = sum_of_square_of_numbers(number)
    return square_of_sum - sum_of_square

def sum_of_arithmetic_series(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)

def sum_of_square_of_numbers(n):
    return (n * (n + 1) * (2 * n + 1)) / 6
```
