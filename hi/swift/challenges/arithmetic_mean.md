---
language: swift
exerciseType: 1
difficulty: 1
title: अंकगणितीय माध्य
---

# --description--

एक संख्यात्मक वेक्टर का _अंकगणितीय माध्य_ (arithmetic average) ज्ञात करने के लिए `mean` नामक एक फ़ंक्शन लिखें।

# --instructions--

एक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का माध्य लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(mean([1, 2, 3]))
// prints 2.0
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
func mean() {
    
}
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]` का माध्य 4.0 के बराबर होना चाहिए

```swift
tryCatch(mean([1, 2, 3, 4, 5, 6, 7]) == 4.0)
```

`[4, 5, 6]` का माध्य 5.0 के बराबर होना चाहिए

```swift
tryCatch(mean([4, 5, 6]) == 5.0)
```

`[12, 34, 56, 78]` का माध्य 45.0 के बराबर होना चाहिए

```swift
tryCatch(mean([12, 34, 56, 78]) == 45.0)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
