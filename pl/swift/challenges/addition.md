---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Dane są dwie liczby całkowite `num1` i `num2`. Napisz program, który dodaje te dwie liczby.

# --instructions--

Napisz funkcję, która zwraca sumę dwóch liczb.
> WSKAZÓWKA: pomiń etykiety argumentów używając `_` (podkreślnika)

Przykład wywołania funkcji:
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

Suma 1 i 3 musi być równa 4

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

Suma 200 i 210 musi być równa 410

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

Suma 15 i 35 musi być równa 50

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
