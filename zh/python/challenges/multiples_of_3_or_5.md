---
language: python
exerciseType: 1
difficulty: 1
title: 3或5的倍数
---

# --description--

如果我们列出10以下所有3或5的倍数的自然数，我们得到3、5、6和9。这些倍数的和是23。

# --instructions--

求给定参数值 `number` 以下所有3或5的倍数之和。

# --seed--

```python
def multiples_of_3_and_5(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`multiples_of_3_and_5(10)` 应返回 23。

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)` 应返回 233168。

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)` 应返回 11390208

```python
    def test3(self):
        self.assertEqual(multiples_of_3_and_5(6987), 11390208, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def multiples_of_3_and_5(number):
  total = 0
  for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total
```
