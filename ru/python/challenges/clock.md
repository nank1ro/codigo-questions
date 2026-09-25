---
language: python
exerciseType: 1
difficulty: 2
title: Часы
---

# --description--

24-часовые часы показывают время суток в формате `HH:MM`: отсчёт начинается с `00:00` сразу после полуночи и заканчивается `23:59` — за минуту до следующей полуночи. Обе части всегда записываются двумя цифрами, поэтому девять минут двенадцатого утра выглядят как `11:09`.

Целые сутки длятся 1440 минут. Как только часы проходят `23:59`, они переключаются на `00:00` и день начинается заново, а при переводе назад мимо `00:00` получается `23:59`.

# --instructions--

Напишите функцию `clock_time`, которая принимает два целых числа, `hours` и `minutes`, и возвращает показания 24-часовых часов в виде строки `"HH:MM"`, причём обе части дополнены до двух цифр.

Примеры:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Каждое из чисел может быть отрицательным или больше, чем допускают настоящие часы.
- Вычислите общее количество минут как `hours * 60 + minutes`, а затем заверните полученную сумму в диапазон от `0` до `1439`, чтобы часы переключались в обоих направлениях.
- `clock_time(24, 0)` — это ровно один день, поэтому получится `"00:00"`.

# --seed--

```python
def clock_time(hours, minutes):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Восемь часов утра — это `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

Одиночные цифры дополняются до двух, поэтому девять минут двенадцатого — это `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

Ровно одни полные сутки переключаются на `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

Минуты сверх 60 переходят в часы

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

Отрицательный час переводит часы назад мимо полуночи

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

Отрицательное количество минут тоже переводит часы назад

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

Больше целых суток назад — часы продолжают переключаться

```python
    def test_more_than_a_day_backwards(self):
        self.assertEqual(clock_time(-25, 0), "23:00", "--err-t7--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def clock_time(hours, minutes):
    # Оператор % в Python всегда берёт знак делителя, поэтому отрицательная
    # сумма уже заворачивается вперёд в диапазон 0..1439.
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
