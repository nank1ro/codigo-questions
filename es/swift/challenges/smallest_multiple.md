---
language: swift
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 es el número más pequeño que puede dividirse por cada uno de los números del 1 al 10 sin ningún resto.

# --instructions--

Escribe una función que devuelva el número positivo más pequeño que sea divisible de forma exacta por todos los números del 1 al n.

Ejemplo de llamada a la función:
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

El mínimo múltiplo del 1 al 5 debe ser igual a 60

```swift
    func testSmallestMultiple1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

El mínimo múltiplo del 1 al 10 debe ser igual a 2520

```swift
    func testSmallestMultiple2() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t2--")
    }
```

El mínimo múltiplo del 1 al 20 debe ser igual a 232792560

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
