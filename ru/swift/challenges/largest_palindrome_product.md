---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Палиндромное число читается одинаково в обоих направлениях. Наибольший палиндром, полученный как произведение двух 2-значных чисел, — это 9009 = 91 × 99.

# --instructions--

Напишите функцию, которая находит наибольший палиндром, являющийся произведением двух n-значных чисел.

Пример вызова функции:
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

Наибольший палиндром из произведения двух 2-значных чисел должен быть равен 9009

```swift
    func testPalindrome1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

Наибольший палиндром из произведения двух 3-значных чисел должен быть равен 906609

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
