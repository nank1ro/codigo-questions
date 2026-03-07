---
language: swift
exerciseType: 1
difficulty: 1
title: Два за одного
---

# --description--

Дано имя, верните строку с сообщением:
`One for X, one for me.`
Где `X` — это данное имя.
Однако, если имя отсутствует, верните строку:
`One for you, one for me.`

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

**ввод**: `Walter`
**вывод**: `One for Walter, one for me.`

**ввод**: `James`
**вывод**: `One for James, one for me.`

**ввод**: `Martha`
**вывод**: `One for Martha, one for me.`

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

Имя не указано

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

Передано имя "James"

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

Передано имя "Martha"

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


