---
language: python
exerciseType: 1
difficulty: 2
title: Run-length encoding
---

# --description--

Run-length encoding is one of the oldest compression tricks there is: instead of writing the same character over and over, you write how many times it repeats and then the character itself.

A fax machine scanning a mostly blank page meets long stretches of identical pixels, so a row of twelve `W` travels down the line as the much shorter `12W`. When a character shows up only once there is nothing to gain from counting it, so it is copied across on its own.

# --instructions--

Write a function `encode_run` that takes a string `text` and returns its run-length encoded form.

Every run of the same character repeated two or more times becomes the length of the run written in decimal, followed by that character. A run of length one is copied as the single character, with no number in front of it.

Examples:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- The text contains only uppercase letters from `A` to `Z` and spaces.
- A run longer than nine characters uses its full decimal count, so twelve `W` become `12W` and never `9W3W`.
- Spaces are ordinary characters: they are counted and encoded exactly like letters.
- The empty string encodes to the empty string.

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

The empty string encodes to the empty string

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

A single character is copied as itself

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

A string with no repeats travels through unchanged

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

A run of two becomes the count followed by the character

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

The mixed example "AABCCCDEEEE" becomes "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

A run of twelve uses its full decimal count, so the result starts with "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Runs of spaces are encoded just like runs of letters

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

A run of ten is written as "10A", never as two shorter runs

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Single characters that alternate are all copied as themselves

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
