---
language: swift
exerciseType: 1
difficulty: 1
title: Somme des chiffres
---

# --description--

On vous donne un entier `N`.
Écrivez un programme pour calculer la somme de tous les chiffres de N

# --instructions--

Retournez la somme des chiffres de `N`.
> ASTUCE : omettez l'étiquette d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
```swift
print(sumDigits(28))
// prints 10
```

# --seed--

```swift
func sumDigits() {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

La somme des chiffres de 12345 est 15

```swift
    func testSumOfDigits1() {
        XCTAssertEqual(sumDigits(12345), 15, "--err-t1--")
    }
```

La somme des chiffres de 57253 est 22

```swift
    func testSumOfDigits2() {
        XCTAssertEqual(sumDigits(57253), 22, "--err-t2--")
    }
```

La somme des chiffres de 122 est 5

```swift
    func testSumOfDigits3() {
        XCTAssertEqual(sumDigits(122), 5, "--err-t3--")
    }
```

La somme des chiffres de 91979997 est 60

```swift
    func testSumOfDigits4() {
        XCTAssertEqual(sumDigits(91979997), 60, "--err-t4--")
    }
```

La somme des chiffres de 2147483647 est 46

```swift
    func testSumOfDigits5() {
        XCTAssertEqual(sumDigits(2147483647), 46, "--err-t5--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSumOfDigits1", testSumOfDigits1),
            ("testSumOfDigits2", testSumOfDigits2),
            ("testSumOfDigits3", testSumOfDigits3),
            ("testSumOfDigits4", testSumOfDigits4),
            ("testSumOfDigits5", testSumOfDigits5),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func sumDigits(_ num: Int) -> Int {
    var n = num
    var result = 0
    while n > 0 {
        result += n % 10
        n = Int(n / 10)
    }
    return result
}
```

