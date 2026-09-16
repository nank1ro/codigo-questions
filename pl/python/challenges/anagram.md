---
language: python
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Dwa słowa są anagramami, gdy jedno jest przestawieniem drugiego: używają dokładnie tych samych liter, a każda z nich występuje tę samą liczbę razy, tylko w innej kolejności. `listen` i `silent` są anagramami, podobnie jak `stone` i `tones`.

Słowo nigdy nie jest anagramem samego siebie. Jeśli oba słowa są dokładnie takie same, nic nie zostało przestawione, więc odpowiedź to `False`. Oba słowa są podane małymi literami i zawierają wyłącznie litery od `a` do `z`.

# --instructions--

Napisz funkcję `is_anagram`, która przyjmuje dwa słowa, `first` i `second`, i zwraca `True`, gdy jedno z nich jest anagramem drugiego, oraz `False` w przeciwnym razie.

Przykłady:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Dwa identyczne słowa nie są anagramami.
- Słowa o różnych długościach nigdy nie są anagramami.
- Każda litera musi występować tyle samo razy w obu słowach.

# --seed--

```python
def is_anagram(first, second):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Słowa "listen" i "silent" są anagramami

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

Słowa "stone" i "tones" są anagramami

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Słowo nie jest anagramem samego siebie

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Słowa o różnych długościach nie są anagramami

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

Te same litery w różnych ilościach nie tworzą anagramu

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

Słowa "anagram" i "nagaram" są anagramami

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Dwa słowa tej samej długości z różnymi literami nie są anagramami

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Dwa puste słowa są identyczne, więc nie są anagramami

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Dwie różne pojedyncze litery nie są anagramami

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

Słowa "evil" i "vile" są anagramami

```python
    def test10(self):
        self.assertEqual(is_anagram("evil", "vile"), True, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_anagram(first, second):
    if first == second:
        return False

    return sorted(first) == sorted(second)
```
