---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

前十个自然数的平方和为 1² + 2² + ... + 10² = 385。前十个自然数之和的平方为 (1 + 2 + ... + 10)² = 55² = 3025。因此，前十个自然数的平方和与和的平方之差为 3025 − 385 = 2640。

# --instructions--

编写一个函数，求前 n 个自然数的和的平方与平方和之差。

函数调用示例：
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

n=10 时的平方差必须等于 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

n=20 时的平方差必须等于 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

n=100 时的平方差必须等于 25164150

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
