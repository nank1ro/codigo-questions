---
language: python
exerciseType: 1
difficulty: 1
title: 둘이서 하나
---

# --description--

이름이 주어지면 다음 메시지가 포함된 문자열을 반환합니다:
`One for X, one for me.`
여기서 `X`는 주어진 이름입니다.
단, 이름이 없으면 다음 문자열을 반환합니다:
`One for you, one for me.`

# --instructions--

올바른 문자열을 반환하는 함수를 작성하세요. 예시:

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

이름이 주어지지 않은 경우

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

이름으로 "James"를 전달한 경우

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


이름으로 "Martha"를 전달한 경우

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
