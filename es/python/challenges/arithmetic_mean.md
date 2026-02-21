---
language: python
exerciseType: 1
title: Media aritmética
difficulty: 1
---

# --description--

Escribe una función llamada `mean` para encontrar el _promedio aritmético_ de un vector numérico.

# --instructions--

Escribe una función que devuelva la media de un vector numérico.

Ejemplo de llamada a la función:
```python
print(mean([1, 2, 3]))
# imprime 2
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

La media de `[1, 2, 3, 4, 5, 6, 7]` debe ser igual a 4

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

La media de `[4, 5, 6]` debe ser igual a 5

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

La media de `[12, 34, 56, 78]` debe ser igual a 45

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
