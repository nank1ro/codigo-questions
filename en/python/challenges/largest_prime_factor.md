---
language: python
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

The prime factors of 13195 are 5, 7, 13 and 29.

# --instructions--

What is the largest prime factor of the given `number`?

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

`largest_prime_factor(2)` should return 2.

```python
    def test1(self):
        self.assertEqual(largest_prime_factor(2), 2, "--err-t1--")
```

`largest_prime_factor(3)` should return 3.

```python
    def test2(self):
        self.assertEqual(largest_prime_factor(3), 3, "--err-t2--")
```

`largest_prime_factor(5)` should return 5.

```python
    def test3(self):
        self.assertEqual(largest_prime_factor(5), 5, "--err-t3--")
```

`largest_prime_factor(7)` should return 7.

```python
    def test4(self):
        self.assertEqual(largest_prime_factor(7), 7, "--err-t4--")
```

`largest_prime_factor(8)` should return 2.

```python
    def test5(self):
        self.assertEqual(largest_prime_factor(8), 2, "--err-t5--")
```

`largest_prime_factor(13195)` should return 29.

```python
    def test6(self):
        self.assertEqual(largest_prime_factor(13195), 29, "--err-t6--")
```

`largest_prime_factor(600851475143)` should return 6857.

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
