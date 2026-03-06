---
language: swift
exerciseType: 1
difficulty: 1
title: 산술 평균
---

# --description--

숫자 벡터의 _산술 평균_을 구하는 `mean`이라는 함수를 작성하십시오.

# --instructions--

숫자 벡터의 평균을 반환하는 함수를 작성하십시오.

함수 호출 예시:
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

`[1, 2, 3, 4, 5, 6, 7]`의 평균은 4.0이어야 합니다

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

`[4, 5, 6]`의 평균은 5.0이어야 합니다

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

`[12, 34, 56, 78]`의 평균은 45.0이어야 합니다

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
