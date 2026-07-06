---
language: swift
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 ist die kleinste Zahl, die durch jede der Zahlen von 1 bis 10 ohne Rest teilbar ist.

# --instructions--

Schreibe eine Funktion, die die kleinste positive Zahl zurückgibt, die durch alle Zahlen von 1 bis n gleichmäßig teilbar ist.

Beispiel eines Funktionsaufrufs:
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

Das kleinste Vielfache von 1 bis 5 muss 60 ergeben

```swift
    func testSmallestMultiple1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

Das kleinste Vielfache von 1 bis 10 muss 2520 ergeben

```swift
    func testSmallestMultiple2() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t2--")
    }
```

Das kleinste Vielfache von 1 bis 20 muss 232792560 ergeben

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
