---
language: python
exerciseType: 1
difficulty: 3
title: कोष्ठकों का मिलान
---

# --description--

कोड, गणित या मार्कअप ले जाने वाला टेक्स्ट कोष्ठकों से भरा होता है, और हर खोलने वाले कोष्ठक को उसी किस्म का एक बंद करने वाला कोष्ठक चाहिए। एक स्ट्रिंग तब संतुलित होती है जब उसके कोष्ठक जोड़े बनाते हैं और प्याज की परतों की तरह एक-दूसरे के भीतर नेस्ट होते हैं: `{[()]}` संतुलित है, जबकि `{[(])}` संतुलित नहीं है, क्योंकि गोल जोड़ा उस वर्ग जोड़े से पहले बंद हो जाता है जिसके भीतर वह स्थित है।

यहाँ तीन जोड़े मायने रखते हैं: गोल `()`, वर्ग `[]` और कर्ली `{}`। स्ट्रिंग का बाकी हर कैरेक्टर नज़रअंदाज़ कर दिया जाता है। एक बंद करने वाले कोष्ठक को सबसे हाल में खोले गए उस कोष्ठक को बंद करना चाहिए जो अभी भी खुला है, और जब स्ट्रिंग समाप्त हो जाए तो कोई कोष्ठक खुला नहीं रहना चाहिए।

# --instructions--

एक फ़ंक्शन `is_balanced` लिखें जो एक स्ट्रिंग लेता है और तब `True` लौटाता है जब उसके सभी कोष्ठक मेल खाते हों और ठीक से नेस्ट होते हों, अन्यथा `False`।

उदाहरण:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- खाली स्ट्रिंग संतुलित होती है।
- जो कैरेक्टर कोष्ठक नहीं हैं उन्हें नज़रअंदाज़ कर दिया जाता है।
- एक बंद करने वाला कोष्ठक सबसे हाल में खोले गए उस कोष्ठक से मेल खाना चाहिए जो अभी भी खुला है।
- जब स्ट्रिंग समाप्त हो तब कोई कोष्ठक खुला नहीं रहना चाहिए।

# --seed--

```python
def is_balanced(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

खाली स्ट्रिंग संतुलित होती है

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

गोल कोष्ठकों का एक जोड़ा संतुलित होता है

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

एक-दूसरे के भीतर नेस्ट किए गए तीनों किस्म के जोड़े संतुलित होते हैं

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

दूसरे टेक्स्ट के साथ मिले कोष्ठक भी संतुलित होते हैं

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

बगल में रखे गए जोड़े संतुलित होते हैं

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

बिना किसी कोष्ठक वाली स्ट्रिंग संतुलित होती है

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

क्रॉस हो चुका जोड़ा संतुलित नहीं होता

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

कभी बंद न होने वाला खोलने वाला कोष्ठक संतुलित नहीं होता

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

किसी खोलने वाले कोष्ठक से पहले आया बंद करने वाला कोष्ठक संतुलित नहीं होता

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

स्ट्रिंग में गहराई में क्रॉस हो चुके जोड़े संतुलित नहीं होते

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

अंत में बचा हुआ बंद करने वाला कोष्ठक संतुलित नहीं होता

```python
    def test11(self):
        self.assertEqual(is_balanced("())"), False, "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
```
