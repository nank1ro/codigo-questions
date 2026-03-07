---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Создайте функцию, которая принимает число в качестве аргумента и возвращает `"Fizz"`, `"Buzz"` или `"FizzBuzz"`.

# --instructions--

- Если число кратно `3`, результат должен быть `"Fizz"`
- Если число кратно `5`, результат должен быть `"Buzz"`.
- Если число кратно и `3`, и `5`, результат должен быть `"FizzBuzz"`.
- Если число не кратно ни `3`, ни `5`, должно быть выведено само число, как показано в примерах ниже.
- Результат всегда должен быть строкой, даже если число не кратно `3` или `5`.

Примеры:
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

Число `3` должно быть равно `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

Число `5` должно быть равно `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

Число `15` должно быть равно `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

Число `10` должно быть равно `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

Число `98` должно быть равно `"98"`

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
