---
language: python
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Ihnen wird eine Ganzzahl `num` gegeben.
Schreiben Sie ein Programm, um die Summe aller Ziffern von `num` zu berechnen

# --instructions--

Geben Sie die Summe der Ziffern von `num` zurück

# --seed--

```python
def sum_digits(num: int):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Die Summe der Ziffern von 12345 ist 15

```python
    def test_sum_of_digits_1(self):
        self.assertEqual(sum_digits(12345), 15, "--err-t1--")
```

Die Summe der Ziffern von 57253 ist 22

```python
    def test_sum_of_digits_2(self):
        self.assertEqual(sum_digits(57253), 22, "--err-t2--")
```

Die Summe der Ziffern von 122 ist 5

```python
    def test_sum_of_digits_3(self):
        self.assertEqual(sum_digits(122), 5, "--err-t3--")
```

Die Summe der Ziffern von 91979997 ist 60

```python
    def test_sum_of_digits_4(self):
        self.assertEqual(sum_digits(91979997), 60, "--err-t4--")
```

Die Summe der Ziffern von 2147483647 ist 46

```python
    def test_sum_of_digits_5(self):
        self.assertEqual(sum_digits(2147483647), 46, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def sum_digits(num: int):
    result = 0
    while num > 0:
      result += num % 10
      num //= 10
    return result
```
