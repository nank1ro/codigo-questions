---
language: swift
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

列出前六个质数：2, 3, 5, 7, 11 和 13，可以看出第 6 个质数是 13。

# --instructions--

编写一个函数，返回第 n 个质数。

函数调用示例：
```swift
print(nthPrime(6))
// prints 13
```

# --seed--

```swift
func nthPrime(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

第 6 个质数必须等于 13

```swift
    func testNthPrime1() {
        XCTAssertEqual(nthPrime(6), 13, "--err-t1--")
    }
```

第 10 个质数必须等于 29

```swift
    func testNthPrime2() {
        XCTAssertEqual(nthPrime(10), 29, "--err-t2--")
    }
```

第 1000 个质数必须等于 7919

```swift
    func testNthPrime3() {
        XCTAssertEqual(nthPrime(1000), 7919, "--err-t3--")
    }
```

第 10001 个质数必须等于 104743

```swift
    func testNthPrime4() {
        XCTAssertEqual(nthPrime(10001), 104743, "--err-t4--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testNthPrime1", testNthPrime1),
            ("testNthPrime2", testNthPrime2),
            ("testNthPrime3", testNthPrime3),
            ("testNthPrime4", testNthPrime4),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func nthPrime(_ n: Int) -> Int {
    func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num == 2 { return true }
        if num % 2 == 0 { return false }
        var i = 3
        while i * i <= num {
            if num % i == 0 { return false }
            i += 2
        }
        return true
    }
    var count = 0
    var candidate = 1
    while count < n {
        candidate += 1
        if isPrime(candidate) {
            count += 1
        }
    }
    return candidate
}
```
