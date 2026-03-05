---
language: python
exerciseType: 1
difficulty: 1
title: 제곱합 차이
---

# --description--

처음 10개의 자연수의 제곱의 합은,

12 + 22 + ... + 102 = 385
처음 10개의 자연수의 합의 제곱은,

(1 + 2 + ... + 10)2 = 552 = 3025
따라서 처음 10개의 자연수의 제곱의 합과 합의 제곱의 차이는 3025 - 385 = 2640입니다.

# --instructions--

처음 `n`개의 자연수의 제곱의 합과 합의 제곱의 차이를 구하세요.

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

`sum_square_difference(10)`은 2640을 반환해야 합니다.

```python
    def test1(self):
        self.assertEqual(sum_square_difference(10), 2640, "--err-t1--")
```

`sum_square_difference(20)`은 41230을 반환해야 합니다.

```python
    def test2(self):
        self.assertEqual(sum_square_difference(20), 41230, "--err-t2--")
```

`sum_square_difference(100)`은 25164150을 반환해야 합니다.

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
