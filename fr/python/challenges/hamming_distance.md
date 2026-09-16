---
language: python
exerciseType: 1
difficulty: 1
title: Distance de Hamming
---

# --description--

L'ADN s'écrit sous la forme d'un brin de nucléotides, chacun étant une seule lettre : `A`, `C`, `G` ou `T`. Lorsque deux brins de même longueur sont alignés côte à côte, certaines positions portent le même nucléotide et d'autres un nucléotide différent.

Le nombre de positions où les deux brins diffèrent s'appelle la distance de Hamming, et les biologistes l'utilisent pour mesurer à quel point deux brins ont divergé. L'alignement de `GAGCCTACTAACGGGAT` avec `CATCGTAATGACGGCCT` donne 7 positions différentes, leur distance de Hamming est donc 7.

# --instructions--

Écrivez une fonction `hamming_distance` qui prend deux brins d'ADN de même longueur et retourne le nombre de positions où ils diffèrent.

Exemples :
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- Les deux brins ont toujours la même longueur, vous n'avez donc jamais à gérer des brins de longueurs différentes.
- Deux brins vides ne diffèrent nulle part, leur distance est donc 0.

# --seed--

```python
def hamming_distance(left, right):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Deux brins vides ne diffèrent nulle part

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Deux brins identiques d'un seul nucléotide n'ont aucune différence

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Deux brins d'un seul nucléotide différents diffèrent en une position

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Deux brins courts qui diffèrent à chaque position

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Deux brins courts qui ne diffèrent qu'à la première position

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

Un seul nucléotide différent au milieu des brins

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

Les mêmes nucléotides à des positions différentes comptent quand même comme des différences

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

Une paire de brins plus longue avec quatre différences

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Décaler un brin d'une position fait différer presque toutes les positions

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

Les deux brins de la description ont une distance de sept

```python
    def test10(self):
        self.assertEqual(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def hamming_distance(left, right):
    distance = 0

    for left_nucleotide, right_nucleotide in zip(left, right):
        if left_nucleotide != right_nucleotide:
            distance += 1

    return distance
```
