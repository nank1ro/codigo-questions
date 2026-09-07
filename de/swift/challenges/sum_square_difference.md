---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Die Summe der Quadrate der ersten zehn natürlichen Zahlen ist 1² + 2² + ... + 10² = 385. Das Quadrat der Summe der ersten zehn natürlichen Zahlen ist (1 + 2 + ... + 10)² = 55² = 3025. Die Differenz zwischen dem Quadrat der Summe und der Summe der Quadrate der ersten zehn natürlichen Zahlen beträgt 3025 − 385 = 2640.

# --instructions--

Schreibe eine Funktion, die die Differenz zwischen dem Quadrat der Summe und der Summe der Quadrate der ersten n natürlichen Zahlen berechnet.

Beispiel eines Funktionsaufrufs:
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

Die Quadratsummendifferenz für n=10 muss 2640 ergeben

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

Die Quadratsummendifferenz für n=20 muss 41230 ergeben

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

Die Quadratsummendifferenz für n=100 muss 25164150 ergeben

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
