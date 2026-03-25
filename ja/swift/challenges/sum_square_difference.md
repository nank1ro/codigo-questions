---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

最初の10個の自然数の二乗の和は、

12 + 22 + ... + 102 = 385
最初の10個の自然数の和の二乗は、

(1 + 2 + ... + 10)2 = 552 = 3025
したがって、最初の10個の自然数の二乗の和と和の二乗の差は 3025 − 385 = 2640 です。

# --instructions--

最初の`n`個の自然数の二乗の和と和の二乗の差を求めてください。

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

`sumSquareDifference(10)`は2640を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

`sumSquareDifference(20)`は41230を返すべきです。

```swift
    func test2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

`sumSquareDifference(100)`は25164150を返すべきです。

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
