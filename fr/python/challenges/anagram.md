---
language: python
exerciseType: 1
difficulty: 2
title: Anagramme
---

# --description--

Deux mots sont des anagrammes lorsque l'un est un réarrangement de l'autre : ils utilisent exactement les mêmes lettres, chacune le même nombre de fois, simplement dans un ordre différent. `listen` et `silent` sont des anagrammes, et il en va de même pour `stone` et `tones`.

Un mot n'est jamais un anagramme de lui-même. Si les deux mots sont exactement identiques, rien n'a été réarrangé, donc la réponse est `False`. Les deux mots sont donnés en minuscules et ne contiennent que les lettres de `a` à `z`.

# --instructions--

Écrivez une fonction `is_anagram` qui prend deux mots, `first` et `second`, et retourne `True` s'ils sont des anagrammes l'un de l'autre et `False` sinon.

Exemples :
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Deux mots identiques ne sont pas des anagrammes.
- Des mots de longueurs différentes ne sont jamais des anagrammes.
- Chaque lettre doit apparaître le même nombre de fois dans les deux mots.

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

Les mots "listen" et "silent" sont des anagrammes

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

Les mots "stone" et "tones" sont des anagrammes

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Un mot n'est pas un anagramme de lui-même

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Des mots de longueurs différentes ne sont pas des anagrammes

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

Les mêmes lettres en quantités différentes ne forment pas un anagramme

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

Les mots "anagram" et "nagaram" sont des anagrammes

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Deux mots de même longueur avec des lettres différentes ne sont pas des anagrammes

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Deux mots vides sont identiques, ils ne sont donc pas des anagrammes

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Deux lettres différentes ne sont pas des anagrammes

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

Les mots "evil" et "vile" sont des anagrammes

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
