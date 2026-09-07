---
language: swift
exerciseType: 1
difficulty: 2
title: सबसे बड़ा अभाज्य गुणनखंड
---

# --description--

13195 के अभाज्य गुणनखंड 5, 7, 13 और 29 हैं। 13195 का सबसे बड़ा अभाज्य गुणनखंड 29 है।

# --instructions--

एक फ़ंक्शन लिखें जो दी गई संख्या का सबसे बड़ा अभाज्य गुणनखंड लौटाए।

फ़ंक्शन कॉल का उदाहरण:
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

2 का सबसे बड़ा अभाज्य गुणनखंड 2 होना चाहिए

```swift
tryCatch(largestPrimeFactor(2) == 2)
```

13195 का सबसे बड़ा अभाज्य गुणनखंड 29 होना चाहिए

```swift
tryCatch(largestPrimeFactor(13195) == 29)
```

600851475143 का सबसे बड़ा अभाज्य गुणनखंड 6857 होना चाहिए

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
