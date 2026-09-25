---
language: swift
exerciseType: 1
difficulty: 2
title: 时钟
---

# --description--

24 小时制时钟以 `HH:MM` 的形式显示一天中的时间，从午夜刚过的 `00:00` 开始，到下一个午夜前一分钟的 `23:59` 结束。两部分始终写成两位数字，所以上午十一点零九分显示为 `11:09`。

一整天共有 1440 分钟。时钟一旦走过 `23:59` 就会回到 `00:00` 重新开始一天，而向后拨过 `00:00` 则会落在 `23:59`。

# --instructions--

编写一个函数 `clockTime`，它接收两个整数 `hours` 和 `minutes`，并返回 24 小时制时钟的读数，即字符串 `"HH:MM"`，两部分都补足成两位数字。

示例：
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- 两个数都可能是负数，也可能大于真实时钟所允许的范围。
- 先按 `hours * 60 + minutes` 算出总分钟数，再把这个总数折回 `0` 到 `1439` 的范围内，让时钟向两个方向都能回绕。
- `clockTime(24, 0)` 正好是一天，所以读数是 `"00:00"`。

> 提示：使用 `_`（下划线）省略参数标签

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

早上八点显示为 `08:00`

```swift
tryCatch(clockTime(8, 0) == "08:00")
```

个位数字会补足成两位，所以十一点零九分显示为 `11:09`

```swift
tryCatch(clockTime(11, 9) == "11:09")
```

正好一整天的小时会回绕到 `00:00`

```swift
tryCatch(clockTime(24, 0) == "00:00")
```

超过 60 的分钟数会进位到小时

```swift
tryCatch(clockTime(25, 160) == "03:40")
```

负的小时数会把时钟向后拨过午夜

```swift
tryCatch(clockTime(-1, 15) == "23:15")
```

负的分钟数同样会把时钟向后拨

```swift
tryCatch(clockTime(0, -90) == "22:30")
```

向后超过一整天也会继续回绕

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
    // % 会保留左操作数的符号，所以先加上一整天再
    // 回绕一次，落回 0..1439。
    let total = (((hours * 60 + minutes) % 1440) + 1440) % 1440

    return String(format: "%02d:%02d", total / 60, total % 60)
}
```
