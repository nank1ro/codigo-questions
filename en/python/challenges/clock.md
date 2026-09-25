---
language: python
exerciseType: 1
difficulty: 2
title: Clock
---

# --description--

A 24-hour clock shows the time of day as `HH:MM`, starting at `00:00` just after midnight and ending at `23:59` one minute before the next midnight. Both parts are always written with two digits, so nine minutes past eleven in the morning reads `11:09`.

A whole day lasts 1440 minutes. Once the clock passes `23:59` it rolls over to `00:00` and starts the day again, and winding it backwards past `00:00` lands on `23:59`.

# --instructions--

Write a function `clock_time` that takes two whole numbers, `hours` and `minutes`, and returns the reading of a 24-hour clock as the string `"HH:MM"`, with both parts padded to two digits.

Examples:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Either number may be negative, or larger than a real clock allows.
- Work out the total number of minutes as `hours * 60 + minutes`, then wrap that total into the range `0` to `1439` so the clock rolls over in both directions.
- `clock_time(24, 0)` is exactly one day, so it reads `"00:00"`.

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

Eight in the morning reads `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

Single digits are padded to two, so nine minutes past eleven reads `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

Exactly one full day of hours rolls over to `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

Minutes over 60 carry into the hours

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

A negative hour winds the clock backwards past midnight

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

A negative minute count also winds the clock backwards

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

More than a whole day backwards keeps rolling over

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
    # Python's % always takes the sign of the divisor, so a negative total
    # already wraps forward into 0..1439.
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
