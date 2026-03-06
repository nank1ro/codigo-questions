---
language: python
exerciseType: 1
title: 덧셈
difficulty: 1
---

# --description--

두 정수 `num1`과 `num2`가 주어졌을 때, 이 두 수를 더하는 프로그램을 작성하세요.

# --instructions--

두 수의 합을 반환하는 함수를 작성하세요.

# --seed--

```python
def addition():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

1과 3의 합은 4여야 합니다

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

200과 210의 합은 410이어야 합니다

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

15와 35의 합은 50이어야 합니다

```python
    def test_addition3(self):
        self.assertEqual(addition(15, 35), 50, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def addition(num1, num2):
    return num1 + num2
```
