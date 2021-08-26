---
language: swift
exerciseType: 1
difficulty: 1
title: Addizione
---

# --description--

Dati due number interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri
> SUGGERIMENTO: ometti i nomi degli argomenti con l'underscore `_`

Esempio di chiamata della funzione:
```swift
print(somma(1, 2))
// stampa 3
```

# --seed--

```swift
func somma() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class AdditionTests: XCTestCase {
```

# --asserts--

La somma di 1 e 3 deve essere uguale a 4

```swift
    func testAddition1() {
        XCTAssertEqual(somma(1, 3), 4, "--err-t1--")
    }
```

La somma di 200 e 210 deve essere uguale a 410

```swift
    func testAddition2() {
        XCTAssertEqual(somma(200, 210), 410, "--err-t2--")
    }
```

La somma di 15 e 35 deve essere uguale a 50

```swift
    func testAddition3() {
        XCTAssertEqual(somma(15, 35), 50, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension AdditionTests {
    static var allTests : [(String, (AdditionTests) -> () throws -> Void)] {
        return [
            ("testAddition1", testAddition1),
            ("testAddition2", testAddition2),
            ("testAddition3", testAddition3),
        ]
    }
}

XCTMain([testCase(AdditionTests.allTests)])
```

# --solutions--

```swift
func somma(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2;
}
```
