---
language: python
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

Luhn 알고리즘은 신용카드 번호와 같은 식별 번호를 검증하는 데 사용되는 간단한 체크섬입니다.

수를 검사하기 전에 문자열에서 모든 공백을 제거합니다. 남은 부분이 한 문자보다 길고 원래 문자열이 숫자와 공백만을 담고 있을 때만 그 문자열은 유효합니다.

검사를 수행하려면 가장 오른쪽 자릿수부터 시작하여 왼쪽으로 이동하면서 한 칸 건너있는 자릿수마다 2배를 합니다. 2배한 값이 9보다 크면 9를 뺍니다. 그다음 모든 자릿수를 더합니다. 이 합계가 10으로 나누어떨어질 때만 그 수는 유효합니다.

예를 들어 `"059"`는 `0`이고, 그다음 `5`를 2배한 `10`은 `1`이 되며, 마지막은 `9`입니다. 이들의 합은 `10`이고 10으로 나누어떨어지므로 이 수는 유효합니다.

# --instructions--

문자열을 받아 수가 유효하면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `is_valid`를 작성하세요.

- `"4539 3195 0343 6467"`은 체크섬을 통과하므로 결과는 `True`입니다.
- `"8273 1232 7352 0569"`는 체크섬을 통과하지 못하므로 결과는 `False`입니다.
- `"0"`은 길이가 한 문자뿐이므로 결과는 `False`입니다.
- `"055-444-285"`에는 숫자나 공백이 아닌 문자가 포함되어 있으므로 결과는 `False`입니다.

함수 호출 예시:
```python
print(is_valid("095 245 88"))
# prints True
```

# --seed--

```python
def is_valid(value):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

한 자리 숫자는 유효하지 않습니다.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

앞에 공백이 있는 한 자리 숫자는 유효하지 않습니다.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

숫자 `"059"`는 유효합니다.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

숫자 `"59"`는 유효합니다.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

숫자 `"055 444 285"`는 유효합니다.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

숫자 `"055 444 286"`은 유효하지 않습니다.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

숫자 `"8273 1232 7352 0569"`는 유효하지 않습니다.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

숫자 `"4539 3195 0343 6467"`은 유효합니다.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

숫자 `"1 2345 6789 1234 5678 9012"`는 유효하지 않습니다.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

숫자 `"095 245 88"`는 유효합니다.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

영문자가 있으면 숫자는 유효하지 않습니다.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

대시가 있으면 숫자는 유효하지 않습니다.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

문장 부호가 있으면 숫자는 유효하지 않습니다.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

기호가 있으면 숫자는 유효하지 않습니다.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

빈 문자열은 유효하지 않습니다.

```python
    def test_an_empty_string_is_not_valid(self):
        self.assertEqual(is_valid(""), False, "--err-t15--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_valid(value):
    total = 0
    count = 0
    for char in reversed(value):
        if char == ' ':
            continue
        if char < '0' or char > '9':
            return False
        digit = int(char)
        if count % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        count += 1
    return count > 1 and total % 10 == 0
```
