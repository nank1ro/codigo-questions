---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Eine Palindromzahl liest sich von vorne und hinten gleich. Das größte Palindrom, das aus dem Produkt zweier 2-stelliger Zahlen gebildet wird, ist 9009 = 91 × 99.

# --instructions--

Schreibe eine Funktion, die das größte Palindrom findet, das aus dem Produkt zweier n-stelliger Zahlen gebildet wird.

Beispiel eines Funktionsaufrufs:
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

Das größte Palindromprodukt zweier 2-stelliger Zahlen muss 9009 ergeben

```swift
    func testPalindrome1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

Das größte Palindromprodukt zweier 3-stelliger Zahlen muss 906609 ergeben

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
