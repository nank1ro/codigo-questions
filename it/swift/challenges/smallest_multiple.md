---
language: swift
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 è il numero più piccolo che può essere diviso per ciascuno dei numeri da 1 a 10 senza alcun resto.

# --instructions--

Scrivi una funzione che restituisce il numero positivo più piccolo che sia divisibile per tutti i numeri da 1 a n.

Esempio di chiamata alla funzione:
```swift
print(smallestMultiple(10))
// prints 2520
```

# --seed--

```swift
func smallestMultiple(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Il minimo multiplo da 1 a 5 deve essere uguale a 60

```swift
    func testSmallestMultiple1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

Il minimo multiplo da 1 a 10 deve essere uguale a 2520

```swift
    func testSmallestMultiple2() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t2--")
    }
```

Il minimo multiplo da 1 a 20 deve essere uguale a 232792560

```swift
    func testSmallestMultiple3() {
        XCTAssertEqual(smallestMultiple(20), 232792560, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSmallestMultiple1", testSmallestMultiple1),
            ("testSmallestMultiple2", testSmallestMultiple2),
            ("testSmallestMultiple3", testSmallestMultiple3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    return (1...n).reduce(1) { lcm($0, $1) }
}
```
