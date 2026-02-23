---
language: python
exerciseType: 1
title: Roman Numeral Converter
difficulty: 3
---

# --description--

Erstellen Sie eine Funktion, die eine positive Ganzzahl als Parameter entgegennimmt und einen String zurückgibt, der die römische Zifferndarstellung dieser Ganzzahl enthält. Moderne römische Ziffern werden geschrieben, indem jede Ziffer separat ausgedrückt wird, beginnend mit der linken Ziffer und überspringt jede Ziffer mit dem Wert Null.

# --instructions--

Beispiele:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- Alle römischen Ziffern sollten als Großbuchstaben zurückgegeben werden.
- Die größte Zahl, die in dieser Notation dargestellt werden kann, ist 3.999.

# --seed--

```python
def convert_to_roman(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Die Zahl `2` muss gleich `II` sein

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

Die Zahl `12` muss gleich `XII` sein

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

Die Zahl `16` muss gleich `XVI` sein

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

Die Zahl `44` muss gleich `XLIV` sein

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

Die Zahl `68` muss gleich `LXVIII` sein

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

Die Zahl `400` muss gleich `CD` sein

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

Die Zahl `798` muss gleich `DCCXCVIII` sein

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

Die Zahl `1000` muss gleich `M` sein

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

Die Zahl `3999` muss gleich `MMMCMXCIX` sein

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

Die Zahl `649` muss gleich `DCXLIX` sein

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

Die Zahl `1666` muss gleich `MDCLXVI` sein

```python
    def test11(self):
        self.assertEqual(convert_to_roman(1666), "MDCLXVI", "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def convert_to_roman(n):
    result = ""

    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    for value, letter in values:
        while n >= value:
            result += letter
            n -= value

    return result
```
