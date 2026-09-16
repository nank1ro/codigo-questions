---
language: python
exerciseType: 1
difficulty: 2
title: Anagramma
---

# --description--

Due parole sono anagrammi quando una è un riarrangiamento dell'altra: usano esattamente le stesse lettere, ognuna lo stesso numero di volte, solo in un ordine diverso. `listen` e `silent` sono anagrammi, e lo sono anche `stone` e `tones`.

Una parola non è mai un anagramma di se stessa. Se le due parole sono esattamente uguali, nulla è stato riarrangiato, quindi la risposta è `False`. Entrambe le parole sono fornite in minuscolo e contengono solo le lettere dalla `a` alla `z`.

# --instructions--

Scrivi una funzione `is_anagram` che prende due parole, `first` e `second`, e restituisce `True` quando sono anagrammi l'una dell'altra e `False` altrimenti.

Esempi:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Due parole identiche non sono anagrammi.
- Parole di lunghezza diversa non sono mai anagrammi.
- Ogni lettera deve apparire lo stesso numero di volte in entrambe le parole.

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

Le parole "listen" e "silent" sono anagrammi

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

Le parole "stone" e "tones" sono anagrammi

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Una parola non è un anagramma di se stessa

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Parole di lunghezza diversa non sono anagrammi

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

Le stesse lettere in quantità diverse non sono un anagramma

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

Le parole "anagram" e "nagaram" sono anagrammi

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Due parole della stessa lunghezza con lettere diverse non sono anagrammi

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Due parole vuote sono identiche, quindi non sono anagrammi

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Due lettere singole diverse non sono anagrammi

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

Le parole "evil" e "vile" sono anagrammi

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
