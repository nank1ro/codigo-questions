---
language: python
exerciseType: 1
difficulty: 3
title: 闰年
---

# --description--

一个日历年恰好有365.25天。但最终，这会导致混淆，因为人类通常按整除1来计算，而不是用小数点。因此，为了避免这种情况，人们决定将每四年周期中的0.25天累加起来，使该年有366天（包括2月29日作为闰日），并称之为__闰年__。四年周期中的其他三年只有365天，__不是闰年__。

# --instructions--

在这个挑战中，我们将提升难度，你需要在不使用 `datetime` 类、__if 语句块__、__if-elif 语句块__或__条件表达式__（`a if b else c`）以及逻辑运算符 __AND__（`and`）和 __OR__（`or`）的情况下判断是否为闰年，但允许使用 __NOT__（`not`）运算符。

如果是闰年返回 `True`，否则返回 `False`。

函数调用示例：
```dart
print(leap_year(2000))
// prints true
```

# --seed--

```python
def leap_year(year):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

不允许使用 `month`、`day`、`if`、`else`、`elif`、`and`、`or`。

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年份 `2016` 是闰年。

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

年份 `1996` 是闰年。

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

年份 `1600` 是闰年。

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

年份 `2020` 是闰年。

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

年份 `2000` 是闰年。

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

年份 `2008` 是闰年。

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

年份 `1521` 不是闰年。

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

年份 `1800` 不是闰年。

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

年份 `2007` 不是闰年。

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

年份 `2002` 不是闰年。

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

年份 `1979` 不是闰年。

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

年份 `2006` 不是闰年。

```python
    def test12(self):
        self.assertEqual(leap_year(2006), False, "--err-t12--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def leap_year(year):
    return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0))
```

```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```
