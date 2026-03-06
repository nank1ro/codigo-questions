---
language: swift
exerciseType: 1
difficulty: 1
title: 你好世界！
---

# --description--

__"Hello, World!"__ 是在新语言或环境中开始编程的传统第一个程序。

# --instructions--

编写一个返回字符串 "Hello, World!" 的函数。

# --seed--

```swift
func hello() -> String {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

函数应该返回 "Hello, World!"。

```swift
    func testHi() {
        let expected = "Hello, World!"
        XCTAssertEqual(hello(), expected, "--err-t1--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testHi", testHi),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func hello() -> String {
    return "Hello, World!"
}
```

