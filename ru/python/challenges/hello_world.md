---
language: python
exerciseType: 1
difficulty: 1
title: Привет, мир!
---

# --description--

__"Привет, мир!"__ — это традиционная первая программа для начинающих программировать на новом языке или в новой среде.

# --instructions--

Напишите функцию, которая возвращает строку "Hello, World!".

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

Функция должна возвращать "Hello, World!".

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
