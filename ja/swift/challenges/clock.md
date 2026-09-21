---
language: swift
exerciseType: 1
difficulty: 2
title: 時計
---

# --description--

24時間時計は、時刻を `HH:MM` の形で表します。真夜中の直後の `00:00` に始まり、次の真夜中の1分前の `23:59` で終わります。どちらの部分も常に2桁で書かれるため、午前11時9分は `11:09` と表示されます。

1日はちょうど1440分です。時計が `23:59` を過ぎると `00:00` に折り返して1日がまた始まり、逆に `00:00` より前へ巻き戻すと `23:59` に到達します。

# --instructions--

2つの整数 `hours` と `minutes` を受け取り、24時間時計の時刻を、両方の部分が2桁になるようゼロ埋めした文字列 `"HH:MM"` として返す関数 `clockTime` を書いてください。

例:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- どちらの数も、負の値や実際の時計が取りうる範囲を超える大きな値になることがあります。
- 合計分数を `hours * 60 + minutes` として求め、その合計を `0` から `1439` の範囲に折り返して、時計がどちらの方向にも巡るようにします。
- `clockTime(24, 0)` はちょうど1日なので、`"00:00"` と表示されます。

> HINT: omit the argument labels with the `_` (underscore)

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func clockTime(_ hours: Int, _ minutes: Int) -> String {
    
}
```

# --asserts--

Eight in the morning reads `08:00`

```swift
tryCatch(clockTime(8, 0) == "08:00")
```

Single digits are padded to two, so nine minutes past eleven reads `11:09`

```swift
tryCatch(clockTime(11, 9) == "11:09")
```

Exactly one full day of hours rolls over to `00:00`

```swift
tryCatch(clockTime(24, 0) == "00:00")
```

Minutes over 60 carry into the hours

```swift
tryCatch(clockTime(25, 160) == "03:40")
```

A negative hour winds the clock backwards past midnight

```swift
tryCatch(clockTime(-1, 15) == "23:15")
```

A negative minute count also winds the clock backwards

```swift
tryCatch(clockTime(0, -90) == "22:30")
```

More than a whole day backwards keeps rolling over

```swift
tryCatch(clockTime(-25, 0) == "23:00")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func clockTime(_ hours: Int, _ minutes: Int) -> String {
    // % keeps the sign of the left operand, so add a whole day before wrapping
    // again to land in 0..1439.
    let total = (((hours * 60 + minutes) % 1440) + 1440) % 1440

    return String(format: "%02d:%02d", total / 60, total % 60)
}
```
