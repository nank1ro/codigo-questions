---
language: python
exerciseType: 1
title: Среднее арифметическое
difficulty: 1
---

# --description--

Напишите функцию `mean` для нахождения _среднего арифметического_ числового вектора.

# --instructions--

Напишите функцию, которая возвращает среднее арифметическое числового вектора.

Пример вызова функции:
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

Среднее арифметическое `[1, 2, 3, 4, 5, 6, 7]` должно быть равно 4

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

Среднее арифметическое `[4, 5, 6]` должно быть равно 5

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

Среднее арифметическое `[12, 34, 56, 78]` должно быть равно 45

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
