---
language: swift
exerciseType: 1
difficulty: 1
title: Hallo Welt!
---

# --description--

__"Hello, World!"__ ist das traditionelle erste Programm zum Erlernen der Programmierung in einer neuen Sprache oder Umgebung.

# --instructions--

Schreiben Sie eine Funktion, die den String "Hello, World!" zurückgibt.

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

Die Funktion sollte "Hello, World!" zurückgeben.

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

