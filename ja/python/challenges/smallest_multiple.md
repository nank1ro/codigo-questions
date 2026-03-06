---
language: python
exerciseType: 1
difficulty: 1
title: 最小公倍数
---

# --description--

2520は1から10までのすべての数で余りなく割り切れる最小の数です。

# --instructions--

1から`n`までのすべての数で割り切れる最小の正の数は何ですか？

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

`smallest_multiple(5)`は60を返すべきです。

```python
    def test1(self):
        self.assertEqual(smallest_multiple(5), 60, "--err-t1--")
```

`smallest_multiple(7)`は420を返すべきです。

```python
    def test2(self):
        self.assertEqual(smallest_multiple(7), 420, "--err-t2--")
```

`smallest_multiple(10)`は2520を返すべきです。

```python
    def test3(self):
        self.assertEqual(smallest_multiple(10), 2520, "--err-t3--")
```

`smallest_multiple(13)`は360360を返すべきです。

```python
    def test4(self):
        self.assertEqual(smallest_multiple(13), 360360, "--err-t4--")
```

`smallest_multiple(20)`は232792560を返すべきです。

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
