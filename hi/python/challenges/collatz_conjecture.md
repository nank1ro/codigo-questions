---
language: python
exerciseType: 1
difficulty: 1
title: कोलैट्ज़ अनुमान
---

# --description--

कोलैट्ज़ अनुमान किसी भी धनात्मक पूर्णांक `n` से शुरू होकर एक ही सरल नियम दोहराता है: यदि `n` सम है, तो उसे आधा कर दें; यदि `n` विषम है, तो उसे `3n + 1` से बदल दें। कभी न कभी अनुक्रम 1 तक पहुँच जाता है।

उदाहरण के लिए, 16 से शुरू करने पर अनुक्रम `16 -> 8 -> 4 -> 2 -> 1` होता है, इसलिए इसमें 4 चरण लगते हैं।

अब तक किसी ने भी यह सिद्ध नहीं किया है कि ऐसा हमेशा होता है, लेकिन यह अब तक परीक्षण की गई हर संख्या पर लागू होता है।

# --instructions--

`collatz_steps` नाम का एक फ़ंक्शन लिखें जो एक धनात्मक पूर्णांक `n` लेता है और 1 तक पहुँचने के लिए आवश्यक चरणों की संख्या लौटाता है।

`collatz_steps(1)` का मान 0 है, क्योंकि 1 पहले से ही अनुक्रम का अंत है। `collatz_steps(12)` का मान 9 है, और `collatz_steps(27)` का मान 111 है।

# --seed--

```python
def collatz_steps(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`collatz_steps(1)` को 0 लौटाना चाहिए, क्योंकि 1 पहले से ही अनुक्रम का अंत है।

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` को 1 लौटाना चाहिए।

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` को 8 लौटाना चाहिए।

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` को 16 लौटाना चाहिए।

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` को 4 लौटाना चाहिए।

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` को 9 लौटाना चाहिए।

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` को 111 लौटाना चाहिए।

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` को 118 लौटाना चाहिए।

```python
    def test8(self):
        self.assertEqual(collatz_steps(97), 118, "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def collatz_steps(n):
    value = n
    steps = 0
    while value != 1:
        value = value // 2 if value % 2 == 0 else 3 * value + 1
        steps += 1
    return steps
```
