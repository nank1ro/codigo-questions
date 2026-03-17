---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Ein pythagoreisches Tripel ist eine Menge dreier natürlicher Zahlen a < b < c, für die gilt: a² + b² = c². Es gibt genau ein pythagoreisches Tripel, für das a + b + c = 1000 gilt. Finde das Produkt a × b × c.

# --instructions--

Schreibe eine Funktion, die das Produkt a × b × c des pythagoreischen Tripels berechnet, für das a + b + c = n gilt.

Beispiel eines Funktionsaufrufs:
```swift
print(specialPythagoreanTriplet(12))
// prints 60
```

# --seed--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Das Produkt des pythagoreischen Tripels mit a + b + c = 12 muss 60 ergeben

```swift
    func testPythagorean1() {
        XCTAssertEqual(specialPythagoreanTriplet(12), 60, "--err-t1--")
    }
```

Das Produkt des pythagoreischen Tripels mit a + b + c = 1000 muss 31875000 ergeben

```swift
    func testPythagorean2() {
        XCTAssertEqual(specialPythagoreanTriplet(1000), 31875000, "--err-t2--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testPythagorean1", testPythagorean1),
            ("testPythagorean2", testPythagorean2),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
