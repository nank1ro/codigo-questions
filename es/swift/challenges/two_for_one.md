---
language: swift
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Given un nombre, Devuelve un cadena con el mensaje:
`One para X, uno para me.`
donde `X` es el dado nombre.
sin embargo, si el nombre es missing, Devuelve el cadena:
`One para you, uno para me.`

# --instructions--

Escribe un funcion ese devuelve el correct cadena, ejemplos:

**entrada**: `Walter`
**salida**: `One para Walter, uno para me.`

**entrada**: `James`
**salida**: `One para James, uno para me.`

**entrada**: `Martha`
**salida**: `One para Martha, uno para me.`

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

No name given

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

Pass "James" as name

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

Pass "Martha" as name

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
func twoForOne(nombre: String? = nil) -> String {
    if let validName = nombre {
        return "One for \(validName), one for me."
    }
    return "One for you, one for me."
}
```


