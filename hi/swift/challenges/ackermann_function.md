---
language: swift
exerciseType: 1
difficulty: 1
title: एकरमन फलन
---

# --description--

एकरमन फलन एक पुनरावर्ती फलन (recursive function) का एक उत्कृष्ट उदाहरण है, जो विशेष रूप से इसलिए उल्लेखनीय है क्योंकि यह एक आदिम पुनरावर्ती फलन (primitive recursive function) नहीं है। इसका मान बहुत तेज़ी से बढ़ता है, और इसके कॉल ट्री का आकार भी।

एकरमन फलन को आमतौर पर इस प्रकार परिभाषित किया जाता है:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

इसके आर्गुमेंट कभी ऋणात्मक नहीं होते और यह हमेशा समाप्त होता है

# --instructions--

एक फ़ंक्शन लिखें जो एकरमन फलन का मान लौटाए।

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

`ack(0, 0)` को 1 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(ack(0, 0), 1, "--err-t1--")
    }
```

`ack(1, 1)` को 3 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(ack(1, 1), 3, "--err-t2--")
    }
```

`ack(2, 5)` को 13 लौटाना चाहिए।

```swift
    func test3() {
        XCTAssertEqual(ack(2, 5), 13, "--err-t3--")
    }
```

`ack(3, 3)` को 61 लौटाना चाहिए।

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
