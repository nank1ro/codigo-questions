---
language: python
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se elenchiamo tutti i numeri naturali inferiori a 10 che sono multipli di 3 o 5, otteniamo 3, 5, 6 e 9. La somma di questi multipli è 23.

# --instructions--

Trova la somma di tutti i multipli di 3 o 5 al di sotto del valore del parametro fornito `number`.

# --seed--

```python
def multiples_of_3_and_5(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`multiples_of_3_and_5(10)` deve restituire 23.

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)` deve restituire 233168.

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)` deve restituire 11390208

```python
    def test3(self):
        self.assertEqual(multiples_of_3_and_5(6987), 11390208, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def multiples_of_3_and_5(number):
  total = 0
  for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total
```
