---
language: python
exerciseType: 1
difficulty: 3
title: 로마 숫자 변환기
---

# --description--

양의 정수를 매개변수로 받아 해당 정수의 로마 숫자 표현을 문자열로 반환하는 함수를 만드세요. 현대 로마 숫자는 각 자릿수를 따로 표현하며, 가장 왼쪽 자릿수부터 시작하고 값이 0인 자릿수는 건너뜁니다.

# --instructions--

예시:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- 모든 로마 숫자는 대문자로 반환해야 합니다.
- 이 표기법으로 표현할 수 있는 가장 큰 수는 3,999입니다.

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

숫자 `2`는 `II`와 같아야 합니다

```python
    def test1(self):
        self.assertEqual(convert_to_roman(2), "II", "--err-t1--")
```

숫자 `12`는 `XII`와 같아야 합니다

```python
    def test2(self):
        self.assertEqual(convert_to_roman(12), "XII", "--err-t2--")
```

숫자 `16`은 `XVI`와 같아야 합니다

```python
    def test3(self):
        self.assertEqual(convert_to_roman(16), "XVI", "--err-t3--")
```

숫자 `44`는 `XLIV`와 같아야 합니다

```python
    def test4(self):
        self.assertEqual(convert_to_roman(44), "XLIV", "--err-t4--")
```

숫자 `68`은 `LXVIII`과 같아야 합니다

```python
    def test5(self):
        self.assertEqual(convert_to_roman(68), "LXVIII", "--err-t5--")
```

숫자 `400`은 `CD`와 같아야 합니다

```python
    def test6(self):
        self.assertEqual(convert_to_roman(400), "CD", "--err-t6--")
```

숫자 `798`은 `DCCXCVIII`과 같아야 합니다

```python
    def test7(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII", "--err-t7--")
```

숫자 `1000`은 `M`과 같아야 합니다

```python
    def test8(self):
        self.assertEqual(convert_to_roman(1000), "M", "--err-t8--")
```

숫자 `3999`는 `MMMCMXCIX`와 같아야 합니다

```python
    def test9(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX", "--err-t9--")
```

숫자 `649`는 `DCXLIX`와 같아야 합니다

```python
    def test10(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX", "--err-t10--")
```

숫자 `1666`은 `MDCLXVI`와 같아야 합니다

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
