---
language: python
exerciseType: 1
difficulty: 2
title: Luhnチェックサム
---

# --description--

Luhnアルゴリズムは、クレジットカード番号などの識別番号を検証するために使われるシンプルなチェックサムです。

数をチェックする前に、文字列からすべてのスペースを取り除きます。残った部分が1文字より長く、元の文字列が数字とスペースのみを含んでいる場合にのみ、その文字列は有効です。

チェックを行うには、一番右の桁から始めて左へ進み、1つおきの桁を2倍していきます。2倍した結果が9より大きい数になった場合は、そこから9を引きます。次にすべての桁を合計します。その合計が10で割り切れる場合にのみ、数は有効です。

たとえば、`"059"`は`0`、次に`5`を2倍した`10`が`1`になり、そして`9`となります。合計は`10`で10で割り切れるので、この数は有効です。

# --instructions--

文字列を受け取り、数が有効な場合には`True`を、そうでない場合には`False`を返す関数`is_valid`を書いてください。

- `"4539 3195 0343 6467"`はチェックサムを満たすため、結果は`True`です。
- `"8273 1232 7352 0569"`はチェックサムを満たさないため、結果は`False`です。
- `"0"`は長さが1文字しかないため、結果は`False`です。
- `"055-444-285"`には数字でもスペースでもない文字が含まれているため、結果は`False`です。

関数呼び出しの例：
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

1桁の数字は有効ではありません。

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

先頭にスペースが付いた1桁の数字は有効ではありません。

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

数`"059"`は有効です。

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

数`"59"`は有効です。

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

数`"055 444 285"`は有効です。

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

数`"055 444 286"`は有効ではありません。

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

数`"8273 1232 7352 0569"`は有効ではありません。

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

数`"4539 3195 0343 6467"`は有効です。

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

数`"1 2345 6789 1234 5678 9012"`は有効ではありません。

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

数`"095 245 88"`は有効です。

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

英字が1つあるだけで数は無効になります。

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

ダッシュがあると数は無効になります。

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

句読点があると数は無効になります。

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

記号があると数は無効になります。

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

空の文字列は有効ではありません。

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
