---
language: python
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

The Luhn algorithm is a simple checksum used to validate identification numbers, such as credit card numbers.

Before checking a number, strip every space from the string. The string is valid only if what remains is longer than one character and the original string contains nothing but digits and spaces.

To run the check, start from the rightmost digit and move left, doubling every second digit. When doubling produces a number greater than 9, subtract 9 from it. Then sum all the digits: the number is valid only if the sum is divisible by 10.

For example, `"059"` gives `0`, then `5` doubled is `10` which becomes `1`, then `9`. Their sum is `10`, which is divisible by 10, so the number is valid.

# --instructions--

Write a function `is_valid` that takes a string and returns `True` when the number is valid, `False` otherwise.

- `"4539 3195 0343 6467"` passes the checksum, so the result is `True`.
- `"8273 1232 7352 0569"` fails the checksum, so the result is `False`.
- `"0"` is only one character long, so the result is `False`.
- `"055-444-285"` contains a character that is not a digit or a space, so the result is `False`.

Example of function call:
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

A single digit is not valid.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

A single digit with a leading space is not valid.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

The number `"059"` is valid.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

The number `"59"` is valid.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

The number `"055 444 285"` is valid.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

The number `"055 444 286"` is not valid.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

The number `"8273 1232 7352 0569"` is not valid.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

The number `"4539 3195 0343 6467"` is valid.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

The number `"1 2345 6789 1234 5678 9012"` is not valid.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

The number `"095 245 88"` is valid.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

A letter makes the number invalid.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

Dashes make the number invalid.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

A punctuation character makes the number invalid.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

Symbols make the number invalid.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

An empty string is not valid.

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
