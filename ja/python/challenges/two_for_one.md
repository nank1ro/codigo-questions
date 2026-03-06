---
language: python
exerciseType: 1
difficulty: 1
title: 2対1
---

# --description--

名前が与えられたとき、次のメッセージを含む文字列を返してください：
`One for X, one for me.`
ここで`X`は与えられた名前です。
ただし、名前が指定されていない場合は、次の文字列を返してください：
`One for you, one for me.`

# --instructions--

正しい文字列を返す関数を書いてください。例：

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

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

名前が指定されていない場合

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

名前に"James"を渡す

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


名前に"Martha"を渡す

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
