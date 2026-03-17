---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

A soma dos quadrados dos primeiros dez números naturais é,

12 + 22 + ... + 102 = 385
O quadrado da soma dos primeiros dez números naturais é,

(1 + 2 + ... + 10)2 = 552 = 3025
Portanto, a diferença entre a soma dos quadrados dos primeiros dez números naturais e o quadrado da soma é 3025 − 385 = 2640.

# --instructions--

Encontre a diferença entre a soma dos quadrados dos primeiros `n` números naturais e o quadrado da soma.

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

`sumSquareDifference(10)` deve retornar 2640.

```swift
    func test1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

`sumSquareDifference(20)` deve retornar 41230.

```swift
    func test2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

`sumSquareDifference(100)` deve retornar 25164150.

```swift
    func test3() {
        XCTAssertEqual(sumSquareDifference(100), 25164150, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
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
