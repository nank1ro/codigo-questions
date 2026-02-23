---
language: python
exerciseType: 1
title: Special pythagorean triplet
difficulty: 2
---

# --description--

Ein pythagoreisches Tripel ist ein Satz von drei natürlichen Zahlen, `a` < `b` < `c`, für den gilt: <latex>a^2 + b^2 = c^2</latex>

Zum Beispiel: <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

Es gibt genau ein pythagoreisches Tripel, für das `a` + `b` + `c` = 1000 gilt.

# --instructions--

Finden Sie das Produkt `abc` so, dass `a` + `b` + `c` = `n` gilt.

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

`special_pythagorean_triplet(24)` sollte 480 zurückgeben.

```python
    def test1(self):
        self.assertEqual(special_pythagorean_triplet(24), 480, "--err-t1--")
```

`special_pythagorean_triplet(120)` sollte 49920, 55080 oder 60000 zurückgeben.

```python
    def test2(self):
        self.assertIn(special_pythagorean_triplet(120), [49920, 55080, 60000], "--err-t2--")
```

`special_pythagorean_triplet(1000)` sollte 31875000 zurückgeben.

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
