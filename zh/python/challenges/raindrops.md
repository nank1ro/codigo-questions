---
language: python
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与特定可能因数对应的雨滴声的字符串。
因数是能整除另一个数字且没有余数的数字。
测试一个数字是否是另一个数字的因数最简单的方法是使用取模运算。
雨滴的规则如下：

- 如果3是因数，将 'Pling' 添加到结果中。
- 如果5是因数，将 'Plang' 添加到结果中。
- 如果7是因数，将 'Plong' 添加到结果中。
- 如果3、5或7都不是因数，结果应为该数字本身。

# --instructions--

编写一个函数，返回正确的字符串，示例：

- 28有因数7，但没有3或5，所以结果是 `"Plong"`。
- 30同时有因数3和5，但没有7，所以结果是 `"PlingPlang"`。
- 34不能被3、5或7整除，所以结果是 `"34"`。

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

1的声音是 "1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

3的声音是 "Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

5的声音是 "Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

7的声音是 "Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

6的声音是 "Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

8的声音是 "8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

9的声音是 "Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

10的声音是 "Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

14的声音是 "Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

15的声音是 "PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

21的声音是 "PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

25的声音是 "Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

27的声音是 "Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

35的声音是 "PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

49的声音是 "Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

52的声音是 "52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

105的声音是 "PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

3125的声音是 "Plang"

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
