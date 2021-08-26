---
language: python
exerciseType: 1
difficulty: 1
title: Somma cifre
---

# --description--

Ti viene dato un numero intero `num`.
Scrivi un programma per calcolare la somma di tutte le cifre di `num`

# --instructions--

Restituisci la somma delle cifre di `num`

# --seed--

```python
def somma_cifre():
    pass
```

# --before-asserts--

```python
import unittest

class SumDigitsTest(unittest.TestCase):
```

# --asserts--

La somma delle cifre di 12345 è 15

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(somma_cifre(12345), 15, "--err-t1--")
```

La somma delle cifre di 57253 è 22

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(somma_cifre(57253), 22, "--err-t2--")
```

La somma delle cifre di 122 è 5

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(somma_cifre(122), 5, "--err-t3--")
```

La somma delle cifre di 91979997 è 60

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(somma_cifre(91979997), 60, "--err-t4--")
```

La somma delle cifre di 2147483647 è 46

```python
    def test_sum_of_digits_5(self):
        self.assertEqual(somma_cifre(2147483647), 46, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def somma_cifre(num: int):
    risultato = 0
    while num > 0:
      risultato += num % 10
      num //= 10
    return risultato
```
