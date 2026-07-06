---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Uma terna pitagórica é um conjunto de três números naturais, `a` < `b` < `c`, para os quais, <latex>a^2 + b^2 = c^2</latex>

Por exemplo, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

Existe exatamente uma terna pitagórica para a qual `a` + `b` + `c` = 1000.

# --instructions--

Encontre o produto `abc` tal que `a` + `b` + `c` = `n`.

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

`specialPythagoreanTriplet(24)` deve retornar 480.

```swift
    func test1() {
        XCTAssertEqual(specialPythagoreanTriplet(24), 480, "--err-t1--")
    }
```

`specialPythagoreanTriplet(120)` deve retornar 49920, 55080 ou 60000.

```swift
    func test2() {
        XCTAssertTrue([49920, 55080, 60000].contains(specialPythagoreanTriplet(120)), "--err-t2--")
    }
```

`specialPythagoreanTriplet(1000)` deve retornar 31875000.

```swift
    func test3() {
        XCTAssertEqual(specialPythagoreanTriplet(1000), 31875000, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1...(n / 3) {
        for b in (a + 1)...(n / 2) {
            let cSquared = a * a + b * b
            let c = Int(Double(cSquared).squareRoot())
            if c * c == cSquared && a + b + c == n {
                return a * b * c
            }
        }
    }
    return 0
}
```
