---
language: swift
exerciseType: 1
difficulty: 1
title: 二换一
---

# --description--

给定一个名字，返回一个包含以下消息的字符串：
`One for X, one for me.`
其中 `X` 是给定的名字。
但是，如果没有提供名字，返回字符串：
`One for you, one for me.`

# --instructions--

编写一个返回正确字符串的函数，示例：

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**: `James`
**output**: `One for James, one for me.`

**input**: `Martha`
**output**: `One for Martha, one for me.`

# --seed--

```swift
func twoForOne(name: String) -> String {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

未提供名字

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

传入 "James" 作为名字

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

传入 "Martha" 作为名字

```swift
    func testAnotherNameGiven() {
        let expected = "One for Martha, one for me."
        XCTAssertEqual(twoForOne(name: "Martha"), expected, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testNoNameGiven", testNoNameGiven),
            ("testANameGiven", testANameGiven),
            ("testAnotherNameGiven", testAnotherNameGive),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func twoForOne(name: String? = nil) -> String {
    if let validName = name {
        return "One for \(validName), one for me."
    }
    return "One for you, one for me."
}
```


