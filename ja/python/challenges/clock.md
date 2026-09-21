---
language: python
exerciseType: 1
difficulty: 2
title: 時計
---

# --description--

24時間時計は、時刻を `HH:MM` の形で表します。真夜中の直後の `00:00` に始まり、次の真夜中の1分前の `23:59` で終わります。どちらの部分も常に2桁で書かれるため、午前11時9分は `11:09` と表示されます。

1日はちょうど1440分です。時計が `23:59` を過ぎると `00:00` に折り返して1日がまた始まり、逆に `00:00` より前へ巻き戻すと `23:59` に到達します。

# --instructions--

2つの整数 `hours` と `minutes` を受け取り、24時間時計の時刻を、両方の部分が2桁になるようゼロ埋めした文字列 `"HH:MM"` として返す関数 `clock_time` を書いてください。

例:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- どちらの数も、負の値や実際の時計が取りうる範囲を超える大きな値になることがあります。
- 合計分数を `hours * 60 + minutes` として求め、その合計を `0` から `1439` の範囲に折り返して、時計がどちらの方向にも巡るようにします。
- `clock_time(24, 0)` はちょうど1日なので、`"00:00"` と表示されます。

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

午前8時は `08:00` と表示される

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

1桁の数字は2桁になるようゼロ埋めされるため、午前11時9分は `11:09` と表示される

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

ちょうど1日分の時間は `00:00` に折り返される

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

60を超える分は時間の方へ繰り越される

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

負の時間は時計を真夜中より前へ巻き戻す

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

負の分数も時計を巻き戻す

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

1日より多く巻き戻しても折り返しが続く

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
    # Pythonの%は常に除数の符号を取るため、負の合計は
    # そのまま0..1439の範囲に折り返されます。
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
