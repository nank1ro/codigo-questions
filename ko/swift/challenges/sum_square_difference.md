---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

처음 10개의 자연수의 제곱의 합은,

12 + 22 + ... + 102 = 385
처음 10개의 자연수의 합의 제곱은,

(1 + 2 + ... + 10)2 = 552 = 3025
따라서 처음 10개의 자연수의 제곱의 합과 합의 제곱의 차이는 3025 − 385 = 2640입니다.

# --instructions--

처음 `n`개의 자연수의 제곱의 합과 합의 제곱의 차이를 구하세요.

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

`sumSquareDifference(10)`은 2640을 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

`sumSquareDifference(20)`은 41230을 반환해야 합니다.

```swift
    func test2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

`sumSquareDifference(100)`은 25164150을 반환해야 합니다.

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
