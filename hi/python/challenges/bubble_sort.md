---
language: python
exerciseType: 1
difficulty: 2
title: बबल सॉर्ट
---

# --description--

बबल सॉर्ट सबसे सरल सॉर्टिंग एल्गोरिदम में से एक है। यह एक सूची से गुज़रता है और आसन्न तत्वों के हर जोड़े की तुलना करता है, और जब भी वे गलत क्रम में होते हैं तो उन्हें आपस में बदल देता है। हर पूरे चक्र के बाद सबसे बड़ा शेष मान "बुलबुले" की तरह अपनी अंतिम जगह पर पहुँच जाता है, और जैसे ही कोई चक्र बिना एक भी अदला-बदली के पूरा होता है, सूची क्रमबद्ध हो जाती है।

# --instructions--

`bubble_sort` नाम का एक फ़ंक्शन लिखें जो पूर्णांकों की एक सूची लेता है और उन्हीं मानों के साथ एक **नई** सूची आरोही क्रम में क्रमबद्ध करके लौटाता है। पास की गई सूची में बदलाव नहीं होना चाहिए।

आपको बबल सॉर्ट एल्गोरिदम स्वयं लागू करना होगा, आसन्न तत्वों की तुलना करके और उन्हें आपस में बदलकर। मानक लाइब्रेरी के किसी सॉर्टिंग फ़ंक्शन का उपयोग न करें।

आपका फ़ंक्शन एक खाली सरणी, एक ही तत्व वाली सरणी, पहले से क्रमबद्ध सरणी, दोहराए गए मानों और ऋणात्मक संख्याओं के साथ भी काम करना चाहिए।

फ़ंक्शन कॉल का उदाहरण:
```python
print(bubble_sort([3, 1, 2]))
# [1, 2, 3] प्रिंट करता है
```

# --seed--

```python
def bubble_sort(arr):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

एक खाली सरणी को एक खाली सरणी लौटानी चाहिए

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

एक ही तत्व वाली सरणी वैसी ही रहनी चाहिए

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

पहले से क्रमबद्ध सरणी उसी क्रम में रहनी चाहिए

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

उल्टे क्रम में क्रमबद्ध सरणी को आरोही क्रम में बदलना चाहिए

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

दोहराए गए सभी मान बने रहने चाहिए

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

ऋणात्मक संख्याओं को धनात्मक संख्याओं से पहले क्रमबद्ध होना चाहिए

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

एक लंबी मिश्रित सरणी आरोही क्रम में क्रमबद्ध होनी चाहिए

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

पास की गई सरणी में बदलाव नहीं होना चाहिए

```python
    def test_8(self):
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2], "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def bubble_sort(arr):
    result = list(arr)
    end = len(result)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True
        end -= 1
    return result
```
