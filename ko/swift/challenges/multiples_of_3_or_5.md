---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

10 미만의 자연수 중 3 또는 5의 배수를 나열하면 3, 5, 6, 9입니다. 이 배수들의 합은 23입니다.

# --instructions--

주어진 매개변수 값 `number` 미만의 3 또는 5의 모든 배수의 합을 구하세요.

# --seed--

```swift
func multiplesOf3and5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`multiplesOf3and5(10)`은 23을 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(multiplesOf3and5(10), 23, "--err-t1--")
    }
```

`multiplesOf3and5(1000)`은 233168을 반환해야 합니다.

```swift
    func test2() {
        XCTAssertEqual(multiplesOf3and5(1000), 233168, "--err-t2--")
    }
```

`multiplesOf3and5(6987)`은 11390208을 반환해야 합니다.

```swift
    func test3() {
        XCTAssertEqual(multiplesOf3and5(6987), 11390208, "--err-t3--")
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
func multiplesOf3and5(_ number: Int) -> Int {
    var total = 0
    for i in 0..<number {
        if i % 3 == 0 || i % 5 == 0 {
            total += i
        }
    }
    return total
}
```
