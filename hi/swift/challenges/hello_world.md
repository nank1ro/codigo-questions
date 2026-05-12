---
language: swift
exerciseType: 1
difficulty: 1
title: हैलो वर्ल्ड!
---

# --description--

__"Hello, World!"__ किसी नई भाषा या वातावरण में प्रोग्रामिंग शुरू करने के लिए पारंपरिक पहला प्रोग्राम है।

# --instructions--

एक फ़ंक्शन लिखें जो स्ट्रिंग "Hello, World!" लौटाए।

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
func hello() -> String {
    
}
```

# --asserts--

फ़ंक्शन को "Hello, World!" लौटाना चाहिए।

```swift
do {
    let expected = "Hello, World!"
    tryCatch(hello() == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func hello() -> String {
    return "Hello, World!"
}
```

