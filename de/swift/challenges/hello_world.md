---
language: swift
exerciseType: 1
difficulty: 1
title: Hallo Welt!
---

# --description--

__"Hello, World!"__ ist das traditionelle erste Programm zum Erlernen der Programmierung in einer neuen Sprache oder Umgebung.

# --instructions--

Schreiben Sie eine Funktion, die den String "Hello, World!" zurückgibt.

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

Die Funktion sollte "Hello, World!" zurückgeben.

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

