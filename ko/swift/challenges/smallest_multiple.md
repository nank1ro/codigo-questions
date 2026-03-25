---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520은 1부터 10까지의 각 숫자로 나머지 없이 나눌 수 있는 가장 작은 수입니다.

# --instructions--

1부터 `n`까지의 모든 숫자로 균등하게 나눌 수 있는 가장 작은 양수는 무엇입니까?

# --seed--

```swift
func smallestMultiple(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`smallestMultiple(5)`는 60을 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

`smallestMultiple(7)`는 420을 반환해야 합니다.

```swift
    func test2() {
        XCTAssertEqual(smallestMultiple(7), 420, "--err-t2--")
    }
```

`smallestMultiple(10)`는 2520을 반환해야 합니다.

```swift
    func test3() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t3--")
    }
```

`smallestMultiple(13)`는 360360을 반환해야 합니다.

```swift
    func test4() {
        XCTAssertEqual(smallestMultiple(13), 360360, "--err-t4--")
    }
```

`smallestMultiple(20)`는 232792560을 반환해야 합니다.

```swift
    func test5() {
        XCTAssertEqual(smallestMultiple(20), 232792560, "--err-t5--")
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
            ("test4", test4),
            ("test5", test5),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    var result = 1
    for i in 2...n {
        result = lcm(result, i)
    }
    return result
}
```
