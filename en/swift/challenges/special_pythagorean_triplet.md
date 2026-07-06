---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a² + b² = c². There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product a × b × c.

# --instructions--

Write a function that finds the product a × b × c of the Pythagorean triplet where a + b + c = n.

Example of function call:
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

The product of the Pythagorean triplet where a + b + c = 12 must equal 60

```swift
    func testPythagorean1() {
        XCTAssertEqual(specialPythagoreanTriplet(12), 60, "--err-t1--")
    }
```

The product of the Pythagorean triplet where a + b + c = 1000 must equal 31875000

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
