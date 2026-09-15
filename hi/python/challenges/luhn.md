---
language: python
exerciseType: 1
difficulty: 2
title: लूह्न चेकसम
---

# --description--

लूह्न एल्गोरिदम एक सरल चेकसम है जिसका उपयोग क्रेडिट कार्ड नंबरों जैसी पहचान संख्याओं को मान्य करने के लिए किया जाता है।

किसी संख्या की जांच करने से पहले, स्ट्रिंग से हर स्पेस हटा दें। स्ट्रिंग तभी मान्य है जब शेष बचा हिस्सा एक कैरेक्टर से लंबा हो और मूल स्ट्रिंग में अंकों और स्पेस के अलावा कुछ और न हो।

जांच करने के लिए, सबसे दाईं ओर के अंक से शुरू करें और बाईं ओर बढ़ते हुए हर दूसरे अंक को दोगुना करें। जब दोगुना करने पर 9 से बड़ी संख्या बनती है, तो उसमें से 9 घटा दें। फिर सभी अंकों का योग करें: संख्या तभी मान्य होती है जब योग 10 से विभाज्य हो।

उदाहरण के लिए, `"059"` देता है `0`, फिर `5` का दोगुना `10` होता है जो `1` बन जाता है, फिर `9`। उनका योग `10` है, जो 10 से विभाज्य है, इसलिए संख्या मान्य है।

# --instructions--

एक फ़ंक्शन `is_valid` लिखें जो एक स्ट्रिंग लेता है और संख्या मान्य होने पर `True` लौटाता है, अन्यथा `False`।

- `"4539 3195 0343 6467"` चेकसम पास करता है, इसलिए परिणाम `True` है।
- `"8273 1232 7352 0569"` चेकसम में विफल होता है, इसलिए परिणाम `False` है।
- `"0"` केवल एक कैरेक्टर लंबा है, इसलिए परिणाम `False` है।
- `"055-444-285"` में ऐसा कैरेक्टर है जो अंक या स्पेस नहीं है, इसलिए परिणाम `False` है।

फ़ंक्शन कॉल का उदाहरण:
```python
print(is_valid("095 245 88"))
# True प्रिंट करता है
```

# --seed--

```python
def is_valid(value):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

एक अकेला अंक मान्य नहीं है।

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

शुरुआत में स्पेस के साथ एक अकेला अंक मान्य नहीं है।

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

संख्या `"059"` मान्य है।

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

संख्या `"59"` मान्य है।

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

संख्या `"055 444 285"` मान्य है।

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

संख्या `"055 444 286"` मान्य नहीं है।

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

संख्या `"8273 1232 7352 0569"` मान्य नहीं है।

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

संख्या `"4539 3195 0343 6467"` मान्य है।

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

संख्या `"1 2345 6789 1234 5678 9012"` मान्य नहीं है।

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

संख्या `"095 245 88"` मान्य है।

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

एक अक्षर संख्या को अमान्य बना देता है।

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

डैश संख्या को अमान्य बना देते हैं।

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

एक विराम चिह्न कैरेक्टर संख्या को अमान्य बना देता है।

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

प्रतीक संख्या को अमान्य बना देते हैं।

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

खाली स्ट्रिंग मान्य नहीं है।

```python
    def test_an_empty_string_is_not_valid(self):
        self.assertEqual(is_valid(""), False, "--err-t15--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_valid(value):
    total = 0
    count = 0
    for char in reversed(value):
        if char == ' ':
            continue
        if char < '0' or char > '9':
            return False
        digit = int(char)
        if count % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        count += 1
    return count > 1 and total % 10 == 0
```
