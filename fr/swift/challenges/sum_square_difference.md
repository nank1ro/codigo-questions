---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La somme des carrés des dix premiers nombres naturels est 1² + 2² + ... + 10² = 385. Le carré de la somme des dix premiers nombres naturels est (1 + 2 + ... + 10)² = 55² = 3025. Donc la différence entre le carré de la somme et la somme des carrés des dix premiers nombres naturels est 3025 − 385 = 2640.

# --instructions--

Écris une fonction qui calcule la différence entre le carré de la somme et la somme des carrés des n premiers nombres naturels.

Exemple d'appel de fonction :
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

La différence somme-carré pour n=10 doit être égale à 2640

```swift
    func testSumSquare1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

La différence somme-carré pour n=20 doit être égale à 41230

```swift
    func testSumSquare2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

La différence somme-carré pour n=100 doit être égale à 25164150

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
