---
language: python
exerciseType: 1
difficulty: 2
title: 이진 탐색
---

# --description--

이진 탐색은 **정렬된** 컬렉션 안에서 값을 찾는 방법으로, 탐색 범위를 계속 절반으로 나눕니다. 가운데 원소를 확인하고, 그것이 찾는 값이 아니라면 찾는 값이 더 작을 때는 왼쪽 절반을, 더 클 때는 오른쪽 절반을 계속 탐색합니다.

매 단계마다 남은 원소의 절반을 버리기 때문에, 이진 탐색은 아주 큰 컬렉션에서도 몇 번의 비교만으로 답에 도달합니다. 반면 원소를 하나씩 확인하는 방식은 원소의 개수만큼 단계가 필요합니다.

# --instructions--

오름차순으로 정렬된 정수 목록과 타깃 정수를 받아, 타깃이 목록 안에 있으면 그 인덱스를, 없으면 `-1`을 반환하는 함수 `binary_search`를 작성하세요.

목록에는 중복이 없으므로 인덱스는 항상 유일합니다. 목록이 비어 있을 수도 있습니다. 함수는 선형 탐색이 아니라 매 단계마다 탐색 범위를 절반으로 줄이는 이진 탐색을 사용해야 합니다.

함수 호출 예시:
```python
print(binary_search([1, 3, 5, 7], 5))
# 2 출력
```

# --seed--

```python
def binary_search(arr, target):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

빈 목록에서 탐색하면 -1을 반환해야 합니다

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

`[5]`에서 5를 탐색하면 0을 반환해야 합니다

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

`[5]`에서 9를 탐색하면 -1을 반환해야 합니다

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

12개의 원소를 가진 목록의 첫 번째 원소 -9는 인덱스 0에서 찾아야 합니다

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

12개의 원소를 가진 목록의 마지막 원소 78은 인덱스 11에서 찾아야 합니다

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

원소 15는 인덱스 6에서 찾아야 합니다

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

원소 22는 인덱스 7에서 찾아야 합니다

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

11과 15 사이에 있는 값 12는 -1을 반환해야 합니다

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

모든 원소보다 작은 타깃은 -1을 반환해야 합니다

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

모든 원소보다 큰 타깃은 -1을 반환해야 합니다

```python
    def test10(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
