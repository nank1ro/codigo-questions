---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

피타고라스 삼원수는 <latex>a^2 + b^2 = c^2</latex>를 만족하는 세 자연수 `a` < `b` < `c`의 집합입니다.

예를 들어, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

`a` + `b` + `c` = 1000을 만족하는 피타고라스 삼원수가 정확히 하나 존재합니다.

# --instructions--

`a` + `b` + `c` = `n`이 되는 곱 `abc`를 구하세요.

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

`specialPythagoreanTriplet(24)`는 480을 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(specialPythagoreanTriplet(24), 480, "--err-t1--")
    }
```

`specialPythagoreanTriplet(120)`는 49920, 55080 또는 60000을 반환해야 합니다.

```swift
    func test2() {
        XCTAssertTrue([49920, 55080, 60000].contains(specialPythagoreanTriplet(120)), "--err-t2--")
    }
```

`specialPythagoreanTriplet(1000)`는 31875000을 반환해야 합니다.

```swift
    func test3() {
        XCTAssertEqual(specialPythagoreanTriplet(1000), 31875000, "--err-t3--")
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
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1...(n / 3) {
        for b in (a + 1)...(n / 2) {
            let cSquared = a * a + b * b
            let c = Int(Double(cSquared).squareRoot())
            if c * c == cSquared && a + b + c == n {
                return a * b * c
            }
        }
    }
    return 0
}
```
