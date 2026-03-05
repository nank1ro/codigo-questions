---
language: swift
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ は、新しい言語や環境でプログラミングを始める際の伝統的な最初のプログラムです。

# --instructions--

文字列 "Hello, World!" を返す関数を書いてください。

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

関数は "Hello, World!" を返す必要があります。

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

