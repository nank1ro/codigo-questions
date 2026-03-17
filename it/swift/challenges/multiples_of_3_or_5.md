---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se elenchiamo tutti i numeri naturali inferiori a 10 che sono multipli di 3 o 5, otteniamo 3, 5, 6 e 9. La somma di questi multipli è 23.

# --instructions--

Scrivi una funzione che calcola la somma di tutti i multipli di 3 o 5 inferiori al numero dato.

Esempio di chiamata alla funzione:
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

La somma dei multipli di 3 o 5 inferiori a 10 deve essere uguale a 23

```swift
    func testMultiples1() {
        XCTAssertEqual(multiplesOf3And5(10), 23, "--err-t1--")
    }
```

La somma dei multipli di 3 o 5 inferiori a 1000 deve essere uguale a 233168

```swift
    func testMultiples2() {
        XCTAssertEqual(multiplesOf3And5(1000), 233168, "--err-t2--")
    }
```

La somma dei multipli di 3 o 5 inferiori a 6987 deve essere uguale a 11390208

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
