---
language: swift
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 est le plus petit nombre divisible par chacun des nombres de 1 à 10 sans aucun reste.

# --instructions--

Écris une fonction qui retourne le plus petit nombre positif divisible par tous les nombres de 1 à n.

Exemple d'appel de fonction :
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

Le plus petit multiple de 1 à 5 doit être égal à 60

```swift
    func testSmallestMultiple1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

Le plus petit multiple de 1 à 10 doit être égal à 2520

```swift
    func testSmallestMultiple2() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t2--")
    }
```

Le plus petit multiple de 1 à 20 doit être égal à 232792560

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
