---
language: swift
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ e' il primo programma tradizionale per iniziare a programmare in un nuovo linguaggio o ambiente.

# --instructions--

Scrivi una funzione che restituisce "Hello, World!".

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

La funzione deve restituire "Hello, World!".

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
    return "Hello, World!";
}
```
