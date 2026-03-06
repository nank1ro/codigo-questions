---
language: python
exerciseType: 1
title: अंकगणितीय माध्य
difficulty: 1
---

# --description--

एक `mean` नामक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का _अंकगणितीय औसत_ ज्ञात करे।

# --instructions--

एक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का माध्य लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```python
print(mean([1, 2, 3]))
# prints 2
```

# --seed--

```python
def mean():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]` का माध्य 4 के बराबर होना चाहिए

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

`[4, 5, 6]` का माध्य 5 के बराबर होना चाहिए

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

`[12, 34, 56, 78]` का माध्य 45 के बराबर होना चाहिए

```python
    def test3(self):
        self.assertEqual(mean([12, 34, 56, 78]), 45, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
from math import fsum

def mean(numbers):
    return fsum(numbers) / float(len(numbers))
```
