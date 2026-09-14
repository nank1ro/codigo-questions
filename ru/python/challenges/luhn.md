---
language: python
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

Алгоритм Луна — это простая контрольная сумма, используемая для проверки идентификационных номеров, таких как номера кредитных карт.

Перед проверкой числа удалите из строки все пробелы. Строка является валидной, только если оставшееся длиннее одного символа, а исходная строка не содержит ничего, кроме цифр и пробелов.

Чтобы выполнить проверку, начните с крайней правой цифры и двигайтесь влево, удваивая каждую вторую цифру. Если удвоение даёт число больше 9, вычтите из него 9. Затем сложите все цифры: число является валидным, только если сумма делится на 10.

Например, `"059"` даёт `0`, затем `5` при удвоении превращается в `10`, которое становится `1`, затем `9`. Их сумма равна `10`, что делится на 10, поэтому число является валидным.

# --instructions--

Напишите функцию `is_valid`, которая принимает строку и возвращает `True`, если число является валидным, и `False` в противном случае.

- `"4539 3195 0343 6467"` проходит контрольную сумму, поэтому результат — `True`.
- `"8273 1232 7352 0569"` не проходит контрольную сумму, поэтому результат — `False`.
- `"0"` имеет длину всего один символ, поэтому результат — `False`.
- `"055-444-285"` содержит символ, который не является цифрой или пробелом, поэтому результат — `False`.

Пример вызова функции:
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

Одиночная цифра не является валидной.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

Одиночная цифра с ведущим пробелом не является валидной.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

Число `"059"` является валидным.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

Число `"59"` является валидным.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

Число `"055 444 285"` является валидным.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

Число `"055 444 286"` не является валидным.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

Число `"8273 1232 7352 0569"` не является валидным.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

Число `"4539 3195 0343 6467"` является валидным.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

Число `"1 2345 6789 1234 5678 9012"` не является валидным.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

Число `"095 245 88"` является валидным.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

Буква делает число невалидным.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

Дефисы делают число невалидным.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

Знак препинания делает число невалидным.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

Спецсимволы делают число невалидным.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

Пустая строка не является валидной.

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
