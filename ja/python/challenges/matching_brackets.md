---
language: python
exerciseType: 1
difficulty: 3
title: 括弧の対応
---

# --description--

コードや数式、マークアップを含むテキストには括弧が数多く登場し、開き括弧にはどれも同じ種類の閉じ括弧が必要です。括弧が対をなして玉ねぎの層のように入れ子になっていくとき、その文字列はバランスが取れています。`{[()]}` はバランスが取れていますが、`{[(])}` はバランスが取れていません。丸括弧の組が、その丸括弧が内側に収まっている角括弧の組よりも先に閉じられているからです。

ここで数えるのは、丸括弧 `()`、角括弧 `[]`、波括弧 `{}` の3組です。文字列内のそれ以外の文字はすべて無視されます。閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧を閉じなければならず、文字列が終わるときに開いたままの括弧が残っていてはいけません。

# --instructions--

文字列を受け取り、その中のすべての括弧が対応して正しく入れ子になっていれば `True` を、そうでなければ `False` を返す関数 `is_balanced` を書いてください。

例:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- 空の文字列はバランスが取れています。
- 括弧以外の文字は無視されます。
- 閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧と対応しなければなりません。
- 文字列が終わるとき、開いたままの括弧が残っていてはいけません。

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

空の文字列はバランスが取れている

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

丸括弧1組だけの文字列はバランスが取れている

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

3種類の組が互いに入れ子になった文字列はバランスが取れている

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

括弧が他のテキストと混ざっていてもバランスが取れている

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

組が横に並んでいてもバランスが取れている

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

括弧をまったく含まない文字列はバランスが取れている

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

交差した組はバランスが取れていない

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

閉じられないままの開き括弧はバランスが取れていない

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

開き括弧より先に来る閉じ括弧はバランスが取れていない

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

文字列の奥で交差した組はバランスが取れていない

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

最後に余った閉じ括弧はバランスが取れていない

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
