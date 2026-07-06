---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Die Primfaktoren von 13195 sind 5, 7, 13 und 29. Der größte Primfaktor von 13195 ist 29.

# --instructions--

Schreibe eine Funktion, die den größten Primfaktor der gegebenen Zahl zurückgibt.

Beispiel eines Funktionsaufrufs:
```swift
print(largestPrimeFactor(13195))
// prints 29
```

# --seed--

```swift
func largestPrimeFactor(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Der größte Primfaktor von 2 muss 2 ergeben

```swift
    func testLargestPrime1() {
        XCTAssertEqual(largestPrimeFactor(2), 2, "--err-t1--")
    }
```

Der größte Primfaktor von 13195 muss 29 ergeben

```swift
    func testLargestPrime2() {
        XCTAssertEqual(largestPrimeFactor(13195), 29, "--err-t2--")
    }
```

Der größte Primfaktor von 600851475143 muss 6857 ergeben

```swift
    func testLargestPrime3() {
        XCTAssertEqual(largestPrimeFactor(600851475143), 6857, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testLargestPrime1", testLargestPrime1),
            ("testLargestPrime2", testLargestPrime2),
            ("testLargestPrime3", testLargestPrime3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func largestPrimeFactor(_ number: Int) -> Int {
    var n = number
    var largest = 1
    var factor = 2
    while factor * factor <= n {
        while n % factor == 0 {
            largest = factor
            n /= factor
        }
        factor += 1
    }
    if n > 1 {
        largest = n
    }
    return largest
}
```
