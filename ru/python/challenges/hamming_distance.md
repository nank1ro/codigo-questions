---
language: python
exerciseType: 1
difficulty: 1
title: Расстояние Хэмминга
---

# --description--

ДНК записывается в виде цепочки нуклеотидов, каждый из которых обозначается одной буквой: `A`, `C`, `G` или `T`. Когда две цепочки одинаковой длины располагаются рядом друг с другом, в одних позициях стоит один и тот же нуклеотид, а в других — разные.

Количество позиций, в которых две цепочки различаются, называется расстоянием Хэмминга, и биологи используют его, чтобы измерить, насколько далеко две цепочки разошлись друг от друга. Если сопоставить `GAGCCTACTAACGGGAT` с `CATCGTAATGACGGCCT`, различающихся позиций окажется 7, поэтому их расстояние Хэмминга равно 7.

# --instructions--

Напишите функцию `hamming_distance`, которая принимает две цепочки ДНК одинаковой длины и возвращает количество позиций, в которых они различаются.

Примеры:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- У цепочек всегда одинаковая длина, поэтому обрабатывать цепочки разной длины не придётся.
- Две пустые цепочки не различаются нигде, поэтому их расстояние равно 0.

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

Две пустые цепочки не различаются нигде

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Две одинаковые цепочки из одного нуклеотида не имеют различий

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Две разные цепочки из одного нуклеотида различаются в одной позиции

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Две короткие цепочки, различающиеся в каждой позиции

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Две короткие цепочки, различающиеся только в первой позиции

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

Один различающийся нуклеотид в середине цепочек

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

Одинаковые нуклеотиды в разных позициях всё равно считаются различиями

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

Более длинная пара цепочек с четырьмя различиями

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Сдвиг цепочки на одну позицию делает почти каждую позицию различающейся

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

Две цепочки из описания имеют расстояние семь

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
