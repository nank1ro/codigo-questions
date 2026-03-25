---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385. The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# --instructions--

Write a function that finds the difference between the square of the sum and the sum of the squares of the first n natural numbers.

Example of function call:
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

The sum square difference for n=10 must equal 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

The sum square difference for n=20 must equal 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

The sum square difference for n=100 must equal 25164150

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
