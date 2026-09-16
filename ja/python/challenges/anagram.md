---
language: python
exerciseType: 1
difficulty: 2
title: アナグラム
---

# --description--

アナグラムとは、一方の単語を並べ替えるともう一方になるような2つの単語のことです。使っている文字がまったく同じで、どの文字も同じ回数だけ現れ、順序だけが異なります。`listen` と `silent` はアナグラムであり、`stone` と `tones` もアナグラムです。

単語がそれ自身のアナグラムになることはありません。2つの単語がまったく同じであれば、何も並べ替えられていないため、答えは `False` です。両方の単語は小文字で与えられ、`a` から `z` の文字だけを含みます。

# --instructions--

2つの単語 `first` と `second` を受け取り、互いにアナグラムであれば `True` を、そうでなければ `False` を返す関数 `is_anagram` を書いてください。

例:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- まったく同じ単語どうしはアナグラムではありません。
- 長さが異なる単語がアナグラムになることはありません。
- すべての文字は、両方の単語で同じ回数だけ現れなければなりません。

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

単語 "listen" と "silent" はアナグラムである

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

単語 "stone" と "tones" はアナグラムである

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

単語はそれ自身のアナグラムではない

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

長さが異なる単語はアナグラムではない

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

同じ文字でも出現回数が異なればアナグラムではない

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

単語 "anagram" と "nagaram" はアナグラムである

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

同じ長さでも文字が異なる2つの単語はアナグラムではない

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

2つの空の単語は同一であるため、アナグラムではない

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

異なる1文字どうしはアナグラムではない

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

単語 "evil" と "vile" はアナグラムである

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
