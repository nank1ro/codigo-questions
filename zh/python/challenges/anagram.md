---
language: python
exerciseType: 1
difficulty: 2
title: 变位词
---

# --description--

如果一个单词是另一个单词的重新排列，那么这两个单词就互为变位词：它们使用的字母完全相同，每个字母出现的次数也相同，只是顺序不同。`listen` 和 `silent` 是变位词，`stone` 和 `tones` 也是变位词。

一个单词永远不会是它自身的变位词。如果两个单词完全相同，就没有任何东西被重新排列，所以答案是 `False`。两个单词都以小写形式给出，并且只包含从 `a` 到 `z` 的字母。

# --instructions--

编写一个函数 `is_anagram`，它接收两个单词 `first` 和 `second`，当它们互为变位词时返回 `True`，否则返回 `False`。

示例：
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- 两个完全相同的单词不是变位词。
- 长度不同的单词永远不会是变位词。
- 每个字母在两个单词中出现的次数必须相同。

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

单词 "listen" 和 "silent" 互为变位词

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

单词 "stone" 和 "tones" 互为变位词

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

一个单词不是它自身的变位词

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

长度不同的单词不是变位词

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

字母相同但出现次数不同则不是变位词

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

单词 "anagram" 和 "nagaram" 互为变位词

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

长度相同但字母不同的两个单词不是变位词

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

两个空单词是完全相同的，所以它们不是变位词

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

两个不同的单个字母不是变位词

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

单词 "evil" 和 "vile" 互为变位词

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
