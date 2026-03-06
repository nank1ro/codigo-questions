---
language: python
exerciseType: 1
difficulty: 1
title: बारिश की बूंदें
---

# --description--

आपका कार्य एक संख्या को एक स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणकों से संबंधित बारिश की बूंदों की आवाज़ें हों।
एक गुणक वह संख्या है जो किसी अन्य संख्या को समान रूप से विभाजित करती है, बिना किसी शेष के।
यह जांचने का सबसे सरल तरीका कि कोई संख्या किसी अन्य का गुणक है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
बारिश की बूंदों के नियम निम्नलिखित हैं:

- 3 गुणक के रूप में है, तो परिणाम में 'Pling' जोड़ें।
- 5 गुणक के रूप में है, तो परिणाम में 'Plang' जोड़ें।
- 7 गुणक के रूप में है, तो परिणाम में 'Plong' जोड़ें।
- 3, 5, या 7 में से कोई भी गुणक नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 में 7 गुणक है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 में 3 और 5 दोनों गुणक हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34, 3, 5, या 7 से विभाजित नहीं है, इसलिए परिणाम `"34"` होगा।

# --seed--

```python
def convert(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

1 के लिए ध्वनि "1" है

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

3 के लिए ध्वनि "Pling" है

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

5 के लिए ध्वनि "Plang" है

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

7 के लिए ध्वनि "Plong" है

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

6 के लिए ध्वनि "Pling" है

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

8 के लिए ध्वनि "8" है

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

9 के लिए ध्वनि "Pling" है

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

10 के लिए ध्वनि "Plang" है

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

14 के लिए ध्वनि "Plong" है

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

15 के लिए ध्वनि "PlingPlang" है

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

21 के लिए ध्वनि "PlingPlong" है

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

25 के लिए ध्वनि "Plang" है

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

27 के लिए ध्वनि "Pling" है

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

35 के लिए ध्वनि "PlangPlong" है

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

49 के लिए ध्वनि "Plong" है

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

52 के लिए ध्वनि "52" है

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

105 के लिए ध्वनि "PlingPlangPlong" है

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

3125 के लिए ध्वनि "Plang" है

```python
    def test_the_sound_for_3125(self):
        self.assertEqual(convert(3125), "Plang", "--err-t18--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def convert(number):
    result = ''
    if number % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'

    if not result:
        result = str(number)
    return result
```
