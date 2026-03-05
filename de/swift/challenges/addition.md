---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Gegeben zwei ganze Zahlen `num1` und `num2`, schreiben Sie ein Programm, um diese beiden Zahlen zu addieren

# --instructions--

Schreiben Sie eine Funktion, die die Summe zweier Zahlen zurückgibt.
> HINWEIS: Lassen Sie die Argumentbezeichnungen mit dem `_` (Unterstrich) weg

Beispiel für einen Funktionsaufruf:
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

Die Summe von 1 und 3 muss gleich 4 sein

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

Die Summe von 200 und 210 muss gleich 410 sein

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

Die Summe von 15 und 35 muss gleich 50 sein

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
