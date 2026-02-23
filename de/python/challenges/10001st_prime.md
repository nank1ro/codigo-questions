---
language: python
exerciseType: 1
title: 10001st prime
difficulty: 1
---

# --description--

Durch Auflisten der ersten sechs Primzahlen: 2, 3, 5, 7, 11 und 13,可以看出 dass die 6. Primzahl 13 ist.

# --instructions--

Was ist die `n`-te Primzahl?

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

`nth_prime(6)` sollte 13 zurückgeben.

```python
    def test1(self):
        self.assertEqual(nth_prime(6), 13, "--err-t1--")
```

`nth_prime(10)` sollte 29 zurückgeben.

```python
    def test2(self):
        self.assertEqual(nth_prime(10), 29, "--err-t2--")
```

`nth_prime(100)` sollte 541 zurückgeben.

```python
    def test3(self):
        self.assertEqual(nth_prime(100), 541, "--err-t3--")
```

`nth_prime(1000)` sollte 7919 zurückgeben.

```python
    def test4(self):
        self.assertEqual(nth_prime(1000), 7919, "--err-t4--")
```

`nth_prime(10001)` sollte 104743 zurückgeben.

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
