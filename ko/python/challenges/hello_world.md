---
language: python
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__는 새로운 언어나 환경에서 프로그래밍을 시작할 때 전통적으로 작성하는 첫 번째 프로그램입니다.

# --instructions--

"Hello, World!" 문자열을 반환하는 함수를 작성하세요.

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

함수는 "Hello, World!"를 반환해야 합니다.

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
