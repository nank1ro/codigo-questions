---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

13195 的质因数为 5、7、13 和 29。13195 的最大质因数为 29。

# --instructions--

编写一个函数，返回给定数字的最大质因数。

函数调用示例：
```swift
print(largestPrimeFactor(13195))
// prints 29
```

# --seed--

```swift
func largestPrimeFactor(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

2 的最大质因数必须等于 2

```swift
    func testLargestPrime1() {
        XCTAssertEqual(largestPrimeFactor(2), 2, "--err-t1--")
    }
```

13195 的最大质因数必须等于 29

```swift
    func testLargestPrime2() {
        XCTAssertEqual(largestPrimeFactor(13195), 29, "--err-t2--")
    }
```

600851475143 的最大质因数必须等于 6857

```swift
    func testLargestPrime3() {
        XCTAssertEqual(largestPrimeFactor(600851475143), 6857, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testLargestPrime1", testLargestPrime1),
            ("testLargestPrime2", testLargestPrime2),
            ("testLargestPrime3", testLargestPrime3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func largestPrimeFactor(_ number: Int) -> Int {
    var n = number
    var largest = 1
    var factor = 2
    while factor * factor <= n {
        while n % factor == 0 {
            largest = factor
            n /= factor
        }
        factor += 1
    }
    if n > 1 {
        largest = n
    }
    return largest
}
```
