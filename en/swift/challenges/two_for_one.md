---
language: swift
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Given a name, return a string with the message:
`One for X, one for me.`
Where `X` is the given name.
However, if the name is missing, return the string:
`One for you, one for me.`

# --instructions--

Write a function that returns the correct string, examples:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**: `James`
**output**: `One for James, one for me.`

**input**: `Martha`
**output**: `One for Martha, one for me.`

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

No name given

```swift
do {
    let expected = "One for you, one for me."
    tryCatch(twoForOne() == expected)
}
```

Pass "James" as name

```swift
do {
    let expected = "One for James, one for me."
    tryCatch(twoForOne(name: "James") == expected)
}
```

Pass "Martha" as name

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


