---
language: python
exerciseType: 1
title: 阿克曼函数
difficulty: 1
---

# --description--

阿克曼函数是递归函数的经典示例，尤其值得注意的是它不是原始递归函数。它的值增长非常快，其调用树的大小也是如此。

阿克曼函数通常定义如下：

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

它的参数永远不为负数，且总是会终止

# --instructions--

编写一个函数，返回阿克曼函数的值。

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

`ack(0, 0)` 应返回 1。

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` 应返回 3。

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` 应返回 13。

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` 应返回 61。

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
