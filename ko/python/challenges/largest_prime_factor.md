---
language: python
exerciseType: 1
difficulty: 2
title: 최대 소인수
---

# --description--

13195의 소인수는 5, 7, 13, 29입니다.

# --instructions--

주어진 `number`의 최대 소인수는 무엇입니까?

# --seed--

```python
def largest_prime_factor(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`largest_prime_factor(2)`는 2를 반환해야 합니다.

```python
    def test1(self):
        self.assertEqual(largest_prime_factor(2), 2, "--err-t1--")
```

`largest_prime_factor(3)`은 3을 반환해야 합니다.

```python
    def test2(self):
        self.assertEqual(largest_prime_factor(3), 3, "--err-t2--")
```

`largest_prime_factor(5)`는 5를 반환해야 합니다.

```python
    def test3(self):
        self.assertEqual(largest_prime_factor(5), 5, "--err-t3--")
```

`largest_prime_factor(7)`은 7을 반환해야 합니다.

```python
    def test4(self):
        self.assertEqual(largest_prime_factor(7), 7, "--err-t4--")
```

`largest_prime_factor(8)`은 2를 반환해야 합니다.

```python
    def test5(self):
        self.assertEqual(largest_prime_factor(8), 2, "--err-t5--")
```

`largest_prime_factor(13195)`는 29를 반환해야 합니다.

```python
    def test6(self):
        self.assertEqual(largest_prime_factor(13195), 29, "--err-t6--")
```

`largest_prime_factor(600851475143)`은 6857을 반환해야 합니다.

```python
    def test7(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857, "--err-t7--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
import math

def largest_prime_factor(number):
    largestFactor = number
    for i in range(2, int(math.sqrt(largestFactor)) + 1):
        if largestFactor % i == 0:
            factor = largestFactor / i
            candidate = largest_prime_factor(factor)
            return i if i > candidate else candidate
    return largestFactor
```
