---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Un numero palindromo si legge allo stesso modo in entrambe le direzioni. Il palindromo più grande ottenuto dal prodotto di due numeri a 2 cifre è 9009 = 91 × 99.

# --instructions--

Scrivi una funzione che trova il palindromo più grande ottenuto dal prodotto di due numeri a n cifre.

Esempio di chiamata alla funzione:
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

Il prodotto palindromo più grande di due numeri a 2 cifre deve essere uguale a 9009

```swift
    func testPalindrome1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

Il prodotto palindromo più grande di due numeri a 3 cifre deve essere uguale a 906609

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
