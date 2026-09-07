---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La suma de los cuadrados de los primeros diez números naturales es 1² + 2² + ... + 10² = 385. El cuadrado de la suma de los primeros diez números naturales es (1 + 2 + ... + 10)² = 55² = 3025. Por lo tanto, la diferencia entre el cuadrado de la suma y la suma de los cuadrados de los primeros diez números naturales es 3025 − 385 = 2640.

# --instructions--

Escribe una función que encuentre la diferencia entre el cuadrado de la suma y la suma de los cuadrados de los primeros n números naturales.

Ejemplo de llamada a la función:
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

La diferencia de suma de cuadrados para n=10 debe ser igual a 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

La diferencia de suma de cuadrados para n=20 debe ser igual a 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

La diferencia de suma de cuadrados para n=100 debe ser igual a 25164150

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
