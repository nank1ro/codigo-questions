---
language: swift
exerciseType: 1
difficulty: 1
title: 算术平均值
---

# --description--

编写一个名为 `mean` 的函数来计算数字向量的_算术平均值_。

# --instructions--

编写一个返回数字向量平均值的函数。

函数调用示例：
```swift
print(mean([1, 2, 3]))
// prints 2.0
```

# --seed--

```swift
func mean() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`[1, 2, 3, 4, 5, 6, 7]` 的平均值必须等于 4.0

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

`[4, 5, 6]` 的平均值必须等于 5.0

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

`[12, 34, 56, 78]` 的平均值必须等于 45.0

```swift
    func test3() {
        XCTAssertEqual(mean([12, 34, 56, 78]), 45.0, "--err-t3--")
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
            ("test3", test3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
