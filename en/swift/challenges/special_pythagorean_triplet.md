---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a² + b² = c². There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product a × b × c.

# --instructions--

Write a function that finds the product a × b × c of the Pythagorean triplet where a + b + c = n.

Example of function call:
```swift
print(specialPythagoreanTriplet(12))
// prints 60
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
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --asserts--

The product of the Pythagorean triplet where a + b + c = 12 must equal 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

The product of the Pythagorean triplet where a + b + c = 1000 must equal 31875000

```swift
tryCatch(specialPythagoreanTriplet(1000) == 31875000)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
