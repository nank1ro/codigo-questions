---
language: python
exerciseType: 1
difficulty: 1
title: 第10001个素数
---

# --description--

列出前六个素数：2、3、5、7、11和13，我们可以看到第6个素数是13。

# --instructions--

第`n`个素数是什么？

# --seed--

```python
def nth_prime(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`nth_prime(6)` 应返回 13。

```python
    def test1(self):
        self.assertEqual(nth_prime(6), 13, "--err-t1--")
```

`nth_prime(10)` 应返回 29。

```python
    def test2(self):
        self.assertEqual(nth_prime(10), 29, "--err-t2--")
```

`nth_prime(100)` 应返回 541。

```python
    def test3(self):
        self.assertEqual(nth_prime(100), 541, "--err-t3--")
```

`nth_prime(1000)` 应返回 7919。

```python
    def test4(self):
        self.assertEqual(nth_prime(1000), 7919, "--err-t4--")
```

`nth_prime(10001)` 应返回 104743。

```python
    def test5(self):
        self.assertEqual(nth_prime(10001), 104743, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
import math

def nth_prime(n):
  p_n = 2
  step = 0
  while step < n:
    is_prime = True
    root_n = math.isqrt(p_n)
    for i in range(2, root_n + 1):
      if not p_n % i:
        is_prime = False
        break
    if is_prime:
      step += 1
    p_n += 1
  return p_n - 1
```
