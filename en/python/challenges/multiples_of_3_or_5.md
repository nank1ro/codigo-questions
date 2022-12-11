---
language: python
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# --instructions--

Find the sum of all the multiples of 3 or 5 below the provided parameter value `number`.

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

`multiples_of_3_and_5(10)` should return 23.

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)` should return 233168.

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)` should return 11390208

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
