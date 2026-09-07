---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# --instructions--

Write a function that returns the smallest positive number that is evenly divisible by all numbers from 1 to n.

Example of function call:
```swift
print(smallestMultiple(10))
// prints 2520
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
func smallestMultiple(_ n: Int) -> Int {

}
```

# --asserts--

The smallest multiple of 1 to 5 must equal 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

The smallest multiple of 1 to 10 must equal 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

The smallest multiple of 1 to 20 must equal 232792560

```swift
tryCatch(smallestMultiple(20) == 232792560)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    return (1...n).reduce(1) { lcm($0, $1) }
}
```
