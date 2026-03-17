---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

पाइथागोरियन त्रिक तीन प्राकृतिक संख्याओं का एक समुच्चय है, `a` < `b` < `c`, जिसके लिए, <latex>a^2 + b^2 = c^2</latex>

उदाहरण के लिए, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>

एक ऐसा पाइथागोरियन त्रिक है जिसके लिए `a` + `b` + `c` = 1000।

# --instructions--

ऐसा गुणनफल `abc` ज्ञात करें जिसके लिए `a` + `b` + `c` = `n`।

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

`specialPythagoreanTriplet(24)` को 480 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(specialPythagoreanTriplet(24), 480, "--err-t1--")
    }
```

`specialPythagoreanTriplet(120)` को 49920, 55080 या 60000 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertTrue([49920, 55080, 60000].contains(specialPythagoreanTriplet(120)), "--err-t2--")
    }
```

`specialPythagoreanTriplet(1000)` को 31875000 लौटाना चाहिए।

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
