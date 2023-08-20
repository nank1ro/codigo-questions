---
language: python
exerciseType: 1
difficulty: 3
title: Convertitore numerico romano
---

# --description--

Crea una funzione che prenda come parametro un numero intero positivo e restituisca una stringa contenente la rappresentazione in numeri romani di quel numero intero. I numeri romani moderni sono scritti esprimendo ogni cifra separatamente, partendo dalla cifra più a sinistra e saltando qualsiasi cifra con valore zero.

# --instructions--

Esempi:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- Tutti i numeri romani devono essere riportati in maiuscolo.
- Il numero più grande che può essere rappresentato con questa notazione è 3.999.

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

Il numero `2` deve essere uguale a `II` 

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

Il numero `12` deve essere uguale a `XII`

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

Il numero `16` deve essere uguale a `XVI`

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

Il numero `44` deve essere uguale a `XLIV`

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

Il numero `68` deve essere uguale a `LXVIII`

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

Il numero `400` deve essere uguale a `CD`

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

Il numero `798` deve essere uguale a `DCCXCVIII`

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

Il numero `1000` deve essere uguale a `M`

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

Il numero `3999` deve essere uguale a `MMMCMXCIX`

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

Il numero `649` deve essere uguale a `DCXLIX`

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

Il numero `1666` deve essere uguale a `MDCLXVI`

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
