---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Suma kwadratów pierwszych dziesięciu liczb naturalnych wynosi 1² + 2² + ... + 10² = 385. Kwadrat sumy pierwszych dziesięciu liczb naturalnych wynosi (1 + 2 + ... + 10)² = 55² = 3025. Zatem różnica między sumą kwadratów a kwadratem sumy pierwszych dziesięciu liczb naturalnych wynosi 3025 − 385 = 2640.

# --instructions--

Napisz funkcję, która znajduje różnicę między kwadratem sumy a sumą kwadratów pierwszych n liczb naturalnych.

Przykład wywołania funkcji:
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

Różnica sumy kwadratów dla n=10 musi być równa 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

Różnica sumy kwadratów dla n=20 musi być równa 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

Różnica sumy kwadratów dla n=100 musi być równa 25164150

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
