---
language: swift
exerciseType: 1
difficulty: 1
title: अंकगणितीय माध्य
---

# --description--

एक संख्यात्मक वेक्टर का _अंकगणितीय माध्य_ (arithmetic average) ज्ञात करने के लिए `mean` नामक एक फ़ंक्शन लिखें।

# --instructions--

एक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का माध्य लौटाए।

फ़ंक्शन कॉल का उदाहरण:
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

`[1, 2, 3, 4, 5, 6, 7]` का माध्य 4.0 के बराबर होना चाहिए

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

`[4, 5, 6]` का माध्य 5.0 के बराबर होना चाहिए

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

`[12, 34, 56, 78]` का माध्य 45.0 के बराबर होना चाहिए

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
