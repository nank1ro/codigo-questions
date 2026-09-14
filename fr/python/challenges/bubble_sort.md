---
language: python
exerciseType: 1
difficulty: 2
title: Tri à bulles
---

# --description--

Le tri à bulles est l'un des algorithmes de tri les plus simples. Il parcourt une liste et compare chaque paire d'éléments adjacents, en les échangeant dès qu'ils sont dans le mauvais ordre. Après chaque passage complet, la plus grande valeur restante a « remonté » jusqu'à sa position finale, et la liste est triée dès qu'un passage se termine sans le moindre échange.

# --instructions--

Écrivez une fonction appelée `bubble_sort` qui prend une liste d'entiers et retourne une **nouvelle** liste avec les mêmes valeurs triées par ordre croissant. La liste passée en paramètre ne doit pas être modifiée.

Vous devez implémenter l'algorithme de tri à bulles vous-même, en comparant et en échangeant les éléments adjacents. N'utilisez pas de fonction de tri de la bibliothèque standard.

Votre fonction doit également fonctionner avec un tableau vide, un tableau d'un seul élément, un tableau déjà trié, des valeurs répétées et des nombres négatifs.

Exemple d'appel de fonction :
```python
print(bubble_sort([3, 1, 2]))
# prints [1, 2, 3]
```

# --seed--

```python
def bubble_sort(arr):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Un tableau vide doit retourner un tableau vide

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Un tableau d'un seul élément doit rester identique

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Un tableau déjà trié doit conserver le même ordre

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Un tableau trié à l'envers doit être mis en ordre croissant

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Toutes les valeurs répétées doivent être conservées

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Les nombres négatifs doivent être triés avant les positifs

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Un tableau mixte plus long doit être trié par ordre croissant

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

Le tableau passé en paramètre ne doit pas être modifié

```python
    def test_8(self):
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2], "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def bubble_sort(arr):
    result = list(arr)
    end = len(result)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True
        end -= 1
    return result
```
