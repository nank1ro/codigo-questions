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

La diferencia de suma de cuadrados para n=10 debe ser igual a 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

La diferencia de suma de cuadrados para n=20 debe ser igual a 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

La diferencia de suma de cuadrados para n=100 debe ser igual a 25164150

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
