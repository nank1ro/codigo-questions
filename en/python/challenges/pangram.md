---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

A pangram is a sentence that uses every letter of the English alphabet at least once. The best known example is "the quick brown fox jumps over the lazy dog", which fits all 26 letters into nine short words.

The check is case-insensitive, so `A` and `a` count as the same letter. Digits, punctuation and spaces are ignored: they are not letters, but they are not a reason to reject a sentence either.

# --instructions--

Write a function `is_pangram` that takes a sentence and returns `True` if the sentence is a pangram and `False` otherwise.

Examples:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- An empty sentence is not a pangram.
- Only the 26 letters from `a` to `z` count.

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

An empty sentence is not a pangram

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

The classic sentence "the quick brown fox jumps over the lazy dog" is a pangram

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

A sentence missing the letter `x` is not a pangram

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

The sentence "the five boxing wizards jump quickly" is a pangram

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

Underscores are ignored, so the sentence is still a pangram

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

Digits are ignored, so the sentence is still a pangram

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

Digits do not replace the letters `e`, `i` and `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

An uppercase sentence is a pangram too

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

Mixing the cases of the same half of the alphabet is not enough

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
