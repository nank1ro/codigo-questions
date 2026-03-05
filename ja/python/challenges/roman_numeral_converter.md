---
language: python
exerciseType: 1
difficulty: 3
title: ローマ数字変換器
---

# --description--

正の整数をパラメータとして受け取り、その整数のローマ数字表現を含む文字列を返す関数を作成してください。現代のローマ数字は、各桁を左端の桁から個別に表現し、値がゼロの桁はスキップして書きます。

# --instructions--

例：
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- すべてのローマ数字は大文字で返してください。
- この表記法で表現できる最大の数は3,999です。

# --seed--

```python
def convert_to_roman(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

数`2`は`II`に等しくなければなりません

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

数`12`は`XII`に等しくなければなりません

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

数`16`は`XVI`に等しくなければなりません

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

数`44`は`XLIV`に等しくなければなりません

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

数`68`は`LXVIII`に等しくなければなりません

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

数`400`は`CD`に等しくなければなりません

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

数`798`は`DCCXCVIII`に等しくなければなりません

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

数`1000`は`M`に等しくなければなりません

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

数`3999`は`MMMCMXCIX`に等しくなければなりません

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

数`649`は`DCXLIX`に等しくなければなりません

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

数`1666`は`MDCLXVI`に等しくなければなりません

```python
    def test11(self):
        self.assertEqual(convert_to_roman(1666), "MDCLXVI", "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def convert_to_roman(n):
    result = ""

    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    for value, letter in values:
        while n >= value:
            result += letter
            n -= value

    return result
```
