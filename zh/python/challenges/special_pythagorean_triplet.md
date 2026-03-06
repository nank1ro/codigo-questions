---
language: python
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

A Pythagorean triplet is a set of three natural numbers, `a` < `b` < `c`, for which, <latex>a^2 + b^2 = c^2</latex>

For example, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

There exists exactly one Pythagorean triplet for which `a` + `b` + `c` = 1000.

# --instructions--

Find the product `abc` such that `a` + `b` + `c` = `n`.

# --seed--

```python
def special_pythagorean_triplet(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`special_pythagorean_triplet(24)` should return 480.

```python
    def test1(self):
        self.assertEqual(special_pythagorean_triplet(24), 480, "--err-t1--")
```

`special_pythagorean_triplet(120)` should return 49920, 55080 or 60000.

```python
    def test2(self):
        self.assertIn(special_pythagorean_triplet(120), [49920, 55080, 60000], "--err-t2--")
```

`special_pythagorean_triplet(1000)` should return 31875000.

```python
    def test3(self):
        self.assertEqual(special_pythagorean_triplet(1000), 31875000, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
import math

def special_pythagorean_triplet(n):
    sumOfabc = n
    a, b, c = 0, 0, 0
    for a in range(1, int(sumOfabc / 3) + 1):
        for b in range(a + 1, int(sumOfabc / 2) + 1):
            c = math.sqrt(a * a + b * b)
            if (a + b + c) == sumOfabc:
                return a * b * c
```
