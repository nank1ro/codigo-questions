---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Un número palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. El mayor palíndromo formado por el producto de dos números de 2 dígitos es 9009 = 91 × 99.

# --instructions--

Escribe una función que encuentre el mayor palíndromo formado por el producto de dos números de n dígitos.

Ejemplo de llamada a la función:
```swift
print(largestPalindromeProduct(2))
// prints 9009
```

# --seed--

```swift
func largestPalindromeProduct(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

El mayor producto palíndromo de dos números de 2 dígitos debe ser igual a 9009

```swift
    func testPalindrome1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

El mayor producto palíndromo de dos números de 3 dígitos debe ser igual a 906609

```swift
    func testPalindrome2() {
        XCTAssertEqual(largestPalindromeProduct(3), 906609, "--err-t2--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testPalindrome1", testPalindrome1),
            ("testPalindrome2", testPalindrome2),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func largestPalindromeProduct(_ n: Int) -> Int {
    func isPalindrome(_ num: Int) -> Bool {
        let s = String(num)
        return s == String(s.reversed())
    }
    let upper = Int(pow(10.0, Double(n))) - 1
    let lower = Int(pow(10.0, Double(n - 1)))
    var largest = 0
    for i in stride(from: upper, through: lower, by: -1) {
        if i * upper < largest { break }
        for j in stride(from: i, through: lower, by: -1) {
            let product = i * j
            if product < largest { break }
            if isPalindrome(product) {
                largest = product
            }
        }
    }
    return largest
}
```
