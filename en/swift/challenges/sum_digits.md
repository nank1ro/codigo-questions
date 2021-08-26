---
language: swift
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

You're given an integer `N`.
Write a program to calculate the sum of all the digits of N

# --instructions--

Return the sum of digits of `N`.
> HINT: omit the argument label with the `_` (underscore)

Example of function call:
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

class SumDigitsTests: XCTestCase {
```

# --asserts--

The sum of the digits of 12345 is 15

```swift
    func testSumOfDigits1() {
        XCTAssertEqual(sumDigits(12345), 15, "--err-t1--")
    }
```

The sum of the digits of 57253 is 22

```swift
    func testSumOfDigits2() {
        XCTAssertEqual(sumDigits(57253), 22, "--err-t2--")
    }
```

The sum of the digits of 122 is 5

```swift
    func testSumOfDigits3() {
        XCTAssertEqual(sumDigits(122), 5, "--err-t3--")
    }
```

The sum of the digits of 91979997 is 60

```swift
    func testSumOfDigits4() {
        XCTAssertEqual(sumDigits(91979997), 60, "--err-t4--")
    }
```

The sum of the digits of 2147483647 is 46

```swift
    func testSumOfDigits5() {
        XCTAssertEqual(sumDigits(2147483647), 46, "--err-t5--")
    }
```

# --after-asserts--

```swift
}

extension SumDigitsTests {
    static var allTests : [(String, (SumDigitsTests) -> () throws -> Void)] {
        return [
            ("testSumOfDigits1", testSumOfDigits1),
            ("testSumOfDigits2", testSumOfDigits2),
            ("testSumOfDigits3", testSumOfDigits3),
            ("testSumOfDigits4", testSumOfDigits4),
            ("testSumOfDigits5", testSumOfDigits5),
        ]
    }
}

XCTMain([testCase(SumDigitsTests.allTests)])
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

