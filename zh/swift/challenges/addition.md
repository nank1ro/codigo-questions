---
language: swift
exerciseType: 1
difficulty: 1
title: 加法
---

# --description--

给定两个整数 `num1` 和 `num2`，编写一个程序将这两个数相加

# --instructions--

编写一个返回两个数之和的函数。
> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
```swift
print(addition(1, 2))
// prints 3
```

# --seed--

```swift
func addition() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

1 和 3 的和必须等于 4

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

200 和 210 的和必须等于 410

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

15 和 35 的和必须等于 50

```swift
    func testAddition3() {
        XCTAssertEqual(addition(15, 35), 50, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testAddition1", testAddition1),
            ("testAddition2", testAddition2),
            ("testAddition3", testAddition3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
