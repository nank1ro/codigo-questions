---
language: python
exerciseType: 1
title: Addition
difficulty: 1
---

# --description--

Given two integers `num1` and `num2`, write a program to add these two numbers

# --instructions--

Write a function that returns the sum of two numbers

# --seed--

```python
def addition():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

The sum of 1 and 3 must equal 4

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

The sum of 200 and 210 must equal 410

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

The sum of 15 and 35 must equal 50

```python
    def test_addition3(self):
        self.assertEqual(addition(15, 35), 50, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def addition(num1, num2):
	return num1 + num2
```
