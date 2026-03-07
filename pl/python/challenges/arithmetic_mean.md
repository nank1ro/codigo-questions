---
language: python
exerciseType: 1
title: Średnia arytmetyczna
difficulty: 1
---

# --description--

Napisz funkcję o nazwie `mean`, która znajduje _średnią arytmetyczną_ wektora liczbowego.

# --instructions--

Napisz funkcję, która zwraca średnią wektora liczbowego.

Przykład wywołania funkcji:
```python
print(mean([1, 2, 3]))
# drukuje 2
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

Średnia z `[1, 2, 3, 4, 5, 6, 7]` musi wynosić 4

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

Średnia z `[4, 5, 6]` musi wynosić 5

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

Średnia z `[12, 34, 56, 78]` musi wynosić 45

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
