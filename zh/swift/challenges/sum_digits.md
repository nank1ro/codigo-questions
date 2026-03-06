---
language: swift
exerciseType: 1
difficulty: 1
title: 数字之和
---

# --description--

给定一个整数 `N`。
编写一个程序来计算 N 的所有数字之和

# --instructions--

返回 `N` 的各位数字之和。
> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
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

12345 的各位数字之和是 15

```swift
    func testSumOfDigits1() {
        XCTAssertEqual(sumDigits(12345), 15, "--err-t1--")
    }
```

57253 的各位数字之和是 22

```swift
    func testSumOfDigits2() {
        XCTAssertEqual(sumDigits(57253), 22, "--err-t2--")
    }
```

122 的各位数字之和是 5

```swift
    func testSumOfDigits3() {
        XCTAssertEqual(sumDigits(122), 5, "--err-t3--")
    }
```

91979997 的各位数字之和是 60

```swift
    func testSumOfDigits4() {
        XCTAssertEqual(sumDigits(91979997), 60, "--err-t4--")
    }
```

2147483647 的各位数字之和是 46

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

