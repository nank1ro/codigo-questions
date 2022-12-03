---
language: python
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# --instructions--

Find the sum of all the primes below `n`.

# --seed--

```python
def prime_summation(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`prime_summation(17)` should return 41.

```python
    def test1(self):
        self.assertEqual(prime_summation(17), 41, "--err-t1--")
```

`prime_summation(2001)` should return 277050.

```python
    def test2(self):
        self.assertEqual(prime_summation(2001), 277050, "--err-t2--")
```

`prime_summation(140759)` should return 873608362.

```python
    def test3(self):
        self.assertEqual(prime_summation(140759), 873608362, "--err-t2--")
```

`prime_summation(2000000)` should return 142913828922.

```python
    def test4(self):
        self.assertEqual(prime_summation(2000000), 142913828922, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
import math

class PrimeSeive:
    def __init__(self, num):
        seive = [True] * math.floor((num - 1) / 2)
        upper = math.floor((num - 1) / 2)
        sqrtUpper = math.floor((math.sqrt(num) - 1) / 2)

        for i in range(sqrtUpper):
            if seive[i]:
                prime = 2 * i + 3
                primeSqaredIndex = 2 * i**2 + 6 * i + 3
                for j in range(primeSqaredIndex, upper, prime):
                    seive[j] = False

        self._seive = seive

    def isOddPrime(self, num):
        return self._seive[(num - 3) // 2]

def prime_summation(num):
    primeSeive = PrimeSeive(num)

    sum = 2
    for i in range(3, num, 2):
        if primeSeive.isOddPrime(i):
            sum += i
    return sum
```
