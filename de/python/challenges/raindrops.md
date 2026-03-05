---
language: python
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Ihre Aufgabe ist es, eine Zahl in einen String umzuwandeln, der Regentropfengeräusche enthält, die bestimmten potenziellen Faktoren entsprechen.
Ein Faktor ist eine Zahl, die eine andere Zahl gleichmäßig teilt, ohne einen Rest zu hinterlassen.
Die einfachste Möglichkeit, zu testen, ob eine Zahl ein Faktor einer anderen ist, besteht in der Verwendung der Modulo-Operation.
Die Regeln der Regentropfen sind folgende:

- hat 3 als Faktor, füge 'Pling' zum Ergebnis hinzu.
- hat 5 als Faktor, füge 'Plang' zum Ergebnis hinzu.
- hat 7 als Faktor, füge 'Plong' zum Ergebnis hinzu.
- hat 3, 5 oder 7 nicht als Faktor, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die den richtigen String zurückgibt, Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, daher wäre das Ergebnis `"Plong"`.
- 30 hat sowohl 3 als auch 5 als Faktoren, aber nicht 7, daher wäre das Ergebnis `"PlingPlang"`.
- 34 wird nicht durch 3, 5 oder 7 teilt, daher wäre das Ergebnis `"34"`.

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

Der Klang für 1 ist "1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

Der Klang für 3 ist "Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

Der Klang für 5 ist "Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

Der Klang für 7 ist "Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

Der Klang für 6 ist "Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

Der Klang für 8 ist "8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

Der Klang für 9 ist "Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

Der Klang für 10 ist "Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

Der Klang für 14 ist "Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

Der Klang für 15 ist "PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

Der Klang für 21 ist "PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

Der Klang für 25 ist "Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

Der Klang für 27 ist "Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

Der Klang für 35 ist "PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

Der Klang für 49 ist "Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

Der Klang für 52 ist "52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

Der Klang für 105 ist "PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

Der Klang für 3125 ist "Plang"

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
