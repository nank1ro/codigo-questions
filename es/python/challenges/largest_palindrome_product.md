---
language: python
exerciseType: 1
difficulty: 2
title: Mayor producto palíndromo
---

# --description--

Un número palíndromo se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.

# --instructions--

Encuentra el palíndromo más grande hecho del producto de dos números de `n` dígitos.

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

`largest_palindrome_product(2)` debe devolver 9009.

```python
    def test1(self):
        self.assertEqual(largest_palindrome_product(2), 9009, "--err-t1--")
```

`largest_palindrome_product(3)` debe devolver 906609.

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
