---
language: swift
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"¡Hola, Mundo!"__ es el programa tradicional de inicio para comenzar a programar en un nuevo lenguaje o entorno.

# --instructions--

Escribe una función que devuelva la cadena "Hello, World!".

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

La función debe devolver "Hello, World!".

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

