---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Wenn wir alle natürlichen Zahlen unter 10 auflisten, die Vielfache von 3 oder 5 sind, erhalten wir 3, 5, 6 und 9. Die Summe dieser Vielfachen beträgt 23.

# --instructions--

Schreibe eine Funktion, die die Summe aller Vielfachen von 3 oder 5 unterhalb der gegebenen Zahl berechnet.

Beispiel eines Funktionsaufrufs:
```swift
print(multiplesOf3And5(10))
// prints 23
```

# --seed--

```swift
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Die Summe der Vielfachen von 3 oder 5 unter 10 muss 23 ergeben

```swift
    func testMultiples1() {
        XCTAssertEqual(multiplesOf3And5(10), 23, "--err-t1--")
    }
```

Die Summe der Vielfachen von 3 oder 5 unter 1000 muss 233168 ergeben

```swift
    func testMultiples2() {
        XCTAssertEqual(multiplesOf3And5(1000), 233168, "--err-t2--")
    }
```

Die Summe der Vielfachen von 3 oder 5 unter 6987 muss 11390208 ergeben

```swift
    func testMultiples3() {
        XCTAssertEqual(multiplesOf3And5(6987), 11390208, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testMultiples1", testMultiples1),
            ("testMultiples2", testMultiples2),
            ("testMultiples3", testMultiples3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
