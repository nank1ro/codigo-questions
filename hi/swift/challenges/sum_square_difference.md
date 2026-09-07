---
language: swift
exerciseType: 1
difficulty: 1
title: वर्गों के योग और योग के वर्ग का अंतर
---

# --description--

पहली दस प्राकृत संख्याओं के वर्गों का योग 1² + 2² + ... + 10² = 385 है। पहली दस प्राकृत संख्याओं के योग का वर्ग (1 + 2 + ... + 10)² = 55² = 3025 है। इस प्रकार वर्गों के योग और योग के वर्ग के बीच का अंतर 3025 − 385 = 2640 है।

# --instructions--

एक फ़ंक्शन लिखें जो पहली n प्राकृत संख्याओं के लिए योग के वर्ग और वर्गों के योग के बीच का अंतर ज्ञात करे।

फ़ंक्शन कॉल का उदाहरण:
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

n=10 के लिए वर्ग-योग अंतर 2640 होना चाहिए

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

n=20 के लिए वर्ग-योग अंतर 41230 होना चाहिए

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

n=100 के लिए वर्ग-योग अंतर 25164150 होना चाहिए

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
