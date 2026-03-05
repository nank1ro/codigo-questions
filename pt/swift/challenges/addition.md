---
language: swift
exerciseType: 1
difficulty: 1
title: "Adição"
---

# --description--

Dados dois inteiros `num1` e `num2`, escreva um programa para somar esses dois números

# --instructions--

Escreva uma função que retorne a soma de dois números.
> DICA: omita os rótulos dos argumentos com o `_` (underscore)

Exemplo de chamada da função:
```swift
print(addition(1, 2))
// prints 3
```

# --seed--

```swift
func addition() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

A soma de 1 e 3 deve ser igual a 4

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

A soma de 200 e 210 deve ser igual a 410

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

A soma de 15 e 35 deve ser igual a 50

```swift
    func testAddition3() {
        XCTAssertEqual(addition(15, 35), 50, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testAddition1", testAddition1),
            ("testAddition2", testAddition2),
            ("testAddition3", testAddition3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
