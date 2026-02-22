---
language: python
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# --instructions--

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to `n`?

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

`smallest_multiple(5)` should return 60.

```python
    def test1(self):
        self.assertEqual(smallest_multiple(5), 60, "--err-t1--")
```

`smallest_multiple(7)` should return 420.

```python
    def test2(self):
        self.assertEqual(smallest_multiple(7), 420, "--err-t2--")
```

`smallest_multiple(10)` should return 2520.

```python
    def test3(self):
        self.assertEqual(smallest_multiple(10), 2520, "--err-t3--")
```

`smallest_multiple(13)` should return 360360.

```python
    def test4(self):
        self.assertEqual(smallest_multiple(13), 360360, "--err-t4--")
```

`smallest_multiple(20)` should return 232792560.

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
