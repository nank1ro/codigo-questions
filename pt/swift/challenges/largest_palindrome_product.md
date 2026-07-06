---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Um número palíndromo é lido da mesma forma nos dois sentidos. O maior palíndromo feito a partir do produto de dois números de 2 dígitos é 9009 = 91 × 99.

# --instructions--

Encontre o maior palíndromo feito a partir do produto de dois números de `n` dígitos.

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

`largestPalindromeProduct(2)` deve retornar 9009.

```swift
    func test1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

`largestPalindromeProduct(3)` deve retornar 906609.

```swift
    func test2() {
        XCTAssertEqual(largestPalindromeProduct(3), 906609, "--err-t2--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func largestPalindromeProduct(_ digit: Int) -> Int {
    let start = 1
    let end = Int(pow(10.0, Double(digit))) - 1
    var palindrome = [Int]()
    for i in start...end {
        for j in start...end {
            let product = i * j
            let s = String(product)
            if s == String(s.reversed()) {
                palindrome.append(product)
            }
        }
    }
    return palindrome.max() ?? 0
}
```
