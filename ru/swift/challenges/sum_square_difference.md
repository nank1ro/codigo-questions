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

# --seed--

```swift
func sumSquareDifference(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Разность суммы квадратов для n=10 должна быть равна 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

Разность суммы квадратов для n=20 должна быть равна 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

Разность суммы квадратов для n=100 должна быть равна 25164150

```swift
    func testSumSquare3() {
        XCTAssertEqual(sumSquareDifference(100), 25164150, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSumSquare1", testSumSquare1),
            ("testSumSquare2", testSumSquare2),
            ("testSumSquare3", testSumSquare3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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
