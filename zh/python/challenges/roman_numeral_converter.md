---
language: python
exerciseType: 1
difficulty: 3
title: 罗马数字转换器
---

# --description--

创建一个函数，接收一个正整数作为参数，返回包含该整数的罗马数字表示的字符串。现代罗马数字的书写方式是分别表示每个数位，从最左边的数位开始，跳过值为零的数位。

# --instructions--

示例：
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- 所有罗马数字应以大写形式返回。
- 此表示法能表示的最大数字是3,999。

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

数字 `2` 必须等于 `II`

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

数字 `12` 必须等于 `XII`

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

数字 `16` 必须等于 `XVI`

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

数字 `44` 必须等于 `XLIV`

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

数字 `68` 必须等于 `LXVIII`

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

数字 `400` 必须等于 `CD`

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

数字 `798` 必须等于 `DCCXCVIII`

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

数字 `1000` 必须等于 `M`

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

数字 `3999` 必须等于 `MMMCMXCIX`

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

数字 `649` 必须等于 `DCXLIX`

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

数字 `1666` 必须等于 `MDCLXVI`

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
