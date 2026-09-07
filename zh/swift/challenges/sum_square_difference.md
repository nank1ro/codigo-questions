---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

前十个自然数的平方和为 1² + 2² + ... + 10² = 385。前十个自然数之和的平方为 (1 + 2 + ... + 10)² = 55² = 3025。因此，前十个自然数的平方和与和的平方之差为 3025 − 385 = 2640。

# --instructions--

编写一个函数，求前 n 个自然数的和的平方与平方和之差。

函数调用示例：
```swift
print(sumSquareDifference(10))
// prints 2640
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
func sumSquareDifference(_ n: Int) -> Int {

}
```

# --asserts--

n=10 时的平方差必须等于 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

n=20 时的平方差必须等于 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

n=100 时的平方差必须等于 25164150

```swift
tryCatch(sumSquareDifference(100) == 25164150)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumSquareDifference(_ n: Int) -> Int {
    let sumOfSquares = (1...n).reduce(0) { $0 + $1 * $1 }
    let sum = (1...n).reduce(0, +)
    let squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
