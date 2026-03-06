---
language: python
exerciseType: 1
title: 算術平均
difficulty: 1
---

# --description--

数値ベクトルの_算術平均_を求める`mean`という関数を書いてください。

# --instructions--

数値ベクトルの平均を返す関数を書いてください。

関数呼び出しの例：
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

`[1, 2, 3, 4, 5, 6, 7]`の平均は4でなければなりません

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

`[4, 5, 6]`の平均は5でなければなりません

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

`[12, 34, 56, 78]`の平均は45でなければなりません

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
