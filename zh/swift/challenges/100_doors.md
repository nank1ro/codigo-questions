---
language: swift
exerciseType: 1
difficulty: 1
title: 100扇门
---

# --description--

有100扇门排成一排，最初全部关闭。
你经过这些门100次。
第一次经过时，访问每扇门并"切换"门的状态（如果门是关闭的，就打开它；如果是打开的，就关闭它）。
第二次，只访问每第2扇门（即第2、4、6...扇门）并切换它。
第三次，访问每第3扇门（即第3、6、9...扇门），以此类推，直到你只访问第100扇门。

# --instructions--

实现一个函数来确定最后一次经过后门的状态。
将最终结果以数组形式返回，只有打开的门的编号才包含在数组中。
> 该方法必须能够处理可变数量的门。

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

给定100扇门，返回正确的打开门列表

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

给定10扇门，返回正确的打开门列表

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

给定950扇门，返回正确的打开门列表

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
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
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
