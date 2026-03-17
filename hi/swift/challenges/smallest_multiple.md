---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 वह सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना शेषफल के विभाजित किया जा सकता है।

# --instructions--

वह सबसे छोटी धनात्मक संख्या क्या है जो 1 से `n` तक की सभी संख्याओं से समान रूप से विभाज्य है?

# --seed--

```swift
func smallestMultiple(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`smallestMultiple(5)` को 60 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

`smallestMultiple(7)` को 420 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(smallestMultiple(7), 420, "--err-t2--")
    }
```

`smallestMultiple(10)` को 2520 लौटाना चाहिए।

```swift
    func test3() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t3--")
    }
```

`smallestMultiple(13)` को 360360 लौटाना चाहिए।

```swift
    func test4() {
        XCTAssertEqual(smallestMultiple(13), 360360, "--err-t4--")
    }
```

`smallestMultiple(20)` को 232792560 लौटाना चाहिए।

```swift
    func test5() {
        XCTAssertEqual(smallestMultiple(20), 232792560, "--err-t5--")
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
            ("test4", test4),
            ("test5", test5),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    var result = 1
    for i in 2...n {
        result = lcm(result, i)
    }
    return result
}
```
