---
language: python
exerciseType: 1
difficulty: 2
title: 애너그램
---

# --description--

한 단어가 다른 단어의 재배열일 때 두 단어는 애너그램입니다. 즉, 정확히 같은 문자를 사용하며 각 문자가 같은 횟수로 나타나고 오직 순서만 다릅니다. `listen`과 `silent`는 애너그램이고, `stone`과 `tones`도 애너그램입니다.

단어는 결코 자기 자신의 애너그램이 아닙니다. 두 단어가 완전히 같으면 재배열된 것이 없으므로 답은 `False`입니다. 두 단어는 모두 소문자로 주어지며 `a`부터 `z`까지의 문자만을 담고 있습니다.

# --instructions--

두 단어 `first`와 `second`를 받아 두 단어가 서로의 애너그램이면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `is_anagram`를 작성하세요.

예시:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- 두 단어가 완전히 같으면 애너그램이 아닙니다.
- 길이가 다른 단어는 결코 애너그램이 아닙니다.
- 모든 문자는 두 단어에서 같은 횟수로 나타나야 합니다.

# --seed--

```python
def is_anagram(first, second):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

단어 "listen"과 "silent"는 애너그램입니다

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

단어 "stone"과 "tones"는 애너그램입니다

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

단어는 자기 자신의 애너그램이 아닙니다

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

길이가 다른 단어는 애너그램이 아닙니다

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

같은 문자라도 개수가 다르면 애너그램이 아닙니다

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

단어 "anagram"과 "nagaram"는 애너그램입니다

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

길이가 같고 문자가 다른 두 단어는 애너그램이 아닙니다

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

두 빈 단어는 동일하므로 애너그램이 아닙니다

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

서로 다른 한 문자 두 개는 애너그램이 아닙니다

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

단어 "evil"과 "vile"는 애너그램입니다

```python
    def test10(self):
        self.assertEqual(is_anagram("evil", "vile"), True, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_anagram(first, second):
    if first == second:
        return False

    return sorted(first) == sorted(second)
```
