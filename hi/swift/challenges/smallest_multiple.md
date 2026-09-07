---
language: swift
exerciseType: 1
difficulty: 1
title: सबसे छोटा गुणज
---

# --description--

2520 सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना किसी शेषफल के विभाजित किया जा सकता है।

# --instructions--

एक फ़ंक्शन लिखें जो 1 से n तक की सभी संख्याओं से पूर्ण रूप से विभाज्य सबसे छोटी धनात्मक संख्या लौटाए।

फ़ंक्शन कॉल का उदाहरण:
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

1 से 5 तक का सबसे छोटा गुणज 60 होना चाहिए

```swift
tryCatch(smallestMultiple(5) == 60)
```

1 से 10 तक का सबसे छोटा गुणज 2520 होना चाहिए

```swift
tryCatch(smallestMultiple(10) == 2520)
```

1 से 20 तक का सबसे छोटा गुणज 232792560 होना चाहिए

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
