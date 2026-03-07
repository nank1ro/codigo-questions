---
language: python
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Twoim zadaniem jest zamiana liczby na ciąg znaków zawierający dźwięki kropel deszczu odpowiadające określonym potencjalnym czynnikom.
Czynnik to liczba, która dzieli inną liczbę bez reszty.
Najprostszym sposobem sprawdzenia, czy liczba jest czynnikiem innej, jest użycie operacji modulo.
Zasady Raindrops są następujące:

- jeśli 3 jest czynnikiem, dodaj 'Pling' do wyniku.
- jeśli 5 jest czynnikiem, dodaj 'Plang' do wyniku.
- jeśli 7 jest czynnikiem, dodaj 'Plong' do wyniku.
- jeśli żadna z liczb 3, 5 ani 7 nie jest czynnikiem, wynikiem powinny być cyfry tej liczby.

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

- 28 ma 7 jako czynnik, ale nie 3 ani 5, więc wynikiem byłoby `"Plong"`.
- 30 ma zarówno 3, jak i 5 jako czynniki, ale nie 7, więc wynikiem byłoby `"PlingPlang"`.
- 34 nie jest podzielne przez 3, 5 ani 7, więc wynikiem byłoby `"34"`.

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

Dźwięk dla 1 to "1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

Dźwięk dla 3 to "Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

Dźwięk dla 5 to "Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

Dźwięk dla 7 to "Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

Dźwięk dla 6 to "Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

Dźwięk dla 8 to "8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

Dźwięk dla 9 to "Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

Dźwięk dla 10 to "Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

Dźwięk dla 14 to "Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

Dźwięk dla 15 to "PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

Dźwięk dla 21 to "PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

Dźwięk dla 25 to "Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

Dźwięk dla 27 to "Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

Dźwięk dla 35 to "PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

Dźwięk dla 49 to "Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

Dźwięk dla 52 to "52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

Dźwięk dla 105 to "PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

Dźwięk dla 3125 to "Plang"

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
