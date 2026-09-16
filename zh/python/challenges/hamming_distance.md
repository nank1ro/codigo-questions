---
language: python
exerciseType: 1
difficulty: 1
title: 汉明距离
---

# --description--

DNA 写成一条由核苷酸组成的链，每个核苷酸是单个字母：`A`、`C`、`G` 或 `T`。当两条等长的链并排排列时，有些位置上的核苷酸相同，有些位置上的核苷酸则不同。

两条链上不同位置的数目称为汉明距离，生物学家用它来衡量两条链已经分化得有多远。将 `GAGCCTACTAACGGGAT` 与 `CATCGTAATGACGGCCT` 并排对齐后有 7 个位置不同，因此它们的汉明距离是 7。

# --instructions--

编写一个函数 `hamming_distance`，它接收两条等长的 DNA 链，并返回它们不同位置的数目。

示例：
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- 两条链的长度总是相同的，所以你无需处理长度不同的链。
- 两条空链没有任何不同，所以它们的距离是 0。

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

两条空链没有任何不同

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

两条相同的单核苷酸链没有差异

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

两条不同的单核苷酸链在一个位置上不同

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

两条在每个位置都不同的短链

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

两条只在第一个位置不同的短链

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

链的中间有一个不同的核苷酸

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

相同核苷酸出现在不同位置也算作差异

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

一对有四个差异的较长的链

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

将一条链移动一个位置会使几乎所有位置都不同

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

描述中的两条链的距离为 7

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
