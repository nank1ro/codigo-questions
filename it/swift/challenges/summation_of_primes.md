---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

La somma dei numeri primi inferiori a 10 è 2 + 3 + 5 + 7 = 17.

# --instructions--

Scrivi una funzione che calcola la somma di tutti i numeri primi inferiori al numero dato.

Esempio di chiamata alla funzione:
```swift
print(primeSummation(10))
// prints 17
```

# --seed--

```swift
func primeSummation(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

La somma di tutti i numeri primi inferiori a 10 deve essere uguale a 17

```swift
    func testPrimeSummation1() {
        XCTAssertEqual(primeSummation(10), 17, "--err-t1--")
    }
```

La somma di tutti i numeri primi inferiori a 1000 deve essere uguale a 76127

```swift
    func testPrimeSummation2() {
        XCTAssertEqual(primeSummation(1000), 76127, "--err-t2--")
    }
```

La somma di tutti i numeri primi inferiori a 100000 deve essere uguale a 454396537

```swift
    func testPrimeSummation3() {
        XCTAssertEqual(primeSummation(100000), 454396537, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testPrimeSummation1", testPrimeSummation1),
            ("testPrimeSummation2", testPrimeSummation2),
            ("testPrimeSummation3", testPrimeSummation3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func primeSummation(_ n: Int) -> Int {
    var sieve = [Bool](repeating: true, count: n)
    if n > 0 { sieve[0] = false }
    if n > 1 { sieve[1] = false }
    var i = 2
    while i * i < n {
        if sieve[i] {
            var j = i * i
            while j < n {
                sieve[j] = false
                j += i
            }
        }
        i += 1
    }
    return sieve.indices.filter { sieve[$0] }.reduce(0, +)
}
```
