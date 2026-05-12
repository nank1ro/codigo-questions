---
language: swift
exerciseType: 1
difficulty: 3
title: 闰年
---

# --description--

一个日历年恰好有365.25天。但是，这最终会导致混淆，因为人类通常按整除1来计数，而不是用小数点。因此，为了避免后者，人们决定将每四年周期中的所有0.25天累加起来，给那一年366天（包括2月29日作为闰日），并称之为__闰年__。四年周期中的其他三年只有365天，__不是闰年__。

# --instructions--

在这个挑战中，我们将提升难度，你需要在不使用 `Date` 类、`switch` 语句、__if 代码块__、__if-else 代码块__或__三元运算符__（`x ? a : b`）以及逻辑运算符 __AND__（`&&`）和 __OR__（`||`）的情况下判断是否为闰年，但可以使用 __NOT__（`!`）运算符。

如果是闰年返回 `true`，否则返回 `false`。

函数调用示例：
```swift
print(leapYear(2000))
// prints true
```

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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

不允许使用 `Date`、`switch`、`if`、`else`、`&&`、`||` 或 `?`。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年份 `2016` 是闰年。

```swift
tryCatch(leapYear(2016) == true)
```

年份 `1996` 是闰年。

```swift
tryCatch(leapYear(1996) == true)
```

年份 `1600` 是闰年。

```swift
tryCatch(leapYear(1600) == true)
```

年份 `2020` 是闰年。

```swift
tryCatch(leapYear(2020) == true)
```

年份 `2000` 是闰年。

```swift
tryCatch(leapYear(2000) == true)
```

年份 `2008` 是闰年。

```swift
tryCatch(leapYear(2008) == true)
```

年份 `1521` 不是闰年。

```swift
tryCatch(leapYear(1521) == false)
```

年份 `1800` 不是闰年。

```swift
tryCatch(leapYear(1800) == false)
```

年份 `2007` 不是闰年。

```swift
tryCatch(leapYear(2007) == false)
```

年份 `2002` 不是闰年。

```swift
tryCatch(leapYear(2002) == false)
```

年份 `1979` 不是闰年。

```swift
tryCatch(leapYear(1979) == false)
```

年份 `2006` 不是闰年。

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
