---
language: python
exerciseType: 1
title: 算术平均值
difficulty: 1
---

# --description--

编写一个名为 `mean` 的函数，用于计算数字向量的_算术平均值_。

# --instructions--

编写一个函数，返回数字向量的平均值。

函数调用示例：
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

`[1, 2, 3, 4, 5, 6, 7]` 的平均值必须等于4

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

`[4, 5, 6]` 的平均值必须等于5

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

`[12, 34, 56, 78]` 的平均值必须等于45

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
