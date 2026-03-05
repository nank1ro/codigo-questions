---
language: python
exerciseType: 1
title: 100 portes
difficulty: 1
---

# --description--

Il y a 100 portes d'affilée qui sont toutes initialement fermées.
Vous faites 100 passages par les portes.
La première fois, visitez chaque porte et 'basculez' la porte (si la porte est fermée, ouvrez-la; si elle est ouverte, fermez-la).
La deuxième fois, visitez seulement chaque 2ème porte (c.-à-d., porte #2, #4, #6, ...) et basculez-la.
La troisième fois, visitez chaque 3ème porte (c.-à-d., porte #3, #6, #9, ...), etc., jusqu'à ce que vous ne visitiez que la 100ème porte.

# --instructions--

Implémentez une fonction pour déterminer l'état des portes après le dernier passage.
Retournez le résultat final dans un tableau, avec seulement le numéro de porte inclus dans le tableau s'il est ouvert.
> La méthode doit pouvoir fonctionner avec un nombre variable de portes.

# --seed--

```python
def get_final_opened_doors(num_doors):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Étant donné 100 portes, retournez la liste correcte des portes ouvertes

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

Étant donné 10 portes, retournez la liste correcte des portes ouvertes

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

Étant donné 950 portes, retournez la liste correcte des portes ouvertes

```python
    def test_3(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        self.assertEqual(get_final_opened_doors(950), solution, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def get_final_opened_doors(num_doors):
    open_doors = []
    i = 1;
    while (i**2) <= num_doors:
        open_doors.append(i**2)
        i += 1
    return open_doors
```
