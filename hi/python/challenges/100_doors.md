---
language: python
exerciseType: 1
title: 100 दरवाज़े
difficulty: 1
---

# --description--

एक पंक्ति में 100 दरवाज़े हैं जो सभी शुरू में बंद हैं।
आप दरवाज़ों से 100 बार गुज़रते हैं।
पहली बार, हर दरवाज़े पर जाएं और दरवाज़े को 'टॉगल' करें (यदि दरवाज़ा बंद है, तो खोलें; यदि खुला है, तो बंद करें)।
दूसरी बार, केवल हर दूसरे दरवाज़े पर जाएं (यानी, दरवाज़ा #2, #4, #6, ...) और उसे टॉगल करें।
तीसरी बार, हर तीसरे दरवाज़े पर जाएं (यानी, दरवाज़ा #3, #6, #9, ...), आदि, जब तक कि आप केवल 100वें दरवाज़े पर न जाएं।

# --instructions--

अंतिम पास के बाद दरवाज़ों की स्थिति निर्धारित करने के लिए एक फ़ंक्शन लागू करें।
अंतिम परिणाम को एक ऐरे में लौटाएं, जिसमें केवल वही दरवाज़ा नंबर शामिल हो जो खुला हो।
> विधि को दरवाज़ों की परिवर्तनीय संख्या के साथ काम करने में सक्षम होना चाहिए।

# --seed--

```python
def get_final_opened_doors(num_doors):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

100 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

10 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

950 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```python
    def test_3(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        self.assertEqual(get_final_opened_doors(950), solution, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def get_final_opened_doors(num_doors):
    open_doors = []
    i = 1;
    while (i**2) <= num_doors:
        open_doors.append(i**2)
        i += 1
    return open_doors
```
