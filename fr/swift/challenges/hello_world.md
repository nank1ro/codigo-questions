---
language: swift
exerciseType: 1
difficulty: 1
title: Bonjour le monde !
---

# --description--

**"Bonjour, le monde !"** est le programme traditionnel pour commencer la programmation dans un nouveau langage ou environnement.

# --instructions--

Écrivez une fonction qui retourne la chaîne "Bonjour, le monde !".

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

La fonction doit retourner "Bonjour, le monde !".

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

