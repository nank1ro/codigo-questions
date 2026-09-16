---
language: python
exerciseType: 1
difficulty: 2
title: सीज़र सिफर
---

# --description--

जूलियस सीज़र ने क्रिप्टोग्राफी की सबसे पुरानी तरकीबों में से एक से अपनी निजी चिट्ठियों को सुरक्षित रखा था: वे किसी संदेश के हर अक्षर को वर्णमाला में एक निश्चित संख्या में आगे स्थित अक्षर से बदल देते थे। 3 के शिफ्ट पर `a`, `d` बन जाता है, `b`, `e` बन जाता है और `c`, `f` बन जाता है।

वर्णमाला एक वृत्त जैसा व्यवहार करती है, इसलिए अंत के अक्षर घूमकर वापस शुरुआत पर पहुँच जाते हैं: 3 के शिफ्ट पर `x`, `a` बन जाता है, `y`, `b` बन जाता है और `z`, `c` बन जाता है।

जो कुछ भी अक्षर नहीं है, जैसे रिक्त स्थान, अल्पविराम, विस्मयादिबोधक चिह्न या अंक, वह सिफर से बिना बदले गुज़र जाता है।

# --instructions--

एक फ़ंक्शन `caesar_cipher` लिखें जो एक संदेश `text` और एक पूर्ण संख्या `shift` लेता है, और एन्कोड किया हुआ संदेश लौटाता है।

उदाहरण:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- संदेश हमेशा लोअरकेस में होता है, इसलिए आपको कभी भी अपरकेस अक्षरों से निपटना नहीं पड़ेगा।
- जो वर्ण अक्षर नहीं हैं, वे अपनी जगह और अपना मान बनाए रखते हैं।
- शिफ्ट कभी ऋणात्मक नहीं होता। `0` का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है, और `26` का शिफ्ट भी ऐसा ही करता है।

# --seed--

```python
def caesar_cipher(text, shift):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

3 का शिफ्ट "hello" को "khoor" में बदल देता है

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

वर्णमाला का अंत घूमकर शुरुआत पर वापस आ जाता है, इसलिए "xyz", "abc" बन जाता है

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

0 का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

26 का शिफ्ट वर्णमाला का एक पूरा चक्र है, इसलिए संदेश अपरिवर्तित रहता है

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

विराम चिह्न और रिक्त स्थान बिना बदले गुज़र जाते हैं

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

खाली संदेश खाली ही रहता है

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

अक्षरों के बीच के रिक्त स्थान बने रहते हैं

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

25 के शिफ्ट पर भी अंक शिफ्ट नहीं होते

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

13 का शिफ्ट एक पूरे वाक्य को एन्कोड कर देता है

```python
    def test9(self):
        self.assertEqual(caesar_cipher("the quick brown fox jumps over the lazy dog", 13), "gur dhvpx oebja sbk whzcf bire gur ynml qbt", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
        else:
            result += char

    return result
```
