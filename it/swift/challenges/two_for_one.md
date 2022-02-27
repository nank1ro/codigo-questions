---
language: swift
exerciseType: 1
difficulty: 1
title: Due per uno
---

# --description--

Dato un nome, restituire una stringa con il messaggio:
`Uno per X, uno per me.`
Dove `X` e' il nome dato.
Tuttavia, se il nome manca, restituire la stringa:
`Uno per te, uno per me.`

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

**input**: `Walter`
**output**: `Uno per Walter, uno per me.`

**input**:
**output**: `Uno per te, uno per me.`

**input**: `Martha`
**output**: `Uno per Martha, uno per me.`

# --seed--

```swift
func duePerUno(nome: String) -> String {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Dividi con qualcuno

```swift
    func testNoNameGiven() {
        let expected = "Uno per te, uno per me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

Dividi con "Daniele"

```swift
    func testANameGiven() {
        let expected = "Uno per Daniele, uno per me."
        XCTAssertEqual(twoForOne(nome: "Daniele"), expected, "--err-t2--")
    }
```

Dividi con "Marta"

```swift
    func testAnotherNameGiven() {
        let expected = "Uno per Marta, uno per me."
        XCTAssertEqual(twoForOne(nome: "Marta"), expected, "--err-t3--")
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
func duePerUno(nome: String? = nil) -> String {
    if let nomeValido = nome {
        return "Uno per \(nomeValido), uno per me."
    }
    return "Uno per te, uno per me."
}
```



