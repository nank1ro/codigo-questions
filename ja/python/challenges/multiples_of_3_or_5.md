---
language: python
exerciseType: 1
difficulty: 1
title: 3または5の倍数
---

# --description--

10未満の自然数のうち、3または5の倍数をリストすると、3、5、6、9が得られます。これらの倍数の合計は23です。

# --instructions--

指定されたパラメータ値`number`未満の3または5のすべての倍数の合計を求めてください。

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

`multiples_of_3_and_5(10)`は23を返すべきです。

```python
    def test1(self):
        self.assertEqual(multiples_of_3_and_5(10), 23, "--err-t1--")
```

`multiples_of_3_and_5(1000)`は233168を返すべきです。

```python
    def test2(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168, "--err-t2--")
```

`multiples_of_3_and_5(6987)`は11390208を返すべきです

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
