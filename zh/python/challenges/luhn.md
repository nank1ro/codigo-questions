---
language: python
exerciseType: 1
difficulty: 2
title: Luhn 校验和
---

# --description--

Luhn 算法是一种简单的校验和，用于验证身份识别号码，例如信用卡号。

在检查一个号码之前，先去掉字符串中的所有空格。只有当剩下的部分长度超过一个字符，并且原始字符串只包含数字和空格时，该字符串才是有效的。

执行检查时，从最右边的数字开始向左移动，将每隔一位的数字加倍。当加倍后得到大于 9 的数时，将其减去 9。然后把所有数字相加：只有当总和能被 10 整除时，该号码才有效。

例如，`"059"` 得到 `0`，然后 `5` 加倍为 `10`，它变成 `1`，再是 `9`。它们的和是 `10`，能被 10 整除，所以这个号码是有效的。

# --instructions--

编写一个函数 `is_valid`，它接收一个字符串，当号码有效时返回 `True`，否则返回 `False`。

- `"4539 3195 0343 6467"` 通过校验和，所以结果是 `True`。
- `"8273 1232 7352 0569"` 未通过校验和，所以结果是 `False`。
- `"0"` 只有一个字符长，所以结果是 `False`。
- `"055-444-285"` 包含既不是数字也不是空格的字符，所以结果是 `False`。

函数调用示例：
```python
print(is_valid("095 245 88"))
# 打印 True
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

单个数字是无效的。

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

前面带一个空格的单个数字是无效的。

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

号码 `"059"` 是有效的。

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

号码 `"59"` 是有效的。

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

号码 `"055 444 285"` 是有效的。

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

号码 `"055 444 286"` 是无效的。

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

号码 `"8273 1232 7352 0569"` 是无效的。

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

号码 `"4539 3195 0343 6467"` 是有效的。

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

号码 `"1 2345 6789 1234 5678 9012"` 是无效的。

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

号码 `"095 245 88"` 是有效的。

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

字母会使号码无效。

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

短横线会使号码无效。

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

标点符号字符会使号码无效。

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

符号会使号码无效。

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

空字符串是无效的。

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
