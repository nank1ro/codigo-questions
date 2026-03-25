---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

회문 수는 양방향으로 동일하게 읽힙니다. 두 2자리 숫자의 곱으로 만들어진 가장 큰 회문 수는 9009 = 91 × 99입니다.

# --instructions--

두 `n`자리 숫자의 곱으로 만들어진 가장 큰 회문 수를 구하세요.

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

`largestPalindromeProduct(2)`는 9009를 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

`largestPalindromeProduct(3)`는 906609를 반환해야 합니다.

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
