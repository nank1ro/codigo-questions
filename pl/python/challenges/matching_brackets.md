---
language: python
exerciseType: 1
difficulty: 3
title: Pasujące nawiasy
---

# --description--

Tekst zawierający kod, zapis matematyczny czy znaczniki jest pełen nawiasów, a każdy nawias otwierający potrzebuje nawiasu zamykającego tego samego rodzaju. Ciąg znaków jest zrównoważony, gdy jego nawiasy tworzą pary i zagnieżdżają się jak warstwy cebuli: `{[()]}` jest zrównoważony, natomiast `{[(])}` już nie, ponieważ para okrągła zostaje zamknięta przed parą kwadratową, wewnątrz której się znajduje.

Liczą się tutaj trzy pary: okrągła `()`, kwadratowa `[]` i klamrowa `{}`. Każdy inny znak w ciągu jest ignorowany. Nawias zamykający musi zamykać ostatnio otwarty nawias, który wciąż jest otwarty, a gdy ciąg się kończy, żaden nawias nie może pozostać otwarty.

# --instructions--

Napisz funkcję `is_balanced`, która przyjmuje ciąg znaków i zwraca `True`, gdy wszystkie zawarte w niej nawiasy są sparowane i poprawnie zagnieżdżone, a w przeciwnym razie zwraca `False`.

Przykłady:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Pusty ciąg znaków jest zrównoważony.
- Znaki, które nie są nawiasami, są ignorowane.
- Nawias zamykający musi pasować do ostatnio otwartego nawiasu, który wciąż jest otwarty.
- Żaden nawias nie może pozostać otwarty, gdy ciąg znaków się kończy.

# --seed--

```python
def is_balanced(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Pusty ciąg znaków jest zrównoważony

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Pojedyncza para nawiasów okrągłych jest zrównoważona

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

Trzy rodzaje par zagnieżdżone jeden w drugim są zrównoważone

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Nawiasy przeplatane innym tekstem nadal są zrównoważone

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Pary ustawione obok siebie są zrównoważone

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Ciąg znaków bez żadnych nawiasów jest zrównoważony

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Skrzyżowana para nawiasów nie jest zrównoważona

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Nawias otwierający, który nigdy nie zostaje zamknięty, nie jest zrównoważony

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Nawias zamykający pojawiający się przed jakimkolwiek nawiasem otwierającym nie jest zrównoważony

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Skrzyżowane pary głębiej w ciągu znaków nie są zrównoważone

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Nawias zamykający pozostawiony na końcu nie jest zrównoważony

```python
    def test11(self):
        self.assertEqual(is_balanced("())"), False, "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
```
