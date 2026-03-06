---
language: python
exerciseType: 1
difficulty: 1
title: सबसे छोटा गुणज
---

# --description--

2520 वह सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना किसी शेष के विभाजित किया जा सकता है।

# --instructions--

वह सबसे छोटी धनात्मक संख्या कौन सी है जो 1 से `n` तक की सभी संख्याओं से समान रूप से विभाज्य है?

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

`smallest_multiple(5)` को 60 लौटाना चाहिए।

```python
    def test1(self):
        self.assertEqual(smallest_multiple(5), 60, "--err-t1--")
```

`smallest_multiple(7)` को 420 लौटाना चाहिए।

```python
    def test2(self):
        self.assertEqual(smallest_multiple(7), 420, "--err-t2--")
```

`smallest_multiple(10)` को 2520 लौटाना चाहिए।

```python
    def test3(self):
        self.assertEqual(smallest_multiple(10), 2520, "--err-t3--")
```

`smallest_multiple(13)` को 360360 लौटाना चाहिए।

```python
    def test4(self):
        self.assertEqual(smallest_multiple(13), 360360, "--err-t4--")
```

`smallest_multiple(20)` को 232792560 लौटाना चाहिए।

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
