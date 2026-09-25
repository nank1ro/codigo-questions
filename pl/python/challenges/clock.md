---
language: python
exerciseType: 1
difficulty: 2
title: Zegar
---

# --description--

Zegar 24-godzinny pokazuje porę dnia jako `HH:MM`, zaczynając od `00:00` tuż po północy i kończąc na `23:59`, minutę przed kolejną północą. Obie części są zawsze zapisywane dwiema cyframi, więc dziewięć minut po jedenastej rano to wskazanie `11:09`.

Cały dzień trwa 1440 minut. Gdy zegar przekroczy `23:59`, przewija się na `00:00` i zaczyna dzień od nowa, a przekręcenie go wstecz za `00:00` daje `23:59`.

# --instructions--

Napisz funkcję `clock_time`, która przyjmuje dwie liczby całkowite, `hours` i `minutes`, i zwraca wskazanie zegara 24-godzinnego jako napis `"HH:MM"`, przy czym obie części są uzupełnione do dwóch cyfr.

Przykłady:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Każda z liczb może być ujemna lub większa, niż pozwala prawdziwy zegar.
- Oblicz całkowitą liczbę minut jako `hours * 60 + minutes`, a następnie zawiń tę sumę do zakresu od `0` do `1439`, żeby zegar przewijał się w obu kierunkach.
- `clock_time(24, 0)` to dokładnie jeden dzień, więc wskazanie to `"00:00"`.

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

Ósma rano to wskazanie `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

Pojedyncze cyfry są uzupełniane do dwóch, więc dziewięć minut po jedenastej to wskazanie `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

Dokładnie jeden pełny dzień godzin przewija się na `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

Minuty powyżej 60 przenoszą się na godziny

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

Ujemna godzina przekręca zegar wstecz za północ

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

Ujemna liczba minut również przekręca zegar wstecz

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

Więcej niż cały dzień wstecz nadal przewija zegar

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
    # % w Pythonie zawsze przyjmuje znak dzielnika, więc ujemna suma zostaje
    # od razu zawinięta do przodu do zakresu 0..1439.
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
