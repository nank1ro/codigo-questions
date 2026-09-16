---
language: python
exerciseType: 1
difficulty: 2
title: Szyfr Cezara
---

# --description--

Juliusz Cezar chronił swoje prywatne listy jedną z najstarszych sztuczek kryptografii: zastępował każdą literę wiadomości literą oddaloną o stałą liczbę pozycji w alfabecie. Przy przesunięciu o 3 `a` staje się `d`, `b` staje się `e`, a `c` staje się `f`.

Alfabet zachowuje się jak okrąg, więc litery z końca zawijają się z powrotem do początku: przy przesunięciu o 3 `x` staje się `a`, `y` staje się `b`, a `z` staje się `c`.

Wszystko, co nie jest literą, na przykład spacja, przecinek, wykrzyknik albo cyfra, przechodzi przez szyfr bez zmian.

# --instructions--

Napisz funkcję `caesar_cipher`, która przyjmuje wiadomość `text` i liczbę całkowitą `shift`, i zwraca zaszyfrowaną wiadomość.

Przykłady:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Wiadomość zawsze składa się z małych liter, więc nie musisz przejmować się wielkimi literami.
- Znaki, które nie są literami, zachowują swoje miejsce i swoją wartość.
- Przesunięcie nigdy nie jest ujemne. Przesunięcie o `0` pozostawia wiadomość bez zmian, podobnie jak przesunięcie o `26`.

# --seed--

```python
def caesar_cipher(text, shift):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Przesunięcie o 3 zamienia "hello" w "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

Koniec alfabetu zawija się do początku, więc "xyz" staje się "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Przesunięcie o 0 pozostawia wiadomość bez zmian

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Przesunięcie o 26 to pełny obrót alfabetu, więc wiadomość pozostaje bez zmian

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

Znaki interpunkcyjne i spacje przechodzą bez zmian

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Pusta wiadomość pozostaje pusta

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Spacje między pojedynczymi literami są zachowane

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Cyfry nie są przesuwane, nawet przy przesunięciu o 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Przesunięcie o 13 szyfruje całe zdanie

```python
    def test9(self):
        self.assertEqual(caesar_cipher("the quick brown fox jumps over the lazy dog", 13), "gur dhvpx oebja sbk whzcf bire gur ynml qbt", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
        else:
            result += char

    return result
```
