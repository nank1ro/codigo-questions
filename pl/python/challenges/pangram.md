---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Pangram to zdanie, w którym każda litera angielskiego alfabetu występuje co najmniej raz. Najbardziej znanym przykładem jest "the quick brown fox jumps over the lazy dog", które mieści wszystkie 26 liter w dziewięciu krótkich słowach.

Sprawdzenie nie rozróżnia wielkości liter, więc `A` i `a` liczą się jako ta sama litera. Cyfry, znaki interpunkcyjne i spacje są ignorowane: nie są literami, ale nie są też powodem do odrzucenia zdania.

# --instructions--

Napisz funkcję `is_pangram`, która przyjmuje zdanie i zwraca `True`, jeśli zdanie jest pangramem, a `False` w przeciwnym razie.

Przykłady:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- Puste zdanie nie jest pangramem.
- Liczy się tylko 26 liter od `a` do `z`.

# --seed--

```python
def is_pangram(sentence):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Puste zdanie nie jest pangramem

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

Klasyczne zdanie "the quick brown fox jumps over the lazy dog" jest pangramem

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

Zdanie, w którym brakuje litery `x`, nie jest pangramem

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

Zdanie "the five boxing wizards jump quickly" jest pangramem

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

Podkreślenia są ignorowane, więc zdanie nadal jest pangramem

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

Cyfry są ignorowane, więc zdanie nadal jest pangramem

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

Cyfry nie zastępują liter `e`, `i` oraz `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

Zdanie zapisane wielkimi literami też jest pangramem

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

Mieszanie wielkości liter w tej samej połowie alfabetu nie wystarczy

```python
    def test9(self):
        self.assertEqual(is_pangram("abcdefghijklm ABCDEFGHIJKLM"), False, "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if "a" <= char <= "z":
            letters.add(char)

    return len(letters) == 26
```
