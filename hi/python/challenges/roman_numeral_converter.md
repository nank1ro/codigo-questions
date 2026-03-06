---
language: python
exerciseType: 1
difficulty: 3
title: रोमन अंक परिवर्तक
---

# --description--

एक फ़ंक्शन बनाएं जो एक धनात्मक पूर्णांक को अपने पैरामीटर के रूप में लेता है और उस पूर्णांक के रोमन अंक प्रतिनिधित्व वाली एक स्ट्रिंग लौटाता है। आधुनिक रोमन अंक प्रत्येक अंक को अलग-अलग व्यक्त करके लिखे जाते हैं, सबसे बाएं अंक से शुरू करते हुए और शून्य मान वाले किसी भी अंक को छोड़ते हुए।

# --instructions--

उदाहरण:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- सभी रोमन अंक अपरकेस में लौटाए जाने चाहिए।
- इस अंकन में दर्शाई जा सकने वाली सबसे बड़ी संख्या 3,999 है।

# --seed--

```python
def convert_to_roman(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

संख्या `2` का परिणाम `II` होना चाहिए

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

संख्या `12` का परिणाम `XII` होना चाहिए

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

संख्या `16` का परिणाम `XVI` होना चाहिए

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

संख्या `44` का परिणाम `XLIV` होना चाहिए

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

संख्या `68` का परिणाम `LXVIII` होना चाहिए

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

संख्या `400` का परिणाम `CD` होना चाहिए

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

संख्या `798` का परिणाम `DCCXCVIII` होना चाहिए

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

संख्या `1000` का परिणाम `M` होना चाहिए

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

संख्या `3999` का परिणाम `MMMCMXCIX` होना चाहिए

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

संख्या `649` का परिणाम `DCXLIX` होना चाहिए

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

संख्या `1666` का परिणाम `MDCLXVI` होना चाहिए

```python
    def test11(self):
        self.assertEqual(convert_to_roman(1666), "MDCLXVI", "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def convert_to_roman(n):
    result = ""

    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    for value, letter in values:
        while n >= value:
            result += letter
            n -= value

    return result
```
