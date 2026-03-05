---
language: python
exerciseType: 1
difficulty: 1
title: 자릿수의 합
---

# --description--

정수 `num`이 주어집니다.
`num`의 모든 자릿수의 합을 계산하는 프로그램을 작성하세요.

# --instructions--

`num`의 자릿수의 합을 반환하세요.

# --seed--

```python
def sum_digits(num: int):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

12345의 자릿수의 합은 15입니다

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

57253의 자릿수의 합은 22입니다

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

122의 자릿수의 합은 5입니다

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

91979997의 자릿수의 합은 60입니다

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

2147483647의 자릿수의 합은 46입니다

```python
    def test_sum_of_digits_5(self):
        self.assertEqual(sum_digits(2147483647), 46, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def sum_digits(num: int):
    result = 0
    while num > 0:
      result += num % 10
      num //= 10
    return result
```
