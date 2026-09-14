---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

パングラムとは、英語のアルファベットのすべての文字を少なくとも1回使う文のことです。最もよく知られている例は "the quick brown fox jumps over the lazy dog" で、26文字すべてを9つの短い単語に収めています。

この判定は大文字と小文字を区別しないため、`A` と `a` は同じ文字として数えます。数字、句読点、スペースは無視されます。これらは文字ではありませんが、文を却下する理由にもなりません。

# --instructions--

文を受け取り、その文がパングラムなら `True` を、そうでなければ `False` を返す関数 `is_pangram` を書いてください。

例:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- 空の文はパングラムではありません。
- `a` から `z` までの26文字だけが数えられます。

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

空の文はパングラムではない

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

古典的な文 "the quick brown fox jumps over the lazy dog" はパングラムである

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

文字 `x` が欠けている文はパングラムではない

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

文 "the five boxing wizards jump quickly" はパングラムである

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

アンダースコアは無視されるので、その文は依然としてパングラムである

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

数字は無視されるので、その文は依然としてパングラムである

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

数字は文字 `e`、`i`、`t` の代わりにはならない

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

大文字の文もパングラムである

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

アルファベットの同じ半分の大文字と小文字を混ぜるだけでは足りない

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
