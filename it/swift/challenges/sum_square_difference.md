---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La somma dei quadrati dei primi dieci numeri naturali è 1² + 2² + ... + 10² = 385. Il quadrato della somma dei primi dieci numeri naturali è (1 + 2 + ... + 10)² = 55² = 3025. Quindi la differenza tra il quadrato della somma e la somma dei quadrati dei primi dieci numeri naturali è 3025 − 385 = 2640.

# --instructions--

Scrivi una funzione che calcola la differenza tra il quadrato della somma e la somma dei quadrati dei primi n numeri naturali.

Esempio di chiamata alla funzione:
```swift
print(sumSquareDifference(10))
// prints 2640
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
func sumSquareDifference(_ n: Int) -> Int {

}
```

# --asserts--

La differenza quadrato-somma per n=10 deve essere uguale a 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

La differenza quadrato-somma per n=20 deve essere uguale a 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

La differenza quadrato-somma per n=100 deve essere uguale a 25164150

```swift
tryCatch(sumSquareDifference(100) == 25164150)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumSquareDifference(_ n: Int) -> Int {
    let sumOfSquares = (1...n).reduce(0) { $0 + $1 * $1 }
    let sum = (1...n).reduce(0, +)
    let squareOfSum = sum * sum
    return squareOfSum - sumOfSquares
}
```
