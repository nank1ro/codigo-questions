---
language: python
exerciseType: 1
difficulty: 1
title: हैमिंग दूरी
---

# --description--

DNA को न्यूक्लियोटाइडों के स्ट्रैंड के रूप में लिखा जाता है, जिनमें से प्रत्येक एक अक्षर होता है: `A`, `C`, `G` या `T`। जब समान लंबाई के दो स्ट्रैंड साथ-साथ पंक्तिबद्ध किए जाते हैं, तो कुछ स्थानों पर एक ही न्यूक्लियोटाइड होता है और कुछ स्थानों पर अलग-अलग।

जिन स्थानों पर दोनों स्ट्रैंड भिन्न होते हैं, उनकी संख्या हैमिंग दूरी कहलाती है, और जीववैज्ञानिक इसका उपयोग यह मापने के लिए करते हैं कि दो स्ट्रैंड कितनी दूर अलग हो गए हैं। `GAGCCTACTAACGGGAT` को `CATCGTAATGACGGCCT` के साथ पंक्तिबद्ध करने पर 7 स्थान भिन्न मिलते हैं, इसलिए उनकी हैमिंग दूरी 7 होती है।

# --instructions--

`hamming_distance` नाम का एक फ़ंक्शन लिखें जो समान लंबाई के दो DNA स्ट्रैंड लेता है और उन स्थानों की संख्या लौटाता है जहाँ वे भिन्न होते हैं।

उदाहरण:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- दोनों स्ट्रैंड हमेशा समान लंबाई के होते हैं, इसलिए आपको कभी अलग-अलग लंबाई वाले स्ट्रैंड संभालने की ज़रूरत नहीं है।
- दो खाली स्ट्रैंड कहीं भिन्न नहीं होते, इसलिए उनकी दूरी 0 होती है।

# --seed--

```python
def hamming_distance(left, right):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

दो खाली स्ट्रैंड कहीं भिन्न नहीं होते

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

दो समान एकल-न्यूक्लियोटाइड स्ट्रैंड में कोई अंतर नहीं होता

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

दो भिन्न एकल-न्यूक्लियोटाइड स्ट्रैंड एक स्थान पर भिन्न होते हैं

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

दो छोटे स्ट्रैंड जो हर स्थान पर भिन्न होते हैं

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

दो छोटे स्ट्रैंड जो केवल पहले स्थान पर भिन्न होते हैं

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

स्ट्रैंडों के बीच में एक भिन्न न्यूक्लियोटाइड

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

अलग-अलग स्थानों पर समान न्यूक्लियोटाइड भी अंतर में गिने जाते हैं

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

चार अंतरों वाले स्ट्रैंडों का एक लंबा जोड़ा

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

एक स्ट्रैंड को एक स्थान खिसकाने पर लगभग हर स्थान भिन्न हो जाता है

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

विवरण वाले दोनों स्ट्रैंड की दूरी सात है

```python
    def test10(self):
        self.assertEqual(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def hamming_distance(left, right):
    distance = 0

    for left_nucleotide, right_nucleotide in zip(left, right):
        if left_nucleotide != right_nucleotide:
            distance += 1

    return distance
```
