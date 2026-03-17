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

Różnica sumy kwadratów dla n=10 musi być równa 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

Różnica sumy kwadratów dla n=20 musi być równa 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

Różnica sumy kwadratów dla n=100 musi być równa 25164150

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
