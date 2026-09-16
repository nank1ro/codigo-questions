---
language: python
exerciseType: 1
difficulty: 2
title: Chiffre de César
---

# --description--

Jules César protégeait ses lettres privées avec l'une des plus anciennes astuces de la cryptographie : il remplaçait chaque lettre d'un message par la lettre située un nombre fixe de positions plus loin dans l'alphabet. Avec un décalage de 3, `a` devient `d`, `b` devient `e` et `c` devient `f`.

L'alphabet se comporte comme un cercle, ainsi les lettres de la fin reviennent au début : avec un décalage de 3, `x` devient `a`, `y` devient `b` et `z` devient `c`.

Tout ce qui n'est pas une lettre, comme un espace, une virgule, un point d'exclamation ou un chiffre, traverse le chiffrement sans être modifié.

# --instructions--

Écrivez une fonction `caesar_cipher` qui prend un message `text` et un nombre entier `shift`, et retourne le message encodé.

Exemples :
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Le message est toujours en minuscules, vous n'avez donc jamais à gérer de lettres majuscules.
- Les caractères qui ne sont pas des lettres conservent leur place et leur valeur.
- Le décalage n'est jamais négatif. Un décalage de `0` laisse le message inchangé, et il en va de même pour un décalage de `26`.

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

Un décalage de 3 transforme "hello" en "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

La fin de l'alphabet revient au début, ainsi "xyz" devient "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Un décalage de 0 laisse le message inchangé

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Un décalage de 26 correspond à un tour complet de l'alphabet, le message est donc inchangé

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

La ponctuation et les espaces passent sans être modifiés

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Un message vide reste vide

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Les espaces entre les lettres isolées sont conservés

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Les chiffres ne sont pas décalés, même avec un décalage de 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Un décalage de 13 encode une phrase entière

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
