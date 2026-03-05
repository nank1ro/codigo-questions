---
language: swift
exerciseType: 1
difficulty: 1
title: 둘이서 하나
---

# --description--

이름이 주어지면 다음 메시지가 포함된 문자열을 반환합니다:
`One for X, one for me.`
여기서 `X`는 주어진 이름입니다.
그러나 이름이 없으면 다음 문자열을 반환합니다:
`One for you, one for me.`

# --instructions--

올바른 문자열을 반환하는 함수를 작성하십시오. 예시:

**입력**: `Walter`
**출력**: `One for Walter, one for me.`

**입력**: `James`
**출력**: `One for James, one for me.`

**입력**: `Martha`
**출력**: `One for Martha, one for me.`

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

이름이 주어지지 않음

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

"James"를 이름으로 전달

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

"Martha"를 이름으로 전달

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


