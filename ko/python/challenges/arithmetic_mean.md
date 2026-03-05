---
language: python
exerciseType: 1
title: 산술 평균
difficulty: 1
---

# --description--

숫자 벡터의 _산술 평균_을 구하는 `mean`이라는 함수를 작성하세요.

# --instructions--

숫자 벡터의 평균을 반환하는 함수를 작성하세요.

함수 호출 예시:
```python
print(mean([1, 2, 3]))
# prints 2
```

# --seed--

```python
def mean():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]`의 평균은 4여야 합니다

```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```

`[4, 5, 6]`의 평균은 5여야 합니다

```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```

`[12, 34, 56, 78]`의 평균은 45여야 합니다

```python
    def test3(self):
        self.assertEqual(mean([12, 34, 56, 78]), 45, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
from math import fsum

def mean(numbers):
    return fsum(numbers) / float(len(numbers))
```
