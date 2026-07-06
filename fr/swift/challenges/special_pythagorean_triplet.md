---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Un triplet pythagoricien est un ensemble de trois nombres naturels, a < b < c, pour lesquels a² + b² = c². Il existe exactement un triplet pythagoricien pour lequel a + b + c = 1000. Trouve le produit a × b × c.

# --instructions--

Écris une fonction qui trouve le produit a × b × c du triplet pythagoricien où a + b + c = n.

Exemple d'appel de fonction :
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

Le produit du triplet pythagoricien avec a + b + c = 12 doit être égal à 60

```swift
    func testPythagorean1() {
        XCTAssertEqual(specialPythagoreanTriplet(12), 60, "--err-t1--")
    }
```

Le produit du triplet pythagoricien avec a + b + c = 1000 doit être égal à 31875000

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
