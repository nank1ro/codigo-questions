---
language: python
exerciseType: 1
difficulty: 1
title: 10001番目の素数
---

# --description--

最初の6つの素数をリストすると、2、3、5、7、11、13であり、6番目の素数は13であることがわかります。

# --instructions--

`n`番目の素数は何ですか？

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

`nth_prime(6)`は13を返すべきです。

```python
    def test1(self):
        self.assertEqual(nth_prime(6), 13, "--err-t1--")
```

`nth_prime(10)`は29を返すべきです。

```python
    def test2(self):
        self.assertEqual(nth_prime(10), 29, "--err-t2--")
```

`nth_prime(100)`は541を返すべきです。

```python
    def test3(self):
        self.assertEqual(nth_prime(100), 541, "--err-t3--")
```

`nth_prime(1000)`は7919を返すべきです。

```python
    def test4(self):
        self.assertEqual(nth_prime(1000), 7919, "--err-t4--")
```

`nth_prime(10001)`は104743を返すべきです。

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
