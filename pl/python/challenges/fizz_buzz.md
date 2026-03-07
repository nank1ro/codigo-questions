---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Utwórz funkcję, która przyjmuje liczbę jako argument i zwraca `"Fizz"`, `"Buzz"` lub `"FizzBuzz"`.

# --instructions--

- Jeśli liczba jest wielokrotnością `3`, wynikiem powinno być `"Fizz"`
- Jeśli podana liczba jest wielokrotnością `5`, wynikiem powinno być `"Buzz"`.
- Jeśli podana liczba jest wielokrotnością zarówno `3`, jak i `5`, wynikiem powinno być `"FizzBuzz"`.
- Jeśli liczba nie jest wielokrotnością ani `3`, ani `5`, wynikiem powinna być sama liczba, jak pokazano w przykładach poniżej.
- Wynik powinien zawsze być ciągiem znaków, nawet jeśli nie jest wielokrotnością `3` ani `5`.

Przykłady:
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

Liczba `3` musi być równa `"Fizz"`

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

Liczba `5` musi być równa `"Buzz"`

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

Liczba `15` musi być równa `"FizzBuzz"`

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

Liczba `10` musi być równa `"Buzz"`

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

Liczba `98` musi być równa `"98"`

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
