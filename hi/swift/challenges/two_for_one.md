---
language: swift
exerciseType: 1
difficulty: 1
title: दो में से एक
---

# --description--

एक नाम दिया गया है, इस संदेश के साथ एक स्ट्रिंग लौटाएं:
`One for X, one for me.`
जहां `X` दिया गया नाम है।
हालांकि, यदि नाम नहीं दिया गया है, तो यह स्ट्रिंग लौटाएं:
`One for you, one for me.`

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

**इनपुट**: `Walter`
**आउटपुट**: `One for Walter, one for me.`

**इनपुट**: `James`
**आउटपुट**: `One for James, one for me.`

**इनपुट**: `Martha`
**आउटपुट**: `One for Martha, one for me.`

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
func twoForOne(name: String) -> String {
    
}
```

# --asserts--

कोई नाम नहीं दिया गया

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

नाम के रूप में "James" पास करें

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

नाम के रूप में "Martha" पास करें

```swift
do {
    let expected = "One for Martha, one for me."
    tryCatch(twoForOne(name: "Martha") == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func twoForOne(name: String? = nil) -> String {
    if let validName = name {
        return "One for \(validName), one for me."
    }
    return "One for you, one for me."
}
```


