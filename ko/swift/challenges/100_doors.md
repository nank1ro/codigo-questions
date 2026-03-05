---
language: swift
exerciseType: 1
difficulty: 1
title: 100개의 문
---

# --description--

일렬로 100개의 문이 있으며, 모두 처음에는 닫혀 있습니다.
100번의 통과를 합니다.
첫 번째 통과에서는 모든 문을 방문하여 문을 '전환'합니다 (문이 닫혀 있으면 열고, 열려 있으면 닫습니다).
두 번째 통과에서는 2번째 문마다 방문하여 (즉, 2번, 4번, 6번, ... 문) 전환합니다.
세 번째 통과에서는 3번째 문마다 방문하여 (즉, 3번, 6번, 9번, ... 문) 전환하며, 100번째 문만 방문할 때까지 계속합니다.

# --instructions--

마지막 통과 후 문의 상태를 결정하는 함수를 구현하십시오.
최종 결과를 배열로 반환하되, 열려 있는 문의 번호만 배열에 포함하십시오.
> 이 메서드는 가변적인 수의 문에 대해 작동할 수 있어야 합니다.

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

100개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

10개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

950개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

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
