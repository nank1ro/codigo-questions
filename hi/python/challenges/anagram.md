---
language: python
exerciseType: 1
difficulty: 2
title: अनाग्राम
---

# --description--

दो शब्द अनाग्राम होते हैं जब एक दूसरे के अक्षरों की पुनर्व्यवस्था हो: वे बिल्कुल वही अक्षर उपयोग करते हैं, प्रत्येक अक्षर उतनी ही बार, बस अलग क्रम में। `listen` और `silent` अनाग्राम हैं, और वैसे ही `stone` और `tones` भी।

कोई शब्द कभी अपने आप का अनाग्राम नहीं होता। यदि दोनों शब्द बिल्कुल समान हैं, तो कुछ भी पुनर्व्यवस्थित नहीं हुआ, इसलिए उत्तर `False` है। दोनों शब्द छोटे अक्षरों में दिए जाते हैं और उनमें केवल `a` से `z` तक के अक्षर होते हैं।

# --instructions--

एक फ़ंक्शन `is_anagram` लिखें जो दो शब्द, `first` और `second`, लेता है और यदि वे एक-दूसरे के अनाग्राम हैं तो `True` लौटाता है, अन्यथा `False` लौटाता है।

उदाहरण:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- दो समान शब्द अनाग्राम नहीं होते।
- अलग-अलग लंबाई के शब्द कभी अनाग्राम नहीं होते।
- प्रत्येक अक्षर दोनों शब्दों में उतनी ही बार आना चाहिए।

# --seed--

```python
def is_anagram(first, second):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

शब्द "listen" और "silent" अनाग्राम हैं

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

शब्द "stone" और "tones" अनाग्राम हैं

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

कोई शब्द अपने आप का अनाग्राम नहीं होता

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

अलग-अलग लंबाई के शब्द अनाग्राम नहीं होते

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

समान अक्षरों की अलग-अलग मात्रा अनाग्राम नहीं होती

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

शब्द "anagram" और "nagaram" अनाग्राम हैं

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

समान लंबाई वाले दो शब्द जिनके अक्षर अलग हैं, अनाग्राम नहीं होते

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

दो खाली शब्द समान होते हैं, इसलिए वे अनाग्राम नहीं होते

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

दो अलग एकल अक्षर अनाग्राम नहीं होते

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

शब्द "evil" और "vile" अनाग्राम हैं

```python
    def test10(self):
        self.assertEqual(is_anagram("evil", "vile"), True, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_anagram(first, second):
    if first == second:
        return False

    return sorted(first) == sorted(second)
```
