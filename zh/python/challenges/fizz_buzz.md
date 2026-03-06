---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

创建一个函数，接收一个数字作为参数，并返回 `"Fizz"`、`"Buzz"` 或 `"FizzBuzz"`。

# --instructions--

- 如果数字是 `3` 的倍数，输出应为 `"Fizz"`
- 如果给定的数字是 `5` 的倍数，输出应为 `"Buzz"`。
- 如果给定的数字同时是 `3` 和 `5` 的倍数，输出应为 `"FizzBuzz"`。
- 如果数字既不是 `3` 也不是 `5` 的倍数，则按如下示例输出数字本身。
- 即使数字不是 `3` 或 `5` 的倍数，输出也应始终为字符串。

示例：
```python
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```python
def fizz_buzz():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

数字 `3` 必须等于 `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

数字 `5` 必须等于 `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

数字 `15` 必须等于 `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

数字 `10` 必须等于 `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

数字 `98` 必须等于 `"98"`

```python
    def test5(self):
        self.assertEqual(fizz_buzz(98), "98", "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
```
