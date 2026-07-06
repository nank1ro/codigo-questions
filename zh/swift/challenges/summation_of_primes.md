---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

10 以下所有质数之和为 2 + 3 + 5 + 7 = 17。

# --instructions--

编写一个函数，求所有小于给定数字的质数之和。

函数调用示例：
```swift
print(primeSummation(10))
// prints 17
```

# --seed--

```swift
func primeSummation(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

10 以下所有质数之和必须等于 17

```swift
    func testPrimeSummation1() {
        XCTAssertEqual(primeSummation(10), 17, "--err-t1--")
    }
```

1000 以下所有质数之和必须等于 76127

```swift
    func testPrimeSummation2() {
        XCTAssertEqual(primeSummation(1000), 76127, "--err-t2--")
    }
```

100000 以下所有质数之和必须等于 454396537

```swift
    func testPrimeSummation3() {
        XCTAssertEqual(primeSummation(100000), 454396537, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testPrimeSummation1", testPrimeSummation1),
            ("testPrimeSummation2", testPrimeSummation2),
            ("testPrimeSummation3", testPrimeSummation3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func primeSummation(_ n: Int) -> Int {
    var sieve = [Bool](repeating: true, count: n)
    if n > 0 { sieve[0] = false }
    if n > 1 { sieve[1] = false }
    var i = 2
    while i * i < n {
        if sieve[i] {
            var j = i * i
            while j < n {
                sieve[j] = false
                j += i
            }
        }
        i += 1
    }
    return sieve.indices.filter { sieve[$0] }.reduce(0, +)
}
```
