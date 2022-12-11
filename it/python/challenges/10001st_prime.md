---
language: python
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

Elencando i primi sei numeri primi: 2, 3, 5, 7, 11 e 13, possiamo vedere che il 6° numero primo è 13.

# --instructions--

Qual è l'`n`esimo numero primo?

# --seed--

```python
def nth_prime(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`nth_prime(6)` deve restituire 13.

```python
    def test1(self):
        self.assertEqual(nth_prime(6), 13, "--err-t1--")
```

`nth_prime(10)` deve restituire 29.

```python
    def test2(self):
        self.assertEqual(nth_prime(10), 29, "--err-t2--")
```

`nth_prime(100)` deve restituire 541.

```python
    def test3(self):
        self.assertEqual(nth_prime(100), 541, "--err-t3--")
```

`nth_prime(1000)` deve restituire 7919.

```python
    def test4(self):
        self.assertEqual(nth_prime(1000), 7919, "--err-t4--")
```

`nth_prime(10001)` deve restituire 104743.

```python
    def test5(self):
        self.assertEqual(nth_prime(10001), 104743, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
import math

def nth_prime(n):
  p_n = 2
  step = 0
  while step < n:
    is_prime = True
    root_n = math.isqrt(p_n)
    for i in range(2, root_n + 1):
      if not p_n % i:
        is_prime = False
        break
    if is_prime:
      step += 1
    p_n += 1
  return p_n - 1
```
