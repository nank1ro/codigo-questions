---
language: python
exerciseType: 1
difficulty: 1
title: 雨粒
---

# --description--

あなたの課題は、数値を特定の潜在的な因数に対応する雨粒の音を含む文字列に変換することです。
因数とは、別の数を割り切れる数で、余りが残りません。
ある数が別の数の因数かどうかをテストする最も簡単な方法は、剰余演算を使用することです。
雨粒のルールは次のとおりです：

- 3を因数に持つ場合、結果に'Pling'を追加します。
- 5を因数に持つ場合、結果に'Plang'を追加します。
- 7を因数に持つ場合、結果に'Plong'を追加します。
- 3、5、7のいずれも因数に持たない場合、結果はその数の数字になります。

# --instructions--

正しい文字列を返す関数を書いてください。例：

- 28は7を因数に持ちますが、3や5は持たないので、結果は`"Plong"`になります。
- 30は3と5の両方を因数に持ちますが、7は持たないので、結果は`"PlingPlang"`になります。
- 34は3、5、7のいずれの因数も持たないので、結果は`"34"`になります。

# --seed--

```python
def convert(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

1の音は"1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

3の音は"Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

5の音は"Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

7の音は"Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

6の音は"Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

8の音は"8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

9の音は"Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

10の音は"Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

14の音は"Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

15の音は"PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

21の音は"PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

25の音は"Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

27の音は"Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

35の音は"PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

49の音は"Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

52の音は"52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

105の音は"PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

3125の音は"Plang"

```python
    def test_the_sound_for_3125(self):
        self.assertEqual(convert(3125), "Plang", "--err-t18--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def convert(number):
    result = ''
    if number % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'

    if not result:
        result = str(number)
    return result
```
