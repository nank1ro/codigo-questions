---
language: python
exerciseType: 1
difficulty: 1
title: 考拉兹猜想
---

# --description--

考拉兹猜想从任意正整数 `n` 出发，重复一条简单的规则：如果 `n` 是偶数，就把它减半；如果 `n` 是奇数，就把它替换为 `3n + 1`。这个序列迟早会到达 1。

例如，从 16 开始，序列是 `16 -> 8 -> 4 -> 2 -> 1`，因此需要 4 步。

从来没有人证明过这一规律总是成立，但对于每一个被测试过的数它都成立。

# --instructions--

编写一个函数 `collatz_steps`，它接收一个正整数 `n`，并返回到达 1 所需的步数。

`collatz_steps(1)` 为 0，因为 1 已经是序列的终点。`collatz_steps(12)` 为 9，而 `collatz_steps(27)` 为 111。

# --seed--

```python
def collatz_steps(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`collatz_steps(1)` 应返回 0，因为 1 已经是序列的终点。

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` 应返回 1。

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` 应返回 8。

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` 应返回 16。

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` 应返回 4。

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` 应返回 9。

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` 应返回 111。

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` 应返回 118。

```python
    def test8(self):
        self.assertEqual(collatz_steps(97), 118, "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def collatz_steps(n):
    value = n
    steps = 0
    while value != 1:
        value = value // 2 if value % 2 == 0 else 3 * value + 1
        steps += 1
    return steps
```
