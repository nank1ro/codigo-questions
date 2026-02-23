---
language: python
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Create a function taking a positive integer as its parameter and returning a string containing the Roman numeral representation of that integer. Modern Roman numerals are written by expressing each digit separately, starting with the left most digit and skipping any digit with a value of zero.

# --instructions--

Examples:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- All roman numerals should be returned as uppercase.
- The largest number that can be represented in this notation is 3,999.

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

The number `2` must equal `II` 

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

The number `12` must equal `XII`

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

The number `16` must equal `XVI`

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

The number `44` must equal `XLIV`

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

The number `68` must equal `LXVIII`

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

The number `400` must equal `CD`

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

The number `798` must equal `DCCXCVIII`

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

The number `1000` must equal `M`

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

The number `3999` must equal `MMMCMXCIX`

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

The number `649` must equal `DCXLIX`

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

The number `1666` must equal `MDCLXVI`

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
