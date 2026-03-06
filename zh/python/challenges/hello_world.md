---
language: python
exerciseType: 1
difficulty: 1
title: 你好世界！
---

# --description--

__"Hello, World!"__ 是在新语言或环境中开始编程的传统第一个程序。

# --instructions--

编写一个函数，返回字符串 "Hello, World!"。

# --seed--

```python
def hello():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

该函数应返回 "Hello, World!"。

```python
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!", "--err-t1--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def hello():
    return "Hello, World!"
```
