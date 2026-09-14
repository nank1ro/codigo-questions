---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

全字母句是指至少使用一次英文字母表中每个字母的句子。最著名的例子是 "the quick brown fox jumps over the lazy dog"，它把全部 26 个字母装进了九个短单词里。

检查不区分大小写，因此 `A` 和 `a` 算作同一个字母。数字、标点和空格会被忽略：它们不是字母，但也不构成拒绝一个句子的理由。

# --instructions--

编写一个函数 `is_pangram`，它接收一个句子，如果该句子是全字母句则返回 `True`，否则返回 `False`。

示例：
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- 空句子不是全字母句。
- 只有从 `a` 到 `z` 的 26 个字母才算数。

# --seed--

```python
def is_pangram(sentence):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

空句子不是全字母句

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

经典句子 "the quick brown fox jumps over the lazy dog" 是全字母句

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

缺少字母 `x` 的句子不是全字母句

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

句子 "the five boxing wizards jump quickly" 是全字母句

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

下划线会被忽略，所以这个句子仍然是全字母句

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

数字会被忽略，所以这个句子仍然是全字母句

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

数字不能代替字母 `e`、`i` 和 `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

全大写的句子也是全字母句

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

混合字母表同一半部分的大小写还不够

```python
    def test9(self):
        self.assertEqual(is_pangram("abcdefghijklm ABCDEFGHIJKLM"), False, "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if "a" <= char <= "z":
            letters.add(char)

    return len(letters) == 26
```
