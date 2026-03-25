---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Una terna pitagorica è un insieme di tre numeri naturali, a < b < c, per i quali a² + b² = c². Esiste esattamente una terna pitagorica per la quale a + b + c = 1000. Trova il prodotto a × b × c.

# --instructions--

Scrivi una funzione che trova il prodotto a × b × c della terna pitagorica dove a + b + c = n.

Esempio di chiamata alla funzione:
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

Il prodotto della terna pitagorica con a + b + c = 12 deve essere uguale a 60

```swift
    func testPythagorean1() {
        XCTAssertEqual(specialPythagoreanTriplet(12), 60, "--err-t1--")
    }
```

Il prodotto della terna pitagorica con a + b + c = 1000 deve essere uguale a 31875000

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
