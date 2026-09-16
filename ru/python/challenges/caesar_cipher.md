---
language: python
exerciseType: 1
difficulty: 2
title: Шифр Цезаря
---

# --description--

Юлий Цезарь защищал свои личные письма одним из старейших приёмов криптографии: он заменял каждую букву сообщения буквой, отстоящей от исходной на фиксированное число позиций дальше по алфавиту. При сдвиге 3 `a` становится `d`, `b` становится `e`, а `c` становится `f`.

Алфавит замкнут в круг, поэтому буквы в его конце возвращаются к началу: при сдвиге 3 `x` становится `a`, `y` становится `b`, а `z` становится `c`.

Всё, что не является буквой — например, пробел, запятая, восклицательный знак или цифра, — проходит через шифр без изменений.

# --instructions--

Напишите функцию `caesar_cipher`, которая принимает сообщение `text` и целое число `shift`, и возвращает закодированное сообщение.

Примеры:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Сообщение всегда записано строчными буквами, поэтому вам никогда не придётся иметь дело с заглавными буквами.
- Символы, не являющиеся буквами, сохраняют свою позицию и своё значение.
- Сдвиг никогда не бывает отрицательным. Сдвиг `0` оставляет сообщение без изменений, как и сдвиг `26`.

# --seed--

```python
def caesar_cipher(text, shift):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Сдвиг 3 превращает "hello" в "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

Конец алфавита замыкается по кругу, поэтому "xyz" становится "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Сдвиг 0 оставляет сообщение без изменений

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Сдвиг 26 — это полный оборот алфавита, поэтому сообщение не меняется

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

Знаки препинания и пробелы проходят через шифр без изменений

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Пустое сообщение остаётся пустым

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Пробелы между отдельными буквами сохраняются

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Цифры не сдвигаются, даже при сдвиге 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Сдвиг 13 кодирует целое предложение

```python
    def test9(self):
        self.assertEqual(caesar_cipher("the quick brown fox jumps over the lazy dog", 13), "gur dhvpx oebja sbk whzcf bire gur ynml qbt", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
        else:
            result += char

    return result
```
