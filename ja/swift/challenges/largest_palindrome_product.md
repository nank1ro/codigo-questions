---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

回文数は両方向から同じように読めます。2桁の数字2つの積から作られる最大の回文数は 9009 = 91 × 99 です。

# --instructions--

`n`桁の数字2つの積から作られる最大の回文数を求めてください。

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

`largestPalindromeProduct(2)`は9009を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

`largestPalindromeProduct(3)`は906609を返すべきです。

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
