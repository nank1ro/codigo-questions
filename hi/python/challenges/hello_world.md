---
language: python
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ नई भाषा या वातावरण में प्रोग्रामिंग शुरू करने के लिए पारंपरिक पहला प्रोग्राम है।

# --instructions--

एक फ़ंक्शन लिखें जो स्ट्रिंग "Hello, World!" लौटाए।

# --seed--

```python
def hello():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

फ़ंक्शन को "Hello, World!" लौटाना चाहिए।

```python
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!", "--err-t1--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def hello():
    return "Hello, World!"
```
