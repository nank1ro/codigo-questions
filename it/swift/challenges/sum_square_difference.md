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

La differenza quadrato-somma per n=10 deve essere uguale a 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

La differenza quadrato-somma per n=20 deve essere uguale a 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

La differenza quadrato-somma per n=100 deve essere uguale a 25164150

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
