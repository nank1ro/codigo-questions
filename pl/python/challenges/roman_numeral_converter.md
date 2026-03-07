---
language: python
exerciseType: 1
difficulty: 3
title: Konwerter liczb rzymskich
---

# --description--

Utwórz funkcję przyjmującą dodatnią liczbę całkowitą jako parametr i zwracającą ciąg znaków zawierający reprezentację tej liczby w systemie rzymskim. Nowoczesne cyfry rzymskie są zapisywane przez wyrażenie każdej cyfry osobno, zaczynając od cyfry znajdującej się najbardziej po lewej i pomijając cyfry o wartości zero.

# --instructions--

Przykłady:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- Wszystkie cyfry rzymskie powinny być zwracane jako wielkie litery.
- Największa liczba, którą można przedstawić w tym zapisie, to 3 999.

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

Liczba `2` musi być równa `II`

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

Liczba `12` musi być równa `XII`

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

Liczba `16` musi być równa `XVI`

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

Liczba `44` musi być równa `XLIV`

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

Liczba `68` musi być równa `LXVIII`

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

Liczba `400` musi być równa `CD`

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

Liczba `798` musi być równa `DCCXCVIII`

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

Liczba `1000` musi być równa `M`

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

Liczba `3999` musi być równa `MMMCMXCIX`

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

Liczba `649` musi być równa `DCXLIX`

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

Liczba `1666` musi być równa `MDCLXVI`

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
