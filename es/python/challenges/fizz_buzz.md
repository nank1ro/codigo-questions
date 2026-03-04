---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Crea una función que toma un número como argumento y devuelve `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Si el número es un múltiplo de `3` la salida debe ser `"Fizz"`
- Si el número dado es un múltiplo de `5`, la salida debe ser `"Buzz"`.
- Si el número dado es un múltiplo de ambos `3` y `5`, la salida debe ser `"FizzBuzz"`.
- Si el número no es un múltiplo de `3` o `5`, el número debe ser mostrado por sí solo como se muestra en los ejemplos a continuación.
- La salida siempre debe ser una cadena incluso si no es un múltiplo de `3` o `5`.

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

El número `3` debe igual `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

El número `5` debe igual `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

El número `15` debe igual `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

El número `10` debe igual `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

El número `98` debe igual `"98"`

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
