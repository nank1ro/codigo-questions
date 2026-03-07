---
language: python
exerciseType: 1
difficulty: 1
title: Кратные 3 или 5
---

# --description--

Если перечислить все натуральные числа меньше 10, которые кратны 3 или 5, мы получим 3, 5, 6 и 9. Сумма этих кратных равна 23.

# --instructions--

Найдите сумму всех чисел, кратных 3 или 5, меньше заданного значения параметра `number`.

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

`multiples_of_3_and_5(10)` должна возвращать 23.

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)` должна возвращать 233168.

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)` должна возвращать 11390208

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
