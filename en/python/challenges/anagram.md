---
language: python
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Two words are anagrams when one is a rearrangement of the other: they use exactly the same letters, each letter the same number of times, only in a different order. `listen` and `silent` are anagrams, and so are `stone` and `tones`.

A word is never an anagram of itself. If the two words are exactly the same, nothing was rearranged, so the answer is `False`. Both words are given in lowercase and contain only the letters from `a` to `z`.

# --instructions--

Write a function `is_anagram` that takes two words, `first` and `second`, and returns `True` when they are anagrams of each other and `False` otherwise.

Examples:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Two identical words are not anagrams.
- Words of different lengths are never anagrams.
- Every letter must appear the same number of times in both words.

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

The words "listen" and "silent" are anagrams

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

The words "stone" and "tones" are anagrams

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

A word is not an anagram of itself

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Words of different lengths are not anagrams

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

The same letters in different amounts are not an anagram

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

The words "anagram" and "nagaram" are anagrams

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Two words of the same length with different letters are not anagrams

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Two empty words are identical, so they are not anagrams

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Two different single letters are not anagrams

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

The words "evil" and "vile" are anagrams

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
