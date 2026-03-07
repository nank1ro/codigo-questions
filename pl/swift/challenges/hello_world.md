---
language: swift
exerciseType: 1
difficulty: 1
title: Witaj Świecie!
---

# --description--

__"Witaj, Świecie!"__ to tradycyjny pierwszy program dla osób zaczynających programowanie w nowym języku lub środowisku.

# --instructions--

Napisz funkcję, która zwraca ciąg znaków "Hello, World!".

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

Funkcja powinna zwracać "Hello, World!".

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

