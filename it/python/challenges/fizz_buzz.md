---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Crea una funzione che prenda un numero come argomento e restituisca `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Se il numero è un multiplo di `3`, l'output deve essere `"Fizz"`.
- Se il numero è un multiplo di `5`, l'output deve essere `"Buzz"`.
- Se il numero è un multiplo sia di `3` che di `5`, l'output deve essere `"FizzBuzz"`.
- Se il numero non è un multiplo né di `3` né di `5`, il numero deve essere stampato come stringa, come mostrato negli esempi seguenti.
- L'output deve sempre essere una stringa, anche se non è un multiplo di `3` o `5`.

Esempi:
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

Il numero `3` deve essere uguale a `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

Il numero `5` deve essere uguale a `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

Il numero `15` deve essere uguale a `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

Il numero `10` deve essere uguale a `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

Il numero `98` deve essere uguale a `"98"`

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
