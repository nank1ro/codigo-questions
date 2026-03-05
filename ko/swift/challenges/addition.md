---
language: swift
exerciseType: 1
difficulty: 1
title: 덧셈
---

# --description--

두 정수 `num1`과 `num2`가 주어졌을 때, 이 두 수를 더하는 프로그램을 작성하십시오

# --instructions--

두 수의 합을 반환하는 함수를 작성하십시오.
> 힌트: `_` (밑줄)로 인수 레이블을 생략하십시오

함수 호출 예시:
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

1과 3의 합은 4여야 합니다

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

200과 210의 합은 410이어야 합니다

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

15와 35의 합은 50이어야 합니다

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
