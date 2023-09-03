---
language: python
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In a calendar year there are exactly 365.25 days. But, eventually, this will lead to confusion because humans normally count by exact divisibility of 1 and not with decimal points. So, to avoid the latter, it was decided to add up all 0.25 days every four-year cycle and give that year 366 days (including February 29 as an intercalary day) and call it a __leap year__. The other three years in the four-year cycle would only contain 365 days and __wouldn't be leap years__.

# --instructions--

In this challenge we'll take it to a new level, where you are to determine if it's a leap year or not without the use of the `datetime` class, __if blocks__, __if-elif blocks__ or __conditionals__ (`a if b else c`) nor the logical operators __AND__ (`and`) and __OR__ (`or`) with the exemption of the __NOT__ (`not`) operator.

Return `True` if it's a leap year, `False` otherwise.

Example of function call:
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

The use of `month`, `day`, `if`, `else`, `elif`, `and`, `or` is not allowed.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

The year `1996` is a leap year.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

The year `1600` is a leap year.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

The year `2020` is a leap year.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

The year `2000` is a leap year.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

The year `2008` is a leap year.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

The year `1521` is not a leap year.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

The year `1800` is not a leap year.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

The year `2007` is not a leap year.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

The year `2002` is a leap year.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

The year `1979` is not a leap year.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

The year `2006` is not a leap year.

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
    return (year % 4 == 0) ^ ((year % 100 == 0) and (year % 400 != 0))
```

```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```
