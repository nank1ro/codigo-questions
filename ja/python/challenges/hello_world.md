---
language: python
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__は、新しい言語や環境でプログラミングを始める際の伝統的な最初のプログラムです。

# --instructions--

文字列"Hello, World!"を返す関数を書いてください。

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

関数は"Hello, World!"を返すべきです。

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
