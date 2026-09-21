---
language: python
exerciseType: 1
difficulty: 3
title: 括号匹配
---

# --description--

包含代码、数学式或标记的文本中充满了括号，每个开括号都需要一个同类型的闭括号。当字符串中的括号两两配对，并像洋葱的层层外皮一样嵌套时，它就是平衡的：`{[()]}` 是平衡的，而 `{[(])}` 则不是，因为圆括号对在包含它的方括号对之前就闭合了。

这里有三对括号：圆括号 `()`、方括号 `[]` 和花括号 `{}`。字符串中的其他所有字符都会被忽略。闭括号必须闭合最近一个仍处于打开状态的括号，并且在字符串结束时不能有任何括号保持打开。

# --instructions--

编写一个函数 `is_balanced`，它接收一个字符串，当其中的所有括号都配对且正确嵌套时返回 `True`，否则返回 `False`。

示例：
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- 空字符串是平衡的。
- 不是括号的字符会被忽略。
- 闭括号必须与最近一个仍处于打开状态的括号配对。
- 字符串结束时不能有任何括号保持打开。

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

空字符串是平衡的

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

单独的一对圆括号是平衡的

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

三种括号对彼此嵌套是平衡的

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

括号与其他文本混在一起时依然是平衡的

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

并排摆放的括号对是平衡的

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

不含任何括号的字符串是平衡的

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

交叉的括号对不是平衡的

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

从未被闭合的开括号不是平衡的

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

出现在任何开括号之前的闭括号不是平衡的

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

字符串更深处的交叉括号对不是平衡的

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

结尾遗留的闭括号不是平衡的

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
