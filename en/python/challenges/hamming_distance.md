---
language: python
exerciseType: 1
difficulty: 1
title: Hamming distance
---

# --description--

DNA is written as a strand of nucleotides, each one a single letter: `A`, `C`, `G` or `T`. When two strands of the same length are lined up side by side, some positions hold the same nucleotide and some hold different ones.

The number of positions where the two strands differ is called the Hamming distance, and biologists use it to measure how far two strands have drifted apart. Lining up `GAGCCTACTAACGGGAT` with `CATCGTAATGACGGCCT` gives 7 positions that differ, so their Hamming distance is 7.

# --instructions--

Write a function `hamming_distance` that takes two DNA strands of the same length and returns the number of positions where they differ.

Examples:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- The two strands always have the same length, so you never have to handle strands of different lengths.
- Two empty strands differ nowhere, so their distance is 0.

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

Two empty strands differ nowhere

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Two identical single nucleotide strands have no difference

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Two different single nucleotide strands differ in one position

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Two short strands that differ in every position

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Two short strands that differ in the first position only

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

A single differing nucleotide in the middle of the strands

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

The same nucleotides in different positions still count as differences

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

A longer pair of strands with four differences

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Shifting a strand by one position makes almost every position differ

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

The two strands from the description have a distance of seven

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
