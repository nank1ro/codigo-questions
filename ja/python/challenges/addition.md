---
language: python
exerciseType: 1
title: 足し算
difficulty: 1
---

# --description--

2つの整数`num1`と`num2`が与えられたとき、これら2つの数を足すプログラムを書いてください。

# --instructions--

2つの数の合計を返す関数を書いてください。

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

1と3の合計は4でなければなりません

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

200と210の合計は410でなければなりません

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

15と35の合計は50でなければなりません

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
