---
language: python
exerciseType: 1
difficulty: 1
title: पैनग्राम
---

# --description--

पैनग्राम एक ऐसा वाक्य है जो अंग्रेजी वर्णमाला के हर अक्षर का कम से कम एक बार उपयोग करता है। सबसे प्रसिद्ध उदाहरण "the quick brown fox jumps over the lazy dog" है, जो सभी 26 अक्षरों को नौ छोटे शब्दों में समा लेता है।

यह जाँच अक्षरों के बड़े या छोटे होने का अंतर नहीं करती, इसलिए `A` और `a` एक ही अक्षर गिने जाते हैं। अंक, विराम चिह्न और रिक्त स्थान अनदेखे किए जाते हैं: वे अक्षर नहीं हैं, लेकिन वे किसी वाक्य को अस्वीकार करने का कारण भी नहीं हैं।

# --instructions--

एक फ़ंक्शन `is_pangram` लिखें जो एक वाक्य लेता है और यदि वाक्य पैनग्राम है तो `True` लौटाता है, अन्यथा `False` लौटाता है।

उदाहरण:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- खाली वाक्य पैनग्राम नहीं है।
- केवल `a` से `z` तक के 26 अक्षर गिने जाते हैं।

# --seed--

```python
def is_pangram(sentence):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

खाली वाक्य पैनग्राम नहीं है

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

क्लासिक वाक्य "the quick brown fox jumps over the lazy dog" एक पैनग्राम है

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

जिस वाक्य में अक्षर `x` नहीं है वह पैनग्राम नहीं है

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

वाक्य "the five boxing wizards jump quickly" एक पैनग्राम है

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

अंडरस्कोर अनदेखे किए जाते हैं, इसलिए वाक्य फिर भी पैनग्राम है

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

अंक अनदेखे किए जाते हैं, इसलिए वाक्य फिर भी पैनग्राम है

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

अंक अक्षरों `e`, `i` और `t` की जगह नहीं लेते

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

बड़े अक्षरों में लिखा वाक्य भी पैनग्राम है

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

वर्णमाला के एक ही आधे हिस्से के बड़े और छोटे अक्षर मिलाना पर्याप्त नहीं है

```python
    def test9(self):
        self.assertEqual(is_pangram("abcdefghijklm ABCDEFGHIJKLM"), False, "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if "a" <= char <= "z":
            letters.add(char)

    return len(letters) == 26
```
