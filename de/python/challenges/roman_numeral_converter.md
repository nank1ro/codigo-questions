---
language: python
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Erstellen Sie eine Funktion, die eine positive Ganzzahl als Parameter nimmt und einen String zurückgibt, der die römische Zahlendarstellung dieser Ganzzahl enthält. Moderne römische Ziffern werden geschrieben, indem jede Ziffer einzeln ausgedrückt wird, angefangen mit der linken Ziffer und überspringe jede Ziffer mit einem Wert von Null.

# --instructions--

Beispiele:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- Alle römischen Ziffern sollten in Großbuchstaben zurückgegeben werden.
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

Die Zahl `2` muss `II` entsprechen

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

Die Zahl `12` muss `XII` entsprechen

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

Die Zahl `16` muss `XVI` entsprechen

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

Die Zahl `44` muss `XLIV` entsprechen

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

Die Zahl `68` muss `LXVIII` entsprechen

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

Die Zahl `400` muss `CD` entsprechen

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

Die Zahl `798` muss `DCCXCVIII` entsprechen

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

Die Zahl `1000` muss `M` entsprechen

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

Die Zahl `3999` muss `MMMCMXCIX` entsprechen

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

Die Zahl `649` muss `DCXLIX` entsprechen

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

Die Zahl `1666` muss `MDCLXVI` entsprechen

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
