---
language: python
exerciseType: 1
difficulty: 2
title: बाइनरी सर्च
---

# --description--

बाइनरी सर्च खोज की सीमा को बार-बार आधा करके किसी **क्रमबद्ध** कलेक्शन में एक मान ढूंढता है: बीच में स्थित तत्व को देखें, और यदि वही तत्व नहीं है जिसे आप चाहते हैं, तो जब लक्ष्य छोटा हो तो बाएं आधे हिस्से में और जब लक्ष्य बड़ा हो तो दाएं आधे हिस्से में खोज जारी रखें।

चूंकि हर चरण शेष तत्वों में से आधे तत्वों को छोड़ देता है, इसलिए बाइनरी सर्च बहुत बड़े कलेक्शन पर भी कुछ ही तुलनाओं में उत्तर तक पहुंच जाता है, जबकि तत्वों को एक-एक करके जांचने में उतने ही चरण लगते हैं जितने तत्व होते हैं।

# --instructions--

एक फ़ंक्शन `binary_search` लिखें जो आरोही क्रम में क्रमबद्ध पूर्णांकों की एक सूची और एक लक्ष्य पूर्णांक लेता है, और सूची के भीतर लक्ष्य का इंडेक्स लौटाता है, या `-1` लौटाता है जब लक्ष्य मौजूद न हो।

सूची में कभी डुप्लिकेट नहीं होते, इसलिए इंडेक्स हमेशा अद्वितीय होता है। सूची खाली भी हो सकती है। आपके फ़ंक्शन को लीनियर स्कैन नहीं, बल्कि बाइनरी सर्च का उपयोग करना चाहिए, हर चरण में खोज की सीमा को आधा करते हुए।

फ़ंक्शन कॉल का उदाहरण:
```python
print(binary_search([1, 3, 5, 7], 5))
# 2 प्रिंट करता है
```

# --seed--

```python
def binary_search(arr, target):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

खाली सूची में खोज करने पर -1 लौटाना चाहिए।

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

`[5]` में 5 खोजने पर 0 लौटाना चाहिए।

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

`[5]` में 9 खोजने पर -1 लौटाना चाहिए।

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

12 तत्वों वाली सूची का पहला तत्व -9 इंडेक्स 0 पर मिलना चाहिए।

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

12 तत्वों वाली सूची का अंतिम तत्व 78 इंडेक्स 11 पर मिलना चाहिए।

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

तत्व 15 इंडेक्स 6 पर मिलना चाहिए।

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

तत्व 22 इंडेक्स 7 पर मिलना चाहिए।

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

मान 12, जो 11 और 15 के बीच स्थित है, -1 लौटाना चाहिए।

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

हर तत्व से छोटा लक्ष्य -1 लौटाना चाहिए।

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

हर तत्व से बड़ा लक्ष्य -1 लौटाना चाहिए।

```python
    def test10(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
