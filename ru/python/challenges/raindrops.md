---
language: python
exerciseType: 1
difficulty: 1
title: Капли дождя
---

# --description--

Ваша задача — преобразовать число в строку, содержащую звуки капель дождя, соответствующие определённым потенциальным делителям.
Делитель — это число, которое делит другое число нацело, без остатка.
Самый простой способ проверить, является ли число делителем другого — использовать операцию взятия остатка от деления.
Правила для капель дождя следующие:

- если 3 является делителем, добавить 'Pling' к результату.
- если 5 является делителем, добавить 'Plang' к результату.
- если 7 является делителем, добавить 'Plong' к результату.
- если ни 3, ни 5, ни 7 не являются делителями, результатом должны быть цифры самого числа.

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

- 28 делится на 7, но не на 3 или 5, поэтому результат будет `"Plong"`.
- 30 делится и на 3, и на 5, но не на 7, поэтому результат будет `"PlingPlang"`.
- 34 не делится ни на 3, ни на 5, ни на 7, поэтому результат будет `"34"`.

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

Звук для 1 — "1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

Звук для 3 — "Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

Звук для 5 — "Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

Звук для 7 — "Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

Звук для 6 — "Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

Звук для 8 — "8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

Звук для 9 — "Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

Звук для 10 — "Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

Звук для 14 — "Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

Звук для 15 — "PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

Звук для 21 — "PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

Звук для 25 — "Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

Звук для 27 — "Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

Звук для 35 — "PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

Звук для 49 — "Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

Звук для 52 — "52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

Звук для 105 — "PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

Звук для 3125 — "Plang"

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
