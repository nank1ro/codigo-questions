---
language: python
exerciseType: 1
difficulty: 2
title: Kodowanie RLE
---

# --description--

Kodowanie RLE (run-length encoding) to jedna z najstarszych sztuczek kompresji: zamiast zapisywać ten sam znak w kółko, zapisujesz, ile razy się powtarza, a następnie sam znak.

Faks skanujący w większości pustą stronę napotyka długie ciągi identycznych pikseli, więc rząd dwunastu `W` wędruje przez linię jako znacznie krótsze `12W`. Gdy jakiś znak pojawia się tylko raz, liczenie go niczego nie daje, więc jest on kopiowany samodzielnie.

# --instructions--

Napisz funkcję `encode_run`, która przyjmuje ciąg znaków `text` i zwraca jego postać zakodowaną metodą RLE.

Każda seria tego samego znaku powtórzonego dwa lub więcej razy staje się długością serii zapisaną dziesiętnie, po której następuje ten znak. Seria o długości jeden jest kopiowana jako pojedynczy znak, bez liczby przed nim.

Przykłady:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Tekst zawiera wyłącznie wielkie litery od `A` do `Z` oraz spacje.
- Seria dłuższa niż dziewięć znaków używa pełnej liczby dziesiętnej, więc dwanaście `W` daje `12W`, a nigdy `9W3W`.
- Spacje to zwykłe znaki: są liczone i kodowane dokładnie tak samo jak litery.
- Pusty ciąg znaków koduje się do pustego ciągu znaków.

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Pusty ciąg znaków koduje się do pustego ciągu znaków

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Pojedynczy znak jest kopiowany jako sam siebie

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Ciąg znaków bez powtórzeń przechodzi bez zmian

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Seria o długości dwa staje się liczbą, po której następuje znak

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

Mieszany przykład "AABCCCDEEEE" staje się "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Seria dwunastu znaków używa pełnej liczby dziesiętnej, więc wynik zaczyna się od "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Serie spacji są kodowane dokładnie tak samo jak serie liter

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Seria dziesięciu znaków jest zapisywana jako "10A", a nigdy jako dwie krótsze serie

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Naprzemiennie występujące pojedyncze znaki są wszystkie kopiowane jako sam siebie

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
