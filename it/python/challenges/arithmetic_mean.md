---
language: python
exerciseType: 1
title: Arithmetic mean
difficulty: 1
---

# --description--

Scrivi una funzione chiamata `mean` per trovare la _media aritmetica_ di un vettore numerico.

# --instructions--

Scrivi una funzione che restituisca la media di un vettore numerico.

Esempio di chiamata di funzione:
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

La media di `[1, 2, 3, 4, 5, 6, 7]` deve essere uguale a 4.0

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

La media di `[4, 5, 6]` deve essere uguale a 5.0

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

La media di `[12, 34, 56, 78]` deve essere uguale a 45.0

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
