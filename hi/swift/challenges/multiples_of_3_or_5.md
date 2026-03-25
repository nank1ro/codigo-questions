---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

यदि हम 10 से कम सभी प्राकृतिक संख्याओं को सूचीबद्ध करें जो 3 या 5 के गुणज हैं, तो हमें 3, 5, 6 और 9 मिलते हैं। इन गुणजों का योग 23 है।

# --instructions--

दिए गए पैरामीटर मान `number` से कम 3 या 5 के सभी गुणजों का योग ज्ञात करें।

# --seed--

```swift
func multiplesOf3and5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`multiplesOf3and5(10)` को 23 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(multiplesOf3and5(10), 23, "--err-t1--")
    }
```

`multiplesOf3and5(1000)` को 233168 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(multiplesOf3and5(1000), 233168, "--err-t2--")
    }
```

`multiplesOf3and5(6987)` को 11390208 लौटाना चाहिए।

```swift
    func test3() {
        XCTAssertEqual(multiplesOf3and5(6987), 11390208, "--err-t3--")
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
func multiplesOf3and5(_ number: Int) -> Int {
    var total = 0
    for i in 0..<number {
        if i % 3 == 0 || i % 5 == 0 {
            total += i
        }
    }
    return total
}
```
