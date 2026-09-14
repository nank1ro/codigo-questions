---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Ein Pangramm ist ein Satz, der jeden Buchstaben des englischen Alphabets mindestens einmal verwendet. Das bekannteste Beispiel ist "the quick brown fox jumps over the lazy dog", das alle 26 Buchstaben in neun kurze Wörter unterbringt.

Die Prüfung unterscheidet nicht zwischen Groß- und Kleinschreibung, daher zählen `A` und `a` als derselbe Buchstabe. Ziffern, Satzzeichen und Leerzeichen werden ignoriert: Sie sind keine Buchstaben, aber sie sind auch kein Grund, einen Satz abzulehnen.

# --instructions--

Schreiben Sie eine Funktion `is_pangram`, die einen Satz entgegennimmt und `True` zurückgibt, wenn der Satz ein Pangramm ist, und andernfalls `False`.

Beispiele:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- Ein leerer Satz ist kein Pangramm.
- Nur die 26 Buchstaben von `a` bis `z` zählen.

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

Ein leerer Satz ist kein Pangramm

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

Der klassische Satz "the quick brown fox jumps over the lazy dog" ist ein Pangramm

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

Ein Satz, dem der Buchstabe `x` fehlt, ist kein Pangramm

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

Der Satz "the five boxing wizards jump quickly" ist ein Pangramm

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

Unterstriche werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

Ziffern werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

Ziffern ersetzen nicht die Buchstaben `e`, `i` und `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

Ein Satz in Großbuchstaben ist ebenfalls ein Pangramm

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

Das Mischen der Groß- und Kleinschreibung derselben Hälfte des Alphabets reicht nicht aus

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
