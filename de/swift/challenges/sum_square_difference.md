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

Die Quadratsummendifferenz für n=10 muss 2640 ergeben

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

Die Quadratsummendifferenz für n=20 muss 41230 ergeben

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

Die Quadratsummendifferenz für n=100 muss 25164150 ergeben

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
