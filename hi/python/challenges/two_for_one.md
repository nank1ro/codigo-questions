---
language: python
exerciseType: 1
difficulty: 1
title: दो में से एक
---

# --description--

एक नाम दिया गया है, इस संदेश के साथ एक स्ट्रिंग लौटाएं:
`One for X, one for me.`
जहां `X` दिया गया नाम है।
हालांकि, अगर नाम नहीं दिया गया है, तो यह स्ट्रिंग लौटाएं:
`One for you, one for me.`

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

**इनपुट**: `Walter`
**आउटपुट**: `One for Walter, one for me.`

**इनपुट**:
**आउटपुट**: `One for you, one for me.`

**इनपुट**: `David`
**आउटपुट**: `One for David, one for me.`

# --seed--

```python
def two_for_one(name):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

कोई नाम नहीं दिया गया

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

नाम के रूप में "James" पास करें

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


नाम के रूप में "Martha" पास करें

```python
    def test_another_name_given(self):
        self.assertEqual(two_for_one("Martha"), "One for Martha, one for me.", "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def two_for_one(name = None):
    if not name:
      return "One for you, one for me."
    return f"One for {name}, one for me."
```
