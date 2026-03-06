---
language: python
exerciseType: 1
difficulty: 1
title: 数字之和
---

# --description--

给你一个整数 `num`。
编写一个程序来计算 `num` 所有数字之和

# --instructions--

返回 `num` 的各位数字之和

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

12345的各位数字之和是15

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

57253的各位数字之和是22

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

122的各位数字之和是5

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

91979997的各位数字之和是60

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

2147483647的各位数字之和是46

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
