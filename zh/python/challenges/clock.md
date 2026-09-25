---
language: python
exerciseType: 1
difficulty: 2
title: 时钟
---

# --description--

24 小时制时钟以 `HH:MM` 的形式显示一天中的时间，从午夜刚过的 `00:00` 开始，到下一个午夜前一分钟的 `23:59` 结束。两部分始终写成两位数字，所以上午十一点零九分显示为 `11:09`。

一整天共有 1440 分钟。时钟一旦走过 `23:59` 就会回到 `00:00` 重新开始一天，而向后拨过 `00:00` 则会落在 `23:59`。

# --instructions--

编写一个函数 `clock_time`，它接收两个整数 `hours` 和 `minutes`，并返回 24 小时制时钟的读数，即字符串 `"HH:MM"`，两部分都补足成两位数字。

示例：
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- 两个数都可能是负数，也可能大于真实时钟所允许的范围。
- 先按 `hours * 60 + minutes` 算出总分钟数，再把这个总数折回 `0` 到 `1439` 的范围内，让时钟向两个方向都能回绕。
- `clock_time(24, 0)` 正好是一天，所以读数是 `"00:00"`。

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

早上八点显示为 `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

个位数字会补足成两位，所以十一点零九分显示为 `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

正好一整天的小时会回绕到 `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

超过 60 的分钟数会进位到小时

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

负的小时数会把时钟向后拨过午夜

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

负的分钟数同样会把时钟向后拨

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

向后超过一整天也会继续回绕

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
    # Python 的 % 总是取除数的符号，所以负的总数
    # 已经向前回绕到 0..1439。
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
