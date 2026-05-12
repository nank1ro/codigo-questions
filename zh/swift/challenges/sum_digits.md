---
language: swift
exerciseType: 1
difficulty: 1
title: 数字之和
---

# --description--

给定一个整数 `N`。
编写一个程序来计算 N 的所有数字之和

# --instructions--

返回 `N` 的各位数字之和。
> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
```swift
print(sumDigits(28))
// prints 10
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
func sumDigits() {

}
```

# --asserts--

12345 的各位数字之和是 15

```swift
tryCatch(sumDigits(12345) == 15)
```

57253 的各位数字之和是 22

```swift
tryCatch(sumDigits(57253) == 22)
```

122 的各位数字之和是 5

```swift
tryCatch(sumDigits(122) == 5)
```

91979997 的各位数字之和是 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

2147483647 的各位数字之和是 46

```swift
tryCatch(sumDigits(2147483647) == 46)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumDigits(_ num: Int) -> Int {
    var n = num
    var result = 0
    while n > 0 {
        result += n % 10
        n = Int(n / 10)
    }
    return result
}
```

