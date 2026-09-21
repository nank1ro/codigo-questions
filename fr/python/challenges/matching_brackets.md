---
language: python
exerciseType: 1
difficulty: 3
title: Crochets correspondants
---

# --description--

Le texte qui contient du code, des maths ou du balisage regorge de crochets, et chaque crochet ouvrant a besoin d'un crochet fermant de même type. Une chaîne est équilibrée lorsque ses crochets s'apparient et s'imbriquent comme les couches d'un oignon : `{[()]}` est équilibrée, alors que `{[(])}` ne l'est pas, car la paire ronde est fermée avant la paire carrée dans laquelle elle se trouve.

Trois paires comptent ici : les rondes `()`, les carrées `[]` et les accolades `{}`. Tous les autres caractères de la chaîne sont ignorés. Un crochet fermant doit fermer le crochet le plus récemment ouvert encore ouvert, et lorsque la chaîne se termine, aucun crochet ne doit rester ouvert.

# --instructions--

Écrivez une fonction `is_balanced` qui prend une chaîne et retourne `True` lorsque tous les crochets qu'elle contient sont appariés et correctement imbriqués, et `False` sinon.

Exemples :
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Une chaîne vide est équilibrée.
- Les caractères qui ne sont pas des crochets sont ignorés.
- Un crochet fermant doit correspondre au crochet le plus récemment ouvert encore ouvert.
- Aucun crochet ne doit rester ouvert lorsque la chaîne se termine.

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

Une chaîne vide est équilibrée

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Une seule paire de crochets ronds est équilibrée

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

Les trois types de paires imbriquées l'une dans l'autre sont équilibrées

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Des crochets mélangés à d'autres textes restent équilibrés

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Des paires placées côte à côte sont équilibrées

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Une chaîne sans aucun crochet est équilibrée

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Une paire croisée n'est pas équilibrée

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Un crochet ouvrant jamais fermé n'est pas équilibré

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Un crochet fermant avant tout crochet ouvrant n'est pas équilibré

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Des paires croisées plus profondément dans la chaîne ne sont pas équilibrées

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Un crochet fermant restant à la fin n'est pas équilibré

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
