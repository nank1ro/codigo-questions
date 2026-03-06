---
language: python
exerciseType: 1
difficulty: 1
title: 最小公倍数
---

# --description--

2520是能被1到10中每个数字整除且没有余数的最小数字。

# --instructions--

能被1到 `n` 的所有数字整除的最小正整数是多少？

# --seed--

```python
def smallest_multiple(n) {
  
}
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`smallest_multiple(5)` 应返回 60。

```python
    def test1(self):
        self.assertEqual(smallest_multiple(5), 60, "--err-t1--")
```

`smallest_multiple(7)` 应返回 420。

```python
    def test2(self):
        self.assertEqual(smallest_multiple(7), 420, "--err-t2--")
```

`smallest_multiple(10)` 应返回 2520。

```python
    def test3(self):
        self.assertEqual(smallest_multiple(10), 2520, "--err-t3--")
```

`smallest_multiple(13)` 应返回 360360。

```python
    def test4(self):
        self.assertEqual(smallest_multiple(13), 360360, "--err-t4--")
```

`smallest_multiple(20)` 应返回 232792560。

```python
    def test5(self):
        self.assertEqual(smallest_multiple(20), 232792560, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def smallest_multiple(n):
  def gcd(a, b):
    return a if b == 0 else gcd(b, a % b) # Euclidean algorithm

  def lcm(a, b):
    return a * b / gcd(a, b)

  result = 1
  for i in range(2, n+1):
    result = lcm(result, i)

  return result
```
