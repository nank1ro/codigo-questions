---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

斐波那契数列中的每个新项都是由前两项相加得到的。从 1 和 2 开始，前 10 项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

考虑斐波那契数列中值不超过给定数字的项，求其中偶数项的总和。

# --instructions--

编写一个函数，返回所有不超过给定上限的偶数斐波那契数之和（包含上限）。

函数调用示例：
```swift
print(fibonacciEvenSum(8))
// prints 10
```

# --seed--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

不超过 8 的偶数斐波那契数之和必须等于 10

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

不超过 10 的偶数斐波那契数之和必须等于 10

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

不超过 34 的偶数斐波那契数之和必须等于 44

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

不超过 1000 的偶数斐波那契数之和必须等于 798

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

不超过 4000000 的偶数斐波那契数之和必须等于 4613732

```swift
    func testFibonacci5() {
        XCTAssertEqual(fibonacciEvenSum(4000000), 4613732, "--err-t5--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testFibonacci1", testFibonacci1),
            ("testFibonacci2", testFibonacci2),
            ("testFibonacci3", testFibonacci3),
            ("testFibonacci4", testFibonacci4),
            ("testFibonacci5", testFibonacci5),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {
    var sum = 0
    var a = 1
    var b = 2
    while a <= n {
        if a % 2 == 0 {
            sum += a
        }
        let temp = a + b
        a = b
        b = temp
    }
    return sum
}
```
