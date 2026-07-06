---
language: swift
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

एक पैलिंड्रोमिक संख्या दोनों दिशाओं में समान पढ़ी जाती है। दो 2-अंकीय संख्याओं के गुणनफल से बना सबसे बड़ा पैलिंड्रोम 9009 = 91 × 99 है।

# --instructions--

दो `n`-अंकीय संख्याओं के गुणनफल से बना सबसे बड़ा पैलिंड्रोम ज्ञात करें।

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

`largestPalindromeProduct(2)` को 9009 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(largestPalindromeProduct(2), 9009, "--err-t1--")
    }
```

`largestPalindromeProduct(3)` को 906609 लौटाना चाहिए।

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
