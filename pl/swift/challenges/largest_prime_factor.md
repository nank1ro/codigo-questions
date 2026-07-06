---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Czynniki pierwsze liczby 13195 to 5, 7, 13 i 29. Największy czynnik pierwszy liczby 13195 to 29.

# --instructions--

Napisz funkcję, która zwraca największy czynnik pierwszy podanej liczby.

Przykład wywołania funkcji:
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

Największy czynnik pierwszy liczby 2 musi być równy 2

```swift
    func testLargestPrime1() {
        XCTAssertEqual(largestPrimeFactor(2), 2, "--err-t1--")
    }
```

Największy czynnik pierwszy liczby 13195 musi być równy 29

```swift
    func testLargestPrime2() {
        XCTAssertEqual(largestPrimeFactor(13195), 29, "--err-t2--")
    }
```

Największy czynnik pierwszy liczby 600851475143 musi być równy 6857

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
