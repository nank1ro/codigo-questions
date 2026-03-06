---
language: python
exerciseType: 1
difficulty: 3
title: लीप वर्ष
---

# --description--

एक कैलेंडर वर्ष में ठीक 365.25 दिन होते हैं। लेकिन, अंततः, यह भ्रम पैदा करेगा क्योंकि मनुष्य सामान्यतः 1 की सटीक विभाज्यता से गिनते हैं न कि दशमलव बिंदुओं से। इसलिए, इससे बचने के लिए, यह निर्णय लिया गया कि हर चार साल के चक्र में सभी 0.25 दिनों को जोड़ दिया जाए और उस वर्ष को 366 दिन दिए जाएं (29 फरवरी को एक अधिवर्ष दिवस के रूप में शामिल करते हुए) और इसे __लीप वर्ष__ कहा जाए। चार साल के चक्र में अन्य तीन वर्षों में केवल 365 दिन होंगे और वे __लीप वर्ष नहीं होंगे__।

# --instructions--

इस चुनौती में हम इसे एक नए स्तर पर ले जाएंगे, जहां आपको `datetime` क्लास, __if ब्लॉक__, __if-elif ब्लॉक__ या __कंडीशनल__ (`a if b else c`) और लॉजिकल ऑपरेटर __AND__ (`and`) और __OR__ (`or`) का उपयोग किए बिना यह निर्धारित करना है कि यह लीप वर्ष है या नहीं, __NOT__ (`not`) ऑपरेटर को छोड़कर।

यदि यह लीप वर्ष है तो `True` लौटाएं, अन्यथा `False`।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(leap_year(2000))
// prints true
```

# --seed--

```python
def leap_year(year):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`month`, `day`, `if`, `else`, `elif`, `and`, `or` का उपयोग अनुमत नहीं है।

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

वर्ष `2016` एक लीप वर्ष है।

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

वर्ष `1996` एक लीप वर्ष है।

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

वर्ष `1600` एक लीप वर्ष है।

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

वर्ष `2020` एक लीप वर्ष है।

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

वर्ष `2000` एक लीप वर्ष है।

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

वर्ष `2008` एक लीप वर्ष है।

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

वर्ष `1521` लीप वर्ष नहीं है।

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

वर्ष `1800` लीप वर्ष नहीं है।

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

वर्ष `2007` लीप वर्ष नहीं है।

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

वर्ष `2002` लीप वर्ष है।

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

वर्ष `1979` लीप वर्ष नहीं है।

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

वर्ष `2006` लीप वर्ष नहीं है।

```python
    def test12(self):
        self.assertEqual(leap_year(2006), False, "--err-t12--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def leap_year(year):
    return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0))
```

```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```
