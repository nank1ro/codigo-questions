---
language: python
exerciseType: 1
difficulty: 1
title: コラッツの予想
---

# --description--

コラッツの予想は、任意の正の整数`n`から始めて、1つの単純な規則を繰り返します。`n`が偶数ならそれを半分にし、`n`が奇数なら`3n + 1`で置き換えます。いずれ数列は1に到達します。

例えば、16から始めると数列は`16 -> 8 -> 4 -> 2 -> 1`となり、4ステップかかります。

これが常に起こると証明した人はまだいませんが、これまでテストされたすべての数で成り立っています。

# --instructions--

正の整数`n`を受け取り、1に到達するまでに必要なステップ数を返す関数`collatz_steps`を書いてください。

`collatz_steps(1)`は0になります。1はすでに数列の終わりだからです。`collatz_steps(12)`は9、`collatz_steps(27)`は111です。

# --seed--

```python
def collatz_steps(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`collatz_steps(1)`は、1がすでに数列の終わりであるため、0を返すべきです。

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)`は1を返すべきです。

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)`は8を返すべきです。

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)`は16を返すべきです。

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)`は4を返すべきです。

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)`は9を返すべきです。

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)`は111を返すべきです。

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)`は118を返すべきです。

```python
    def test8(self):
        self.assertEqual(collatz_steps(97), 118, "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def collatz_steps(n):
    value = n
    steps = 0
    while value != 1:
        value = value // 2 if value % 2 == 0 else 3 * value + 1
        steps += 1
    return steps
```
