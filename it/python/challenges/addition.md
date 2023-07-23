---
language: python
exerciseType: 1
difficulty: 1
title: Addizione
---

# --description--

Dati due number interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri

# --seed--

```python
def somma():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

La somma di 1 e 3 deve essere uguale a 4

```python
    def test_addition1(self):
        self.assertEqual(somma(1, 3), 4, "--err-t1--")
```

La somma di 200 e 210 deve essere uguale a 410

```python
    def test_addition2(self):
        self.assertEqual(somma(200, 210), 410, "--err-t2--")
```

La somma di 15 e 35 deve essere uguale a 50

```python
    def test_addition3(self):
        self.assertEqual(somma(15, 35), 50, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def somma(num1, num2):
    return num1 + num2
```
