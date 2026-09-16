---
language: python
exerciseType: 1
difficulty: 1
title: Odległość Hamminga
---

# --description--

DNA zapisuje się jako nić nukleotydów, z których każdy jest pojedynczą literą: `A`, `C`, `G` lub `T`. Gdy dwie nici o tej samej długości ustawimy obok siebie, niektóre pozycje mają ten sam nukleotyd, a niektóre różne.

Liczba pozycji, w których dwie nici różnią się między sobą, nazywana jest odległością Hamminga, a biolodzy używają jej do mierzenia, jak bardzo dwie nici się od siebie oddaliły. Ustawienie `GAGCCTACTAACGGGAT` obok `CATCGTAATGACGGCCT` daje 7 różniących się pozycji, więc ich odległość Hamminga wynosi 7.

# --instructions--

Napisz funkcję `hamming_distance`, która przyjmuje dwie nici DNA o tej samej długości i zwraca liczbę pozycji, w których się różnią.

Przykłady:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- Obie nici zawsze mają tę samą długość, więc nigdy nie musisz obsługiwać nici o różnych długościach.
- Dwie puste nici nie różnią się nigdzie, więc ich odległość wynosi 0.

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

Dwie puste nici nie różnią się nigdzie

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Dwie identyczne nici z pojedynczym nukleotydem nie mają żadnej różnicy

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Dwie różne nici z pojedynczym nukleotydem różnią się w jednej pozycji

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Dwie krótkie nici różniące się w każdej pozycji

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Dwie krótkie nici różniące się tylko w pierwszej pozycji

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

Pojedynczy różniący się nukleotyd w środku nici

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

Te same nukleotydy w różnych pozycjach nadal liczą się jako różnice

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

Dłuższa para nici z czterema różnicami

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Przesunięcie nici o jedną pozycję powoduje, że prawie każda pozycja się różni

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

Dwie nici z opisu mają odległość równą siedem

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
