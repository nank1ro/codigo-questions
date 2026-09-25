---
language: python
exerciseType: 1
difficulty: 2
title: 游程编码
---

# --description--

游程编码是最古老的压缩技巧之一：与其把同一个字符一遍又一遍地写出来，不如先写下它重复的次数，再写下这个字符本身。

一台传真机在扫描一张大部分空白的页面时，会遇到长长的相同像素段，因此一排十二个 `W` 在线路上传输时会变成短得多的 `12W`。当某个字符只出现一次时，统计次数毫无意义，所以它会被单独原样复制过去。

# --instructions--

编写一个函数 `encode_run`，它接收一个字符串 `text`，并返回其游程编码后的形式。

每一段由同一字符重复两次或更多次构成的游程，都会变成该游程长度的十进制数字，后面跟上这个字符。长度为一的游程则只复制为单个字符，前面不带任何数字。

示例：
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- 文本只包含从 `A` 到 `Z` 的大写字母和空格。
- 超过九个字符的游程会使用完整的十进制计数，因此十二个 `W` 会变成 `12W`，而绝不会写成 `9W3W`。
- 空格是普通字符：它们的计数和编码方式与字母完全相同。
- 空字符串编码后仍是空字符串。

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

空字符串编码后仍是空字符串

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

单个字符会被原样复制

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

没有重复字符的字符串会原样通过，不做任何改变

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

长度为二的游程会变成计数后跟字符

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

混合示例 "AABCCCDEEEE" 变成 "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

长度为十二的游程会使用完整的十进制计数，因此结果以 "12W" 开头

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

空格游程的编码方式与字母游程完全相同

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

长度为十的游程会写成 "10A"，绝不会写成两个更短的游程

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

交替出现的单个字符都会被原样复制

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
