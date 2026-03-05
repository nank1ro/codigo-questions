---
language: python
exerciseType: 1
difficulty: 2
title: 최대 회문 곱
---

# --description--

회문수는 앞뒤로 읽어도 같은 수입니다. 두 자리 수의 곱으로 만들 수 있는 가장 큰 회문수는 9009 = 91 x 99입니다.

# --instructions--

두 `n`자리 수의 곱으로 만들 수 있는 가장 큰 회문수를 구하세요.

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

`largest_palindrome_product(2)`는 9009를 반환해야 합니다.

```python
    def test1(self):
        self.assertEqual(largest_palindrome_product(2), 9009, "--err-t1--")
```

`largest_palindrome_product(3)`은 906609를 반환해야 합니다.

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
