---
language: swift
exerciseType: 1
difficulty: 1
title: Bonjour le monde !
---

# --description--

**"Bonjour, le monde !"** est le programme traditionnel pour commencer la programmation dans un nouveau langage ou environnement.

# --instructions--

Écrivez une fonction qui retourne la chaîne "Bonjour, le monde !".

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

La fonction doit retourner "Bonjour, le monde !".

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

