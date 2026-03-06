---
language: python
exerciseType: 1
difficulty: 1
title: अंकों का योग
---

# --description--

आपको एक पूर्णांक `num` दिया गया है।
`num` के सभी अंकों का योग गणना करने के लिए एक प्रोग्राम लिखें

# --instructions--

`num` के अंकों का योग लौटाएं

# --seed--

```python
def sum_digits(num: int):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

12345 के अंकों का योग 15 है

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

57253 के अंकों का योग 22 है

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

122 के अंकों का योग 5 है

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

91979997 के अंकों का योग 60 है

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

2147483647 के अंकों का योग 46 है

```python
    def test_sum_of_digits_5(self):
        self.assertEqual(sum_digits(2147483647), 46, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def sum_digits(num: int):
    result = 0
    while num > 0:
      result += num % 10
      num //= 10
    return result
```
