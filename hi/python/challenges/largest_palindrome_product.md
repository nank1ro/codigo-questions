---
language: python
exerciseType: 1
difficulty: 2
title: सबसे बड़ा पैलिंड्रोम गुणनफल
---

# --description--

एक पैलिंड्रोमिक संख्या दोनों तरफ से समान पढ़ी जाती है। दो 2-अंकीय संख्याओं के गुणनफल से बना सबसे बड़ा पैलिंड्रोम 9009 = 91 × 99 है।

# --instructions--

दो `n`-अंकीय संख्याओं के गुणनफल से बना सबसे बड़ा पैलिंड्रोम ज्ञात करें।

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

`largest_palindrome_product(2)` को 9009 लौटाना चाहिए।

```python
    def test1(self):
        self.assertEqual(largest_palindrome_product(2), 9009, "--err-t1--")
```

`largest_palindrome_product(3)` को 906609 लौटाना चाहिए।

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
