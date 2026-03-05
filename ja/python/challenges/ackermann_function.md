---
language: python
exerciseType: 1
title: アッカーマン関数
difficulty: 1
---

# --description--

アッカーマン関数は再帰関数の典型的な例であり、特に原始再帰関数ではないことで知られています。その値は非常に急速に増加し、呼び出しツリーのサイズも同様です。

アッカーマン関数は通常、次のように定義されます：

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

引数は決して負にならず、常に終了します。

# --instructions--

アッカーマン関数の値を返す関数を書いてください。

# --seed--

```python
def ack(m, n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`ack(0, 0)`は1を返すべきです。

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)`は3を返すべきです。

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)`は13を返すべきです。

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)`は61を返すべきです。

```python
    def test4(self):
        self.assertEqual(ack(3, 3), 61, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def ack(m, n):
    if m == 0:
        return n + 1
    else:
        if (n == 0):
            return ack(m - 1, 1)
        return ack(m - 1, ack(m, n - 1))
```
