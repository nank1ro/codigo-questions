---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Étant donné deux entiers `num1` et `num2`, écrivez un programme pour additionner ces deux nombres

# --instructions--

Écrivez une fonction qui retourne la somme de deux nombres.
> ASTUCE : omettez les étiquettes d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
```swift
print(addition(1, 2))
// prints 3
```

# --seed--

```swift
func addition() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

La somme de 1 et 3 doit être égale à 4

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

La somme de 200 et 210 doit être égale à 410

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

La somme de 15 et 35 doit être égale à 50

```swift
    func testAddition3() {
        XCTAssertEqual(addition(15, 35), 50, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testAddition1", testAddition1),
            ("testAddition2", testAddition2),
            ("testAddition3", testAddition3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
