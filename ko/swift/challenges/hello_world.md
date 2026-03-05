---
language: swift
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__는 새로운 언어나 환경에서 프로그래밍을 시작할 때 전통적으로 작성하는 첫 번째 프로그램입니다.

# --instructions--

"Hello, World!" 문자열을 반환하는 함수를 작성하십시오.

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

함수는 "Hello, World!"를 반환해야 합니다.

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

