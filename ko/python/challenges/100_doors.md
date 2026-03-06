---
language: python
exerciseType: 1
title: 100개의 문
difficulty: 1
---

# --description--

일렬로 100개의 문이 있으며 모두 처음에는 닫혀 있습니다.
100번의 통과를 합니다.
첫 번째 통과에서는 모든 문을 방문하여 문을 '전환'합니다 (문이 닫혀 있으면 열고, 열려 있으면 닫습니다).
두 번째 통과에서는 2번째 문마다 방문하여 (즉, 문 #2, #4, #6, ...) 전환합니다.
세 번째 통과에서는 3번째 문마다 방문하여 (즉, 문 #3, #6, #9, ...) 전환합니다. 이런 식으로 100번째 문만 방문할 때까지 계속합니다.

# --instructions--

마지막 통과 후 문의 상태를 결정하는 함수를 구현하세요.
최종 결과를 배열로 반환하되, 열려 있는 문의 번호만 배열에 포함하세요.
> 이 메서드는 가변적인 문의 수에 대해 작동할 수 있어야 합니다.

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

100개의 문이 주어졌을 때, 열려 있는 문의 올바른 목록을 반환합니다

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

10개의 문이 주어졌을 때, 열려 있는 문의 올바른 목록을 반환합니다

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

950개의 문이 주어졌을 때, 열려 있는 문의 올바른 목록을 반환합니다

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
