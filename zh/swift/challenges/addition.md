---
language: swift
exerciseType: 1
difficulty: 1
title: 加法
---

# --description--

给定两个整数 `num1` 和 `num2`，编写一个程序将这两个数相加

# --instructions--

编写一个返回两个数之和的函数。
> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
```swift
print(addition(1, 2))
// prints 3
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
func addition() {
    
}
```

# --asserts--

1 和 3 的和必须等于 4

```swift
tryCatch(addition(1, 3) == 4)
```

200 和 210 的和必须等于 410

```swift
tryCatch(addition(200, 210) == 410)
```

15 和 35 的和必须等于 50

```swift
tryCatch(addition(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
