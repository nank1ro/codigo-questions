---
language: swift
exerciseType: 1
difficulty: 1
title: "Dois por um"
---

# --description--

Dado um nome, retorne uma string com a mensagem:
`One for X, one for me.`
Onde `X` é o nome dado.
No entanto, se o nome estiver ausente, retorne a string:
`One for you, one for me.`

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

**entrada**: `Walter`
**saída**: `One for Walter, one for me.`

**entrada**: `James`
**saída**: `One for James, one for me.`

**entrada**: `Martha`
**saída**: `One for Martha, one for me.`

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

Nenhum nome fornecido

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

Passar "James" como nome

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

Passar "Martha" como nome

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


