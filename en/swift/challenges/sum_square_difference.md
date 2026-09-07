---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385. The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# --instructions--

Write a function that finds the difference between the square of the sum and the sum of the squares of the first n natural numbers.

Example of function call:
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

The sum square difference for n=10 must equal 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

The sum square difference for n=20 must equal 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

The sum square difference for n=100 must equal 25164150

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
