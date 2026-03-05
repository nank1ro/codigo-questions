---
language: python
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Wenn wir alle natürlichen Zahlen unter 10 auflisten, die Vielfache von 3 oder 5 sind, erhalten wir 3, 5, 6 und 9. Die Summe dieser Vielfachen ist 23.

# --instructions--

Finden Sie die Summe aller Vielfachen von 3 oder 5 unter dem bereitgestellten Parameterwert `number`.

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

`multiples_of_3_and_5(10)` sollte 23 zurückgeben.

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)` sollte 233168 zurückgeben.

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)` sollte 11390208 zurückgeben

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
