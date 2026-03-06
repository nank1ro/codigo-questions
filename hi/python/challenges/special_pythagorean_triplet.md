---
language: python
exerciseType: 1
difficulty: 2
title: विशेष पाइथागोरियन त्रिक
---

# --description--

पाइथागोरियन त्रिक तीन प्राकृतिक संख्याओं का एक समूह है, `a` < `b` < `c`, जिसके लिए, <latex>a^2 + b^2 = c^2</latex>

उदाहरण के लिए, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

ठीक एक पाइथागोरियन त्रिक मौजूद है जिसके लिए `a` + `b` + `c` = 1000।

# --instructions--

गुणनफल `abc` ज्ञात करें जहाँ `a` + `b` + `c` = `n`।

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

`special_pythagorean_triplet(24)` को 480 लौटाना चाहिए।

```python
    def test1(self):
        self.assertEqual(special_pythagorean_triplet(24), 480, "--err-t1--")
```

`special_pythagorean_triplet(120)` को 49920, 55080 या 60000 लौटाना चाहिए।

```python
    def test2(self):
        self.assertIn(special_pythagorean_triplet(120), [49920, 55080, 60000], "--err-t2--")
```

`special_pythagorean_triplet(1000)` को 31875000 लौटाना चाहिए।

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
