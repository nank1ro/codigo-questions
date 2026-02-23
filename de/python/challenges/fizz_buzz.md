---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Create a function that takes a number as an argument and returns `"Fizz"`, `"Buzz"` or `"FizzBuzz"`.

# --instructions--

- If the number is a multiple of `3` the output should be `"Fizz"`
- If the number given is a multiple of `5`, the output should be `"Buzz"`.
- If the number given is a multiple of both `3` and `5`, the output should be `"FizzBuzz"`.
- If the number is not a multiple of either `3` or `5`, the number should be output on its own as shown in the examples below.
- The output should always be a string even if it is not a multiple of `3` or `5`.

Examples:
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

The number `3` must equal `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

The number `5` must equal `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

The number `15` must equal `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

The number `10` must equal `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

The number `98` must equal `"98"`

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
