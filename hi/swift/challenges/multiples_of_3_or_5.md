---
language: swift
exerciseType: 1
difficulty: 1
title: 3 या 5 के गुणज
---

# --description--

यदि हम 10 से कम सभी प्राकृत संख्याओं को सूचीबद्ध करें जो 3 या 5 के गुणज हैं, तो हमें 3, 5, 6 और 9 मिलते हैं। इन गुणजों का योग 23 है।

# --instructions--

एक फ़ंक्शन लिखें जो दी गई संख्या से कम सभी 3 या 5 के गुणजों का योग ज्ञात करे।

फ़ंक्शन कॉल का उदाहरण:
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

10 से कम 3 या 5 के गुणजों का योग 23 होना चाहिए

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

1000 से कम 3 या 5 के गुणजों का योग 233168 होना चाहिए

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

6987 से कम 3 या 5 के गुणजों का योग 11390208 होना चाहिए

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
