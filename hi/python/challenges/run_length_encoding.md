---
language: python
exerciseType: 1
difficulty: 2
title: रन लंबाई एन्कोडिंग
---

# --description--

रन लंबाई एन्कोडिंग संपीड़न की सबसे पुरानी तरकीबों में से एक है: एक ही अक्षर को बार-बार लिखने के बजाय, आप लिख देते हैं कि वह अक्षर कितनी बार दोहराया गया है और फिर उस अक्षर को स्वयं लिख देते हैं।

ज़्यादातर खाली पन्ने को स्कैन करती एक फ़ैक्स मशीन को एक जैसे पिक्सेल के लंबे खिंचाव मिलते हैं, इसलिए बारह `W` की एक पंक्ति लाइन के नीचे बहुत छोटे `12W` के रूप में यात्रा करती है। जब कोई अक्षर केवल एक बार आता है तो उसे गिनने से कुछ हासिल नहीं होता, इसलिए उसे जैसा है वैसा ही अकेले कॉपी कर दिया जाता है।

# --instructions--

एक फ़ंक्शन `encode_run` लिखें जो एक स्ट्रिंग `text` लेता है और उसका रन लंबाई एन्कोडेड रूप लौटाता है।

एक ही अक्षर के दो या दो से अधिक बार दोहराए जाने वाला हर रन उस रन की दशमलव में लिखी गई लंबाई और उसके बाद वह अक्षर बन जाता है। एक की लंबाई वाला रन केवल उस एक अक्षर के रूप में कॉपी होता है, उसके आगे कोई संख्या नहीं लिखी जाती।

उदाहरण:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- टेक्स्ट में केवल `A` से `Z` तक के अपरकेस अक्षर और रिक्त स्थान होते हैं।
- नौ से लंबा कोई रन अपनी पूरी दशमलव गिनती इस्तेमाल करता है, इसलिए बारह `W`, `12W` बन जाते हैं, कभी भी `9W3W` नहीं।
- रिक्त स्थान साधारण अक्षर हैं: उन्हें भी अक्षरों की तरह ही गिना और एन्कोड किया जाता है।
- खाली स्ट्रिंग का एन्कोडिंग खाली स्ट्रिंग ही होता है।

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

खाली स्ट्रिंग का एन्कोडिंग खाली स्ट्रिंग ही होता है

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

एक अकेला अक्षर जैसा है वैसा ही कॉपी हो जाता है

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

बिना दोहराव वाली स्ट्रिंग बिना बदले आगे बढ़ जाती है

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

दो की लंबाई वाला रन गिनती और उसके बाद अक्षर बन जाता है

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

मिश्रित उदाहरण "AABCCCDEEEE", "2AB3CD4E" बन जाता है

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

बारह की लंबाई वाला रन अपनी पूरी दशमलव गिनती इस्तेमाल करता है, इसलिए परिणाम "12W" से शुरू होता है

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

रिक्त स्थानों के रन भी अक्षरों के रनों की तरह ही एन्कोड होते हैं

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

दस की लंबाई वाला रन "10A" लिखा जाता है, कभी भी दो छोटे रनों के रूप में नहीं

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

बारी-बारी से आने वाले अकेले अक्षर सभी जैसे हैं वैसे ही कॉपी होते हैं

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
