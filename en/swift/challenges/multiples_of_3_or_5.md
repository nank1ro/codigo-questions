---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# --instructions--

Write a function that finds the sum of all multiples of 3 or 5 below the given number.

Example of function call:
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

The sum of multiples of 3 or 5 below 10 must equal 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

The sum of multiples of 3 or 5 below 1000 must equal 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

The sum of multiples of 3 or 5 below 6987 must equal 11390208

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
