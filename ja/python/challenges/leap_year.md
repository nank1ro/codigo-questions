---
language: python
exerciseType: 1
difficulty: 3
title: うるう年
---

# --description--

暦年にはちょうど365.25日あります。しかし、最終的にこれは混乱を招きます。なぜなら、人間は通常、小数点ではなく1の正確な割り切りで数えるからです。そこで、後者を避けるために、4年周期ごとに0.25日をすべて合算し、その年を366日（閏日として2月29日を含む）とし、__うるう年__と呼ぶことが決められました。4年周期の残りの3年は365日のみで、__うるう年ではありません__。

# --instructions--

このチャレンジでは、`datetime`クラス、__ifブロック__、__if-elifブロック__、__条件式__（`a if b else c`）、論理演算子__AND__（`and`）および__OR__（`or`）を使用せずに、うるう年かどうかを判定してください。ただし、__NOT__（`not`）演算子は使用可能です。

うるう年の場合は`True`を、そうでない場合は`False`を返してください。

関数呼び出しの例：
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

`month`、`day`、`if`、`else`、`elif`、`and`、`or`の使用は許可されていません。

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年`2016`はうるう年です。

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

年`1996`はうるう年です。

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

年`1600`はうるう年です。

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

年`2020`はうるう年です。

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

年`2000`はうるう年です。

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

年`2008`はうるう年です。

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

年`1521`はうるう年ではありません。

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

年`1800`はうるう年ではありません。

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

年`2007`はうるう年ではありません。

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

年`2002`はうるう年ではありません。

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

年`1979`はうるう年ではありません。

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

年`2006`はうるう年ではありません。

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
