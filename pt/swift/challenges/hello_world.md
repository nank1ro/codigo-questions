---
language: swift
exerciseType: 1
difficulty: 1
title: "Olá Mundo!"
---

# --description--

__"Hello, World!"__ é o primeiro programa tradicional para quem está começando a programar em uma nova linguagem ou ambiente.

# --instructions--

Escreva uma função que retorne a string "Hello, World!".

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

A função deve retornar "Hello, World!".

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

