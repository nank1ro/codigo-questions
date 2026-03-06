---
language: swift
exerciseType: 1
difficulty: 1
title: 아커만 함수
---

# --description--

아커만 함수는 재귀 함수의 고전적인 예로, 특히 원시 재귀 함수가 아니라는 점에서 주목할 만합니다. 그 값은 매우 빠르게 증가하며, 호출 트리의 크기도 마찬가지입니다.

아커만 함수는 보통 다음과 같이 정의됩니다:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

인수는 절대 음수가 아니며 항상 종료됩니다

# --instructions--

아커만 함수의 값을 반환하는 함수를 작성하십시오.

# --seed--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`ack(0, 0)`은 1을 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(ack(0, 0), 1, "--err-t1--")
    }
```

`ack(1, 1)`은 3을 반환해야 합니다.

```swift
    func test2() {
        XCTAssertEqual(ack(1, 1), 3, "--err-t2--")
    }
```

`ack(2, 5)`는 13을 반환해야 합니다.

```swift
    func test3() {
        XCTAssertEqual(ack(2, 5), 13, "--err-t3--")
    }
```

`ack(3, 3)`은 61을 반환해야 합니다.

```swift
    func test4() {
        XCTAssertEqual(ack(3, 3), 61, "--err-t4--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
