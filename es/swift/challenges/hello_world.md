---
language: swift
exerciseType: 1
difficulty: 1
title: ¡Hola Mundo!
---

# --description--

__"¡Hola, Mundo!"__ es el programa tradicional de inicio para comenzar a programar en un nuevo lenguaje o entorno.

# --instructions--

Escribe una función que devuelva la cadena "Hello, World!".

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

La función debe devolver "Hello, World!".

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

