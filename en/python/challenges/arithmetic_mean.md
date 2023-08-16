---
language: python
exerciseType: 1
title: Arithmetic mean
difficulty: 1
---

# --description--

Write a function called `mean` to find the _arithmetic average_ of a numeric vector.

# --instructions--

Write a function that returns the mean of a numeric vector.

Example of function call:
```python
print(mean([1, 2, 3]))
# prints 2
```

# --seed--

```python
def mean():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

The mean of `[1, 2, 3, 4, 5, 6, 7]` must be equal to 4

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

The mean of `[4, 5, 6]` must be equal to 5

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

The mean of `[12, 34, 56, 78]` must be equal to 45

```python
    def test3(self):
        self.assertEqual(mean([12, 34, 56, 78]), 45, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
from math import fsum

def mean(numbers):
    return fsum(numbers) / float(len(numbers))
```
