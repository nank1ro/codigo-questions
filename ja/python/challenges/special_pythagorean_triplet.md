---
language: python
exerciseType: 1
difficulty: 2
title: 特別なピタゴラス数
---

# --description--

ピタゴラスの三つ組は、3つの自然数の組`a` < `b` < `c`で、<latex>a^2 + b^2 = c^2</latex>を満たすものです。

例えば、<latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

`a` + `b` + `c` = 1000となるピタゴラスの三つ組がちょうど1つ存在します。

# --instructions--

`a` + `b` + `c` = `n`となる積`abc`を求めてください。

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

`special_pythagorean_triplet(24)`は480を返すべきです。

```python
    def test1(self):
        self.assertEqual(special_pythagorean_triplet(24), 480, "--err-t1--")
```

`special_pythagorean_triplet(120)`は49920、55080、または60000を返すべきです。

```python
    def test2(self):
        self.assertIn(special_pythagorean_triplet(120), [49920, 55080, 60000], "--err-t2--")
```

`special_pythagorean_triplet(1000)`は31875000を返すべきです。

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
