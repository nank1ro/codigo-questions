---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Si l'on liste tous les nombres naturels inférieurs à 10 qui sont multiples de 3 ou 5, on obtient 3, 5, 6 et 9. La somme de ces multiples est 23.

# --instructions--

Écris une fonction qui calcule la somme de tous les multiples de 3 ou 5 inférieurs au nombre donné.

Exemple d'appel de fonction :
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

La somme des multiples de 3 ou 5 inférieurs à 10 doit être égale à 23

```swift
    func testMultiples1() {
        XCTAssertEqual(multiplesOf3And5(10), 23, "--err-t1--")
    }
```

La somme des multiples de 3 ou 5 inférieurs à 1000 doit être égale à 233168

```swift
    func testMultiples2() {
        XCTAssertEqual(multiplesOf3And5(1000), 233168, "--err-t2--")
    }
```

La somme des multiples de 3 ou 5 inférieurs à 6987 doit être égale à 11390208

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
