---
language: python
exerciseType: 1
difficulty: 2
title: Caesar cipher
---

# --description--

Julius Caesar protected his private letters with one of the oldest tricks in cryptography: he replaced every letter of a message with the letter a fixed number of places further along the alphabet. With a shift of 3, `a` becomes `d`, `b` becomes `e` and `c` becomes `f`.

The alphabet behaves like a circle, so the letters at the end wrap back to the start: with a shift of 3, `x` becomes `a`, `y` becomes `b` and `z` becomes `c`.

Anything that is not a letter, such as a space, a comma, an exclamation mark or a digit, travels through the cipher untouched.

# --instructions--

Write a function `caesar_cipher` that takes a message `text` and a whole number `shift`, and returns the encoded message.

Examples:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- The message is always lowercase, so you never have to deal with uppercase letters.
- Characters that are not letters keep their place and their value.
- The shift is never negative. A shift of `0` leaves the message unchanged, and so does a shift of `26`.

# --seed--

```python
def caesar_cipher(text, shift):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

A shift of 3 turns "hello" into "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

The end of the alphabet wraps around, so "xyz" becomes "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

A shift of 0 leaves the message unchanged

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

A shift of 26 is a full turn of the alphabet, so the message is unchanged

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

Punctuation and spaces pass through unchanged

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

An empty message stays empty

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Spaces between single letters are preserved

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Digits are not shifted, even with a shift of 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

A shift of 13 encodes a whole sentence

```python
    def test9(self):
        self.assertEqual(caesar_cipher("the quick brown fox jumps over the lazy dog", 13), "gur dhvpx oebja sbk whzcf bire gur ynml qbt", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
        else:
            result += char

    return result
```
