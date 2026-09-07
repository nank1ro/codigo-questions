---
language: swift
exerciseType: 1
difficulty: 1
title: 二乗の和と和の二乗の差
---

# --description--

最初の10個の自然数の二乗の和は 1² + 2² + ... + 10² = 385 です。最初の10個の自然数の和の二乗は (1 + 2 + ... + 10)² = 55² = 3025 です。したがって、二乗の和と和の二乗の差は 3025 − 385 = 2640 です。

# --instructions--

最初のn個の自然数について、和の二乗と二乗の和の差を求める関数を書いてください。

関数呼び出しの例:
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

n=10のときの二乗の和と和の二乗の差は2640でなければなりません

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

n=20のときの二乗の和と和の二乗の差は41230でなければなりません

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

n=100のときの二乗の和と和の二乗の差は25164150でなければなりません

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
