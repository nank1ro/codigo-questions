---
language: python
exerciseType: 1
title: Largest palindrome product
difficulty: 2
---

# --description--

Eine palindromische Zahl liest sich beide Wege gleich. Das größte Palindrom, das aus dem Produkt zweier 2-stelliger Zahlen gebildet wird, ist 9009 = 91 × 99.

# --instructions--

Finden Sie das größte Palindrom, das aus dem Produkt zweier `n`-stelliger Zahlen gebildet wird.

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

`largest_palindrome_product(2)` sollte 9009 zurückgeben.

```python
    def test1(self):
        self.assertEqual(largest_palindrome_product(2), 9009, "--err-t1--")
```

`largest_palindrome_product(3)` sollte 906609 zurückgeben.

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
