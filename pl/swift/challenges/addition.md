---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Dane są dwie liczby całkowite `num1` i `num2`. Napisz program, który dodaje te dwie liczby.

# --instructions--

Napisz funkcję, która zwraca sumę dwóch liczb.
> WSKAZÓWKA: pomiń etykiety argumentów używając `_` (podkreślnika)

Przykład wywołania funkcji:
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

Suma 1 i 3 musi być równa 4

```swift
tryCatch(addition(1, 3) == 4)
```

Suma 200 i 210 musi być równa 410

```swift
tryCatch(addition(200, 210) == 410)
```

Suma 15 i 35 musi być równa 50

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
