---
language: python
exerciseType: 1
difficulty: 1
title: 빗방울
---

# --description--

주어진 숫자를 특정 인수에 해당하는 빗방울 소리가 포함된 문자열로 변환하는 것이 과제입니다.
인수란 나머지 없이 다른 숫자를 균등하게 나누는 숫자입니다.
숫자가 다른 숫자의 인수인지 테스트하는 가장 간단한 방법은 나머지 연산을 사용하는 것입니다.
빗방울의 규칙은 다음과 같습니다:

- 3을 인수로 가지면 결과에 'Pling'을 추가합니다.
- 5를 인수로 가지면 결과에 'Plang'을 추가합니다.
- 7을 인수로 가지면 결과에 'Plong'을 추가합니다.
- 3, 5, 7 중 어느 것도 인수로 가지지 않으면 결과는 숫자의 자릿수여야 합니다.

# --instructions--

올바른 문자열을 반환하는 함수를 작성하세요. 예시:

- 28은 7을 인수로 가지지만 3이나 5는 아니므로 결과는 `"Plong"`입니다.
- 30은 3과 5를 모두 인수로 가지지만 7은 아니므로 결과는 `"PlingPlang"`입니다.
- 34는 3, 5, 7의 인수가 아니므로 결과는 `"34"`입니다.

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

1의 소리는 "1"입니다

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

3의 소리는 "Pling"입니다

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

5의 소리는 "Plang"입니다

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

7의 소리는 "Plong"입니다

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

6의 소리는 "Pling"입니다

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

8의 소리는 "8"입니다

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

9의 소리는 "Pling"입니다

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

10의 소리는 "Plang"입니다

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

14의 소리는 "Plong"입니다

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

15의 소리는 "PlingPlang"입니다

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

21의 소리는 "PlingPlong"입니다

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

25의 소리는 "Plang"입니다

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

27의 소리는 "Pling"입니다

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

35의 소리는 "PlangPlong"입니다

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

49의 소리는 "Plong"입니다

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

52의 소리는 "52"입니다

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

105의 소리는 "PlingPlangPlong"입니다

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

3125의 소리는 "Plang"입니다

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
