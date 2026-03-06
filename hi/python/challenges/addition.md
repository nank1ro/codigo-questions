---
language: python
exerciseType: 1
title: जोड़
difficulty: 1
---

# --description--

दो पूर्णांक `num1` और `num2` दिए गए हैं, इन दोनों संख्याओं को जोड़ने के लिए एक प्रोग्राम लिखें

# --instructions--

एक फ़ंक्शन लिखें जो दो संख्याओं का योग लौटाए

# --seed--

```python
def addition():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

1 और 3 का योग 4 होना चाहिए

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

200 और 210 का योग 410 होना चाहिए

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

15 और 35 का योग 50 होना चाहिए

```python
    def test_addition3(self):
        self.assertEqual(addition(15, 35), 50, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def addition(num1, num2):
    return num1 + num2
```
