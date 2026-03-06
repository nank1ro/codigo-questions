---
language: python
exerciseType: 1
difficulty: 2
title: 특수 피타고라스 삼중수
---

# --description--

피타고라스 삼중수는 세 자연수의 집합으로, `a` < `b` < `c`이며, <latex>a^2 + b^2 = c^2</latex>를 만족합니다.

예를 들어, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

`a` + `b` + `c` = 1000인 피타고라스 삼중수는 정확히 하나 존재합니다.

# --instructions--

`a` + `b` + `c` = `n`인 곱 `abc`를 구하세요.

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

`special_pythagorean_triplet(24)`는 480을 반환해야 합니다.

```python
    def test1(self):
        self.assertEqual(special_pythagorean_triplet(24), 480, "--err-t1--")
```

`special_pythagorean_triplet(120)`은 49920, 55080 또는 60000을 반환해야 합니다.

```python
    def test2(self):
        self.assertIn(special_pythagorean_triplet(120), [49920, 55080, 60000], "--err-t2--")
```

`special_pythagorean_triplet(1000)`은 31875000을 반환해야 합니다.

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
