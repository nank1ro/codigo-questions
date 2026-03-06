---
language: python
exerciseType: 1
title: 加法
difficulty: 1
---

# --description--

给定两个整数 `num1` 和 `num2`，编写一个程序将这两个数相加

# --instructions--

编写一个函数，返回两个数的和

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

1和3的和必须等于4

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

200和210的和必须等于410

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

15和35的和必须等于50

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
