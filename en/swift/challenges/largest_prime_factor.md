---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

The prime factors of 13195 are 5, 7, 13 and 29. The largest prime factor of 13195 is 29.

# --instructions--

Write a function that returns the largest prime factor of the given number.

Example of function call:
```swift
print(largestPrimeFactor(13195))
// prints 29
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
func largestPrimeFactor(_ number: Int) -> Int {

}
```

# --asserts--

The largest prime factor of 2 must equal 2

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

The largest prime factor of 13195 must equal 29

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

The largest prime factor of 600851475143 must equal 6857

```swift
tryCatch(largestPrimeFactor(600851475143) == 6857)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func largestPrimeFactor(_ number: Int) -> Int {
    var n = number
    var largest = 1
    var factor = 2
    while factor * factor <= n {
        while n % factor == 0 {
            largest = factor
            n /= factor
        }
        factor += 1
    }
    if n > 1 {
        largest = n
    }
    return largest
}
```
