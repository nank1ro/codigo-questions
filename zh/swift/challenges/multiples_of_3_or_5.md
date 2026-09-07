---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

如果列出 10 以下所有 3 或 5 的倍数，得到 3、5、6 和 9。这些倍数的总和为 23。

# --instructions--

编写一个函数，求所有小于给定数字的 3 或 5 的倍数之和。

函数调用示例：
```swift
print(multiplesOf3And5(10))
// prints 23
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
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --asserts--

10 以下 3 或 5 的倍数之和必须等于 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

1000 以下 3 或 5 的倍数之和必须等于 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

6987 以下 3 或 5 的倍数之和必须等于 11390208

```swift
tryCatch(multiplesOf3And5(6987) == 11390208)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
