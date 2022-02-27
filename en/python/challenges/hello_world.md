---
language: python
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.

# --instructions--

Write a function that returns the string "Hello, World!".

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

The function should return "Hello, World!".

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
