---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Crie uma função que receba um número como argumento e retorne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Se o número for um múltiplo de `3`, a saída deve ser `"Fizz"`
- Se o número dado for um múltiplo de `5`, a saída deve ser `"Buzz"`.
- Se o número dado for um múltiplo de `3` e `5`, a saída deve ser `"FizzBuzz"`.
- Se o número não for um múltiplo de `3` ou `5`, o número deve ser retornado como mostrado nos exemplos abaixo.
- A saída deve sempre ser uma string, mesmo que não seja um múltiplo de `3` ou `5`.

Exemplos:
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

O número `3` deve ser igual a `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

O número `5` deve ser igual a `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

O número `15` deve ser igual a `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

O número `10` deve ser igual a `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

O número `98` deve ser igual a `"98"`

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
