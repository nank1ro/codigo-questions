---
language: python
exerciseType: 1
difficulty: 3
title: Високосный год
---

# --description--

В календарном году ровно 365,25 дней. Но со временем это приведёт к путанице, потому что люди обычно считают целыми числами, а не десятичными дробями. Поэтому, чтобы избежать этого, было решено складывать все 0,25 дня каждые четыре года и давать этому году 366 дней (включая 29 февраля как дополнительный день), называя его __високосным годом__. Остальные три года в четырёхлетнем цикле содержат только 365 дней и __не являются високосными__.

# --instructions--

В этом задании мы выведем задачу на новый уровень: вам нужно определить, является ли год високосным, без использования класса `datetime`, __блоков if__, __блоков if-elif__ или __условных выражений__ (`a if b else c`), а также логических операторов __И__ (`and`) и __ИЛИ__ (`or`), за исключением оператора __НЕ__ (`not`).

Верните `True`, если год високосный, `False` в противном случае.

Пример вызова функции:
```dart
print(leap_year(2000))
// prints true
```

# --seed--

```python
def leap_year(year):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Использование `month`, `day`, `if`, `else`, `elif`, `and`, `or` запрещено.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Год `2016` является високосным.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

Год `1996` является високосным.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

Год `1600` является високосным.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

Год `2020` является високосным.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

Год `2000` является високосным.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

Год `2008` является високосным.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

Год `1521` не является високосным.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

Год `1800` не является високосным.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

Год `2007` не является високосным.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

Год `2002` не является високосным.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

Год `1979` не является високосным.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

Год `2006` не является високосным.

```python
    def test12(self):
        self.assertEqual(leap_year(2006), False, "--err-t12--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def leap_year(year):
    return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0))
```

```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```
