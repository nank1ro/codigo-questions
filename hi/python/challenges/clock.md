---
language: python
exerciseType: 1
difficulty: 2
title: घड़ी
---

# --description--

24 घंटे की घड़ी दिन के समय को `HH:MM` के रूप में दिखाती है, जो आधी रात के ठीक बाद `00:00` से शुरू होती है और अगली आधी रात से एक मिनट पहले `23:59` पर समाप्त होती है। दोनों भाग हमेशा दो अंकों में लिखे जाते हैं, इसलिए सुबह ग्यारह बजकर नौ मिनट को `11:09` पढ़ा जाता है।

एक पूरे दिन में 1440 मिनट होते हैं। जैसे ही घड़ी `23:59` से आगे निकलती है, वह `00:00` पर लौट आती है और दिन को फिर से शुरू करती है, और इसे `00:00` से पीछे की ओर घुमाने पर `23:59` पर पहुँचती है।

# --instructions--

एक फ़ंक्शन `clock_time` लिखें जो दो पूर्ण संख्याएं, `hours` और `minutes`, लेता है और 24 घंटे की घड़ी का समय `"HH:MM"` स्ट्रिंग के रूप में लौटाता है, जिसमें दोनों भाग दो अंकों तक पैड किए गए होते हैं।

उदाहरण:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- कोई भी संख्या ऋणात्मक हो सकती है, या किसी असली घड़ी की अनुमति से बड़ी हो सकती है।
- मिनटों की कुल संख्या `hours * 60 + minutes` के रूप में निकालें, फिर उस कुल को `0` से `1439` की सीमा में लपेटें ताकि घड़ी दोनों दिशाओं में घूम जाए।
- `clock_time(24, 0)` ठीक एक पूरा दिन है, इसलिए उसे `"00:00"` पढ़ा जाता है।

# --seed--

```python
def clock_time(hours, minutes):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

सुबह के आठ बजे को `08:00` पढ़ा जाता है

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

एकल अंक दो अंकों तक पैड किए जाते हैं, इसलिए ग्यारह बजकर नौ मिनट को `11:09` पढ़ा जाता है

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

पूरे एक दिन के घंटे `00:00` पर घूम जाते हैं

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

60 से अधिक मिनट घंटों में जुड़ जाते हैं

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

ऋणात्मक घंटा घड़ी को आधी रात से पीछे की ओर घुमा देता है

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

ऋणात्मक मिनट गिनती भी घड़ी को पीछे की ओर घुमा देती है

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

एक पूरे दिन से अधिक पीछे जाने पर भी घड़ी घूमती रहती है

```python
    def test_more_than_a_day_backwards(self):
        self.assertEqual(clock_time(-25, 0), "23:00", "--err-t7--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def clock_time(hours, minutes):
    # पाइथॉन का % हमेशा भाजक का चिह्न लेता है, इसलिए ऋणात्मक कुल संख्या
    # पहले ही आगे की ओर 0..1439 में लपेट जाती है।
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
