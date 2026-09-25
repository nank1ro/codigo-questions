---
language: python
exerciseType: 1
difficulty: 3
title: Matching brackets
---

# --description--

Text that carries code, maths or markup is full of brackets, and every opening bracket needs a closing one of the same kind. A string is balanced when its brackets pair up and nest like the layers of an onion: `{[()]}` is balanced, while `{[(])}` is not, because the round pair is closed before the square pair it sits inside.

Three pairs count here: round `()`, square `[]` and curly `{}`. Every other character in the string is ignored. A closing bracket must close the most recently opened bracket that is still open, and when the string ends no bracket may be left open.

# --instructions--

Write a function `is_balanced` that takes a string and returns `True` when all the brackets in it are matched and properly nested, and `False` otherwise.

Examples:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- An empty string is balanced.
- Characters that are not brackets are ignored.
- A closing bracket must match the most recently opened bracket that is still open.
- No bracket may be left open when the string ends.

# --seed--

```python
def is_balanced(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

An empty string is balanced

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

A single pair of round brackets is balanced

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

The three kinds of pair nested inside each other are balanced

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Brackets mixed with other text are still balanced

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Pairs placed side by side are balanced

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

A string without any brackets is balanced

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

A crossed pair is not balanced

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

An opening bracket that is never closed is not balanced

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

A closing bracket before any opening one is not balanced

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Crossed pairs deeper in the string are not balanced

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

A closing bracket left over at the end is not balanced

```python
    def test11(self):
        self.assertEqual(is_balanced("())"), False, "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
```
