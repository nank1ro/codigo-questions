---
language: swift
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

पहले दस प्राकृतिक संख्याओं के वर्गों का योग है,

12 + 22 + ... + 102 = 385
पहले दस प्राकृतिक संख्याओं के योग का वर्ग है,

(1 + 2 + ... + 10)2 = 552 = 3025
अतः पहले दस प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर 3025 − 385 = 2640 है।

# --instructions--

पहले `n` प्राकृतिक संख्याओं के वर्गों के योग और योग के वर्ग के बीच का अंतर ज्ञात करें।

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

`sumSquareDifference(10)` को 2640 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(sumSquareDifference(10), 2640, "--err-t1--")
    }
```

`sumSquareDifference(20)` को 41230 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(sumSquareDifference(20), 41230, "--err-t2--")
    }
```

`sumSquareDifference(100)` को 25164150 लौटाना चाहिए।

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
