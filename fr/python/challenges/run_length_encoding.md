---
language: python
exerciseType: 1
difficulty: 2
title: Codage par plages
---

# --description--

Le codage par plages est l'une des plus vieilles astuces de compression qui existent : au lieu d'écrire le même caractère encore et encore, on écrit combien de fois il se répète, puis le caractère lui-même.

Un télécopieur qui scanne une page quasiment vide rencontre de longues plages de pixels identiques : une rangée de douze `W` parcourt ainsi la ligne sous la forme bien plus courte `12W`. Quand un caractère n'apparaît qu'une seule fois, le compter n'apporte rien, si bien qu'il est copié tel quel.

# --instructions--

Écrivez une fonction `encode_run` qui prend une chaîne `text` et retourne sa forme encodée par plages.

Chaque plage du même caractère répété au moins deux fois devient la longueur de cette plage écrite en décimal, suivie de ce caractère. Une plage de longueur un est copiée comme le seul caractère, sans nombre devant lui.

Exemples :
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Le texte ne contient que des lettres majuscules de `A` à `Z` et des espaces.
- Une plage de plus de neuf caractères utilise son comptage décimal complet : douze `W` deviennent donc `12W` et jamais `9W3W`.
- Les espaces sont des caractères ordinaires : elles sont comptées et encodées exactement comme les lettres.
- La chaîne vide s'encode en chaîne vide.

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

La chaîne vide s'encode en chaîne vide

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Un caractère seul est copié tel quel

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Une chaîne sans répétitions passe inchangée

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Une plage de deux devient le comptage suivi du caractère

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

L'exemple mixte "AABCCCDEEEE" devient "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Une plage de douze utilise son comptage décimal complet, donc le résultat commence par "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Les plages d'espaces sont encodées exactement comme les plages de lettres

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Une plage de dix s'écrit "10A", jamais comme deux plages plus courtes

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Les caractères isolés qui alternent sont tous copiés tels quels

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
