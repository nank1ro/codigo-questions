---
language: python
exerciseType: 1
difficulty: 2
title: Recherche binaire
---

# --description--

La recherche binaire trouve une valeur dans une collection **triée** en divisant à plusieurs reprises la plage de recherche par deux : regarde l'élément du milieu et, si ce n'est pas celui que tu cherches, continue dans la moitié gauche lorsque la valeur cherchée est plus petite ou dans la moitié droite lorsqu'elle est plus grande.

Comme chaque étape écarte la moitié des éléments restants, la recherche binaire atteint la réponse en quelques comparaisons même sur de très grandes collections, alors que vérifier les éléments un par un coûterait autant d'étapes qu'il y a d'éléments.

# --instructions--

Écris une fonction `binary_search` qui prend une liste d'entiers triée par ordre croissant et un entier cherché, et renvoie l'index de la valeur cherchée dans la liste, ou `-1` lorsque la valeur n'est pas présente.

La liste ne contient jamais de doublons, l'index est donc toujours unique. La liste peut aussi être vide. Ta fonction doit utiliser la recherche binaire, en divisant la plage de recherche par deux à chaque étape, et non un parcours linéaire.

Exemple d'appel de fonction :
```python
print(binary_search([1, 3, 5, 7], 5))
# affiche 2
```

# --seed--

```python
def binary_search(arr, target):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Rechercher dans une liste vide doit renvoyer -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

Rechercher 5 dans `[5]` doit renvoyer 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

Rechercher 9 dans `[5]` doit renvoyer -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

Le premier élément -9 de la liste de 12 éléments doit être trouvé à l'index 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

Le dernier élément 78 de la liste de 12 éléments doit être trouvé à l'index 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

L'élément 15 doit être trouvé à l'index 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

L'élément 22 doit être trouvé à l'index 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

La valeur 12, qui se situe entre 11 et 15, doit renvoyer -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Une valeur cherchée plus petite que tous les éléments doit renvoyer -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Une valeur cherchée plus grande que tous les éléments doit renvoyer -1

```python
    def test10(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
