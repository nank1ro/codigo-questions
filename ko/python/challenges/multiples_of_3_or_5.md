---
language: python
exerciseType: 1
difficulty: 1
title: 3 또는 5의 배수
---

# --description--

10 미만의 자연수 중 3 또는 5의 배수를 나열하면 3, 5, 6, 9입니다. 이 배수들의 합은 23입니다.

# --instructions--

주어진 매개변수 값 `number` 미만의 3 또는 5의 모든 배수의 합을 구하세요.

# --seed--

```python
def multiples_of_3_and_5(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`multiples_of_3_and_5(10)`은 23을 반환해야 합니다.

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)`은 233168을 반환해야 합니다.

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)`은 11390208을 반환해야 합니다

```python
    def test3(self):
        self.assertEqual(multiples_of_3_and_5(6987), 11390208, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def multiples_of_3_and_5(number):
  total = 0
  for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total
```
