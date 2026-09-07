---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Сумма квадратов первых десяти натуральных чисел равна 1² + 2² + ... + 10² = 385. Квадрат суммы первых десяти натуральных чисел равен (1 + 2 + ... + 10)² = 55² = 3025. Следовательно, разность между квадратом суммы и суммой квадратов первых десяти натуральных чисел равна 3025 − 385 = 2640.

# --instructions--

Напишите функцию, которая находит разность между квадратом суммы и суммой квадратов первых n натуральных чисел.

Пример вызова функции:
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

Разность суммы квадратов для n=10 должна быть равна 2640

```swift
tryCatch(sumSquareDifference(10) == 2640)
```

Разность суммы квадратов для n=20 должна быть равна 41230

```swift
tryCatch(sumSquareDifference(20) == 41230)
```

Разность суммы квадратов для n=100 должна быть равна 25164150

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
