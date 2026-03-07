---
language: swift
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Dana jest liczba całkowita `N`.
Napisz program obliczający sumę wszystkich cyfr liczby N.

# --instructions--

Zwróć sumę cyfr liczby `N`.
> WSKAZÓWKA: pomiń etykietę argumentu używając `_` (podkreślnika)

Przykład wywołania funkcji:
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

Suma cyfr liczby 12345 wynosi 15

```swift
    func testSumOfDigits1() {
        XCTAssertEqual(sumDigits(12345), 15, "--err-t1--")
    }
```

Suma cyfr liczby 57253 wynosi 22

```swift
    func testSumOfDigits2() {
        XCTAssertEqual(sumDigits(57253), 22, "--err-t2--")
    }
```

Suma cyfr liczby 122 wynosi 5

```swift
    func testSumOfDigits3() {
        XCTAssertEqual(sumDigits(122), 5, "--err-t3--")
    }
```

Suma cyfr liczby 91979997 wynosi 60

```swift
    func testSumOfDigits4() {
        XCTAssertEqual(sumDigits(91979997), 60, "--err-t4--")
    }
```

Suma cyfr liczby 2147483647 wynosi 46

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

