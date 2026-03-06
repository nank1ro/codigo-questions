---
language: python
exerciseType: 1
title: Ackermann फ़ंक्शन
difficulty: 1
---

# --description--

Ackermann फ़ंक्शन एक पुनरावर्ती फ़ंक्शन का एक उत्कृष्ट उदाहरण है, विशेष रूप से उल्लेखनीय क्योंकि यह एक प्राथमिक पुनरावर्ती फ़ंक्शन नहीं है। इसका मान बहुत तेज़ी से बढ़ता है, जैसा कि इसके कॉल ट्री का आकार भी बढ़ता है।

Ackermann फ़ंक्शन को आमतौर पर निम्नानुसार परिभाषित किया जाता है:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

इसके आर्गुमेंट कभी ऋणात्मक नहीं होते और यह हमेशा समाप्त होता है

# --instructions--

एक फ़ंक्शन लिखें जो Ackermann फ़ंक्शन का मान लौटाए।

# --seed--

```python
def ack(m, n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`ack(0, 0)` को 1 लौटाना चाहिए।

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` को 3 लौटाना चाहिए।

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` को 13 लौटाना चाहिए।

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` को 61 लौटाना चाहिए।

```python
    def test4(self):
        self.assertEqual(ack(3, 3), 61, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def ack(m, n):
    if m == 0:
        return n + 1
    else:
        if (n == 0):
            return ack(m - 1, 1)
        return ack(m - 1, ack(m, n - 1))
```
