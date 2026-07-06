---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

勾股数是满足 a² + b² = c² 的三个自然数 a < b < c 的组合。存在唯一一组勾股数满足 a + b + c = 1000。求乘积 a × b × c。

# --instructions--

编写一个函数，求满足 a + b + c = n 的勾股数组的乘积 a × b × c。

函数调用示例：
```swift
print(specialPythagoreanTriplet(12))
// prints 60
```

# --seed--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

满足 a + b + c = 12 的勾股数组乘积必须等于 60

```swift
    func testPythagorean1() {
        XCTAssertEqual(specialPythagoreanTriplet(12), 60, "--err-t1--")
    }
```

满足 a + b + c = 1000 的勾股数组乘积必须等于 31875000

```swift
    func testPythagorean2() {
        XCTAssertEqual(specialPythagoreanTriplet(1000), 31875000, "--err-t2--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testPythagorean1", testPythagorean1),
            ("testPythagorean2", testPythagorean2),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
