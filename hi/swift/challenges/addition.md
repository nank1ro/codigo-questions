---
language: swift
exerciseType: 1
difficulty: 1
title: जोड़
---

# --description--

दो पूर्णांक `num1` और `num2` दिए गए हैं, इन दो संख्याओं को जोड़ने के लिए एक प्रोग्राम लिखें

# --instructions--

एक फ़ंक्शन लिखें जो दो संख्याओं का योग लौटाए।
> संकेत: `_` (अंडरस्कोर) के साथ आर्गुमेंट लेबल हटाएं

फ़ंक्शन कॉल का उदाहरण:
```swift
print(addition(1, 2))
// prints 3
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
func addition() {
    
}
```

# --asserts--

1 और 3 का योग 4 होना चाहिए

```swift
tryCatch(addition(1, 3) == 4)
```

200 और 210 का योग 410 होना चाहिए

```swift
tryCatch(addition(200, 210) == 410)
```

15 और 35 का योग 50 होना चाहिए

```swift
tryCatch(addition(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
