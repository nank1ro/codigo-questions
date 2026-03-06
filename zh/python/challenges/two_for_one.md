---
language: python
exerciseType: 1
difficulty: 1
title: 二换一
---

# --description--

给定一个名字，返回包含以下消息的字符串：
`One for X, one for me.`
其中 `X` 是给定的名字。
但是，如果没有提供名字，则返回字符串：
`One for you, one for me.`

# --instructions--

编写一个函数，返回正确的字符串，示例：

**输入**：`Walter`
**输出**：`One for Walter, one for me.`

**输入**：
**输出**：`One for you, one for me.`

**输入**：`David`
**输出**：`One for David, one for me.`

# --seed--

```python
def two_for_one(name):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

未提供名字

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

传入 "James" 作为名字

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


传入 "Martha" 作为名字

```python
    def test_another_name_given(self):
        self.assertEqual(two_for_one("Martha"), "One for Martha, one for me.", "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def two_for_one(name = None):
    if not name:
      return "One for you, one for me."
    return f"One for {name}, one for me."
```
