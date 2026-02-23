---
language: python
exerciseType: 1
title: Largest prime factor
difficulty: 2
---

# --description--

Die Primfaktoren von 13195 sind 5, 7, 13 und 29.

# --instructions--

Was ist der größte Primfaktor der angegebenen `number`?

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

`largest_prime_factor(2)` sollte 2 zurückgeben.

```python
    def test1(self):
        self.assertEqual(largest_prime_factor(2), 2, "--err-t1--")
```

`largest_prime_factor(3)` sollte 3 zurückgeben.

```python
    def test2(self):
        self.assertEqual(largest_prime_factor(3), 3, "--err-t2--")
```

`largest_prime_factor(5)` sollte 5 zurückgeben.

```python
    def test3(self):
        self.assertEqual(largest_prime_factor(5), 5, "--err-t3--")
```

`largest_prime_factor(7)` sollte 7 zurückgeben.

```python
    def test4(self):
        self.assertEqual(largest_prime_factor(7), 7, "--err-t4--")
```

`largest_prime_factor(8)` sollte 2 zurückgeben.

```python
    def test5(self):
        self.assertEqual(largest_prime_factor(8), 2, "--err-t5--")
```

`largest_prime_factor(13195)` sollte 29 zurückgeben.

```python
    def test6(self):
        self.assertEqual(largest_prime_factor(13195), 29, "--err-t6--")
```

`largest_prime_factor(600851475143)` sollte 6857 zurückgeben.

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
