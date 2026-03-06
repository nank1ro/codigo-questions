---
language: swift
exerciseType: 1
difficulty: 1
title: हैलो वर्ल्ड!
---

# --description--

__"Hello, World!"__ किसी नई भाषा या वातावरण में प्रोग्रामिंग शुरू करने के लिए पारंपरिक पहला प्रोग्राम है।

# --instructions--

एक फ़ंक्शन लिखें जो स्ट्रिंग "Hello, World!" लौटाए।

# --seed--

```swift
func hello() -> String {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

फ़ंक्शन को "Hello, World!" लौटाना चाहिए।

```swift
    func testHi() {
        let expected = "Hello, World!"
        XCTAssertEqual(hello(), expected, "--err-t1--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testHi", testHi),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func hello() -> String {
    return "Hello, World!"
}
```

