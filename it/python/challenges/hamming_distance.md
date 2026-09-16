---
language: python
exerciseType: 1
difficulty: 1
title: Distanza di Hamming
---

# --description--

Il DNA è scritto come un filamento di nucleotidi, ognuno dei quali è una singola lettera: `A`, `C`, `G` o `T`. Quando due filamenti della stessa lunghezza vengono affiancati, alcune posizioni contengono lo stesso nucleotide e altre ne contengono di diversi.

Il numero di posizioni in cui i due filamenti differiscono è chiamato distanza di Hamming, e i biologi lo usano per misurare quanto due filamenti si sono allontanati l'uno dall'altro. Affiancando `GAGCCTACTAACGGGAT` con `CATCGTAATGACGGCCT` si ottengono 7 posizioni che differiscono, quindi la loro distanza di Hamming è 7.

# --instructions--

Write a function `hamming_distance` that takes two DNA strands of the same length and returns the number of positions where they differ.

Esempi:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- I due filamenti hanno sempre la stessa lunghezza, quindi non devi mai gestire filamenti di lunghezza diversa.
- Due filamenti vuoti non differiscono in nessuna posizione, quindi la loro distanza è 0.

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

Due filamenti vuoti non differiscono in nessuna posizione

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Due filamenti identici di un solo nucleotide non hanno differenze

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Due filamenti di un solo nucleotide diversi differiscono in una posizione

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Due filamenti brevi che differiscono in ogni posizione

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Due filamenti brevi che differiscono solo nella prima posizione

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

Un singolo nucleotide diverso nel mezzo dei filamenti

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

Gli stessi nucleotidi in posizioni diverse contano comunque come differenze

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

Una coppia di filamenti più lunga con quattro differenze

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Spostare un filamento di una posizione fa differire quasi ogni posizione

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

I due filamenti della descrizione hanno una distanza di sette

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
