---
language: python
exerciseType: 1
difficulty: 1
title: 해밍 거리
---

# --description--

DNA는 각각 한 글자인 뉴클레오터드 가닥으로 표기합니다: `A`, `C`, `G` 또는 `T`. 같은 길이의 두 가닥을 나란히 놓으면 어떤 위치에는 같은 뉴클레오터드가 있고 어떤 위치에는 다른 뉴클레오터드가 있습니다.

두 가닥이 서로 다른 위치의 개수를 해밍 거리라고 하며, 생물학자들은 이를 이용해 두 가닥이 얼마나 멀어졌는지 측정합니다. `GAGCCTACTAACGGGAT`를 `CATCGTAATGACGGCCT`와 나란히 놓으면 서로 다른 위치가 7개이므로 두 가닥의 해밍 거리는 7입니다.

# --instructions--

같은 길이의 두 DNA 가닥을 받아 서로 다른 위치의 개수를 반환하는 함수 `hamming_distance`를 작성하세요.

예시:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- 두 가닥은 항상 길이가 같으므로 길이가 다른 가닥을 처리할 필요는 없습니다.
- 두 빈 가닥은 어디에서도 다르지 않으므로 거리는 0입니다.

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

두 빈 가닥은 어디에서도 다르지 않습니다

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

같은 뉴클레오터드 하나를 가진 두 가닥에는 차이가 없습니다

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

다른 뉴클레오터드 하나를 가진 두 가닥은 한 위치에서 다릅니다

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

모든 위치에서 다른 두 짧은 가닥

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

첫 번째 위치에서만 다른 두 짧은 가닥

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

가닥 중간에 하나의 다른 뉴클레오터드

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

위치가 다른 같은 뉴클레오터드도 차이로 계산됩니다

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

네 군데가 다른 더 긴 가닥 쌍

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

가닥을 한 칸 밀면 거의 모든 위치가 달라집니다

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

설명에 나온 두 가닥의 거리는 7입니다

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
