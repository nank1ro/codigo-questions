---
language: python
exerciseType: 1
title: Функция Аккермана
difficulty: 1
---

# --description--

Функция Аккермана — это классический пример рекурсивной функции, примечательный тем, что она не является примитивно рекурсивной. Её значение растёт очень быстро, как и размер дерева вызовов.

Функция Аккермана обычно определяется следующим образом:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Её аргументы никогда не бывают отрицательными, и она всегда завершается

# --instructions--

Напишите функцию, которая возвращает значение функции Аккермана.

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

`ack(0, 0)` должна возвращать 1.

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` должна возвращать 3.

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` должна возвращать 13.

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` должна возвращать 61.

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
