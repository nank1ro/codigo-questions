---
language: python
exerciseType: 1
difficulty: 2
title: Кодирование длин серий
---

# --description--

Кодирование длин серий — один из старейших приёмов сжатия: вместо того чтобы писать один и тот же символ снова и снова, вы записываете, сколько раз он повторяется, а затем сам символ.

Факсимильный аппарат, сканирующий почти пустую страницу, встречает длинные участки одинаковых пикселей, поэтому ряд из двенадцати `W` передаётся по линии как гораздо более короткое `12W`. Когда символ встречается лишь однажды, считать его незачем, поэтому он копируется сам по себе.

# --instructions--

Напишите функцию `encode_run`, которая принимает строку `text` и возвращает её закодированное представление.

Каждая серия одного и того же символа, повторённого два или более раз, превращается в длину серии, записанную в десятичном виде, за которой следует сам символ. Серия длины один копируется как одиночный символ, без числа перед ним.

Примеры:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Текст содержит только заглавные буквы от `A` до `Z` и пробелы.
- Серия длиннее девяти символов записывается своим полным десятичным количеством, поэтому двенадцать `W` превращаются в `12W`, но никогда в `9W3W`.
- Пробелы — обычные символы: они считаются и кодируются точно так же, как буквы.
- Пустая строка кодируется в пустую строку.

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Пустая строка кодируется в пустую строку

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Одиночный символ копируется без изменений

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Строка без повторов проходит через кодирование без изменений

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Серия из двух символов превращается в число, за которым следует символ

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

Смешанный пример "AABCCCDEEEE" превращается в "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Серия из двенадцати записывается своим полным десятичным количеством, поэтому результат начинается с "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Серии пробелов кодируются точно так же, как серии букв

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Серия из десяти записывается как "10A", но никогда как две более короткие серии

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Чередующиеся одиночные символы копируются без изменений

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
