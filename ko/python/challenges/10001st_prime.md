---
language: python
exerciseType: 1
difficulty: 1
title: 10001번째 소수
---

# --description--

처음 여섯 개의 소수를 나열하면: 2, 3, 5, 7, 11, 13이며, 6번째 소수는 13입니다.

# --instructions--

`n`번째 소수는 무엇입니까?

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

`nth_prime(6)`은 13을 반환해야 합니다.

```python
    def test1(self):
        self.assertEqual(nth_prime(6), 13, "--err-t1--")
```

`nth_prime(10)`은 29를 반환해야 합니다.

```python
    def test2(self):
        self.assertEqual(nth_prime(10), 29, "--err-t2--")
```

`nth_prime(100)`은 541을 반환해야 합니다.

```python
    def test3(self):
        self.assertEqual(nth_prime(100), 541, "--err-t3--")
```

`nth_prime(1000)`은 7919를 반환해야 합니다.

```python
    def test4(self):
        self.assertEqual(nth_prime(1000), 7919, "--err-t4--")
```

`nth_prime(10001)`은 104743을 반환해야 합니다.

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
