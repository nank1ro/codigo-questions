---
language: python
exerciseType: 1
difficulty: 2
title: 最大回文積
---

# --description--

回文数は前からも後ろからも同じように読めます。2桁の数の積から作られる最大の回文数は9009 = 91 × 99です。

# --instructions--

`n`桁の数2つの積から作られる最大の回文数を見つけてください。

# --seed--

```python
def largest_palindrome_product(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`largest_palindrome_product(2)`は9009を返すべきです。

```python
    def test1(self):
        self.assertEqual(largest_palindrome_product(2), 9009, "--err-t1--")
```

`largest_palindrome_product(3)`は906609を返すべきです。

```python
    def test2(self):
        self.assertEqual(largest_palindrome_product(3), 906609, "--err-t2--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
import re

def largest_palindrome_product(digit):
  start = 1
  end = int(float(f"1e{digit}")) - 1
  palindrome = []
  for i in range(start, end+1):
    for j in range(start, end+1):
      product = i*j
      palindromeRegex = re.compile(r"\b(\d)(\d?)(\d?).?\3\2\1\b", re.IGNORECASE)
      if palindromeRegex.search(str(product)):
        palindrome.append(product)
  return max(palindrome)
```
