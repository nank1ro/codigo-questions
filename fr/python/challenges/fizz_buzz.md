---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Créez une fonction qui prend un nombre comme argument et retourne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Si le nombre est un multiple de `3`, la sortie doit être `"Fizz"`
- Si le nombre donné est un multiple de `5`, la sortie doit être `"Buzz"`.
- Si le nombre donné est un multiple de `3` et `5`, la sortie doit être `"FizzBuzz"`.
- Si le nombre n'est pas un multiple de `3` ou `5`, le nombre doit être affiché comme montré dans les exemples ci-dessous.
- La sortie doit toujours être une chaîne même si ce n'est pas un multiple de `3` ou `5`.

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
