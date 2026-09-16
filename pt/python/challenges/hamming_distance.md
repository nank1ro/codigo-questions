---
language: python
exerciseType: 1
difficulty: 1
title: Distância de Hamming
---

# --description--

O DNA é escrito como uma fita de nucleotídeos, cada um representado por uma única letra: `A`, `C`, `G` ou `T`. Quando duas fitas de mesmo comprimento são alinhadas lado a lado, algumas posições contêm o mesmo nucleotídeo e outras contêm nucleotídeos diferentes.

O número de posições em que as duas fitas diferem é chamado de distância de Hamming, e biólogos o usam para medir o quanto duas fitas se afastaram uma da outra. Alinhar `GAGCCTACTAACGGGAT` com `CATCGTAATGACGGCCT` resulta em 7 posições que diferem, de modo que a distância de Hamming entre elas é 7.

# --instructions--

Escreva uma função `hamming_distance` que recebe duas fitas de DNA de mesmo comprimento e retorna o número de posições em que elas diferem.

Exemplos:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- As duas fitas sempre têm o mesmo comprimento, então você nunca precisa lidar com fitas de comprimentos diferentes.
- Duas fitas vazias não diferem em nenhuma posição, então a distância entre elas é 0.

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

Duas fitas vazias não diferem em nenhuma posição

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Duas fitas idênticas de um único nucleotídeo não têm nenhuma diferença

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Duas fitas diferentes de um único nucleotídeo diferem em uma posição

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Duas fitas curtas que diferem em todas as posições

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Duas fitas curtas que diferem apenas na primeira posição

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

Um único nucleotídeo diferente no meio das fitas

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

Os mesmos nucleotídeos em posições diferentes ainda contam como diferenças

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

Um par de fitas mais longo com quatro diferenças

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Deslocar uma fita em uma posição faz quase todas as posições diferirem

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

As duas fitas da descrição têm uma distância de sete

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
