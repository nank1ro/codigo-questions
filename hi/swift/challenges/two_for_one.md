---
language: swift
exerciseType: 1
difficulty: 1
title: दो में से एक
---

# --description--

एक नाम दिया गया है, इस संदेश के साथ एक स्ट्रिंग लौटाएं:
`One for X, one for me.`
जहां `X` दिया गया नाम है।
हालांकि, यदि नाम नहीं दिया गया है, तो यह स्ट्रिंग लौटाएं:
`One for you, one for me.`

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

**इनपुट**: `Walter`
**आउटपुट**: `One for Walter, one for me.`

**इनपुट**: `James`
**आउटपुट**: `One for James, one for me.`

**इनपुट**: `Martha`
**आउटपुट**: `One for Martha, one for me.`

# --seed--

```swift
func twoForOne(name: String) -> String {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

कोई नाम नहीं दिया गया

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

नाम के रूप में "James" पास करें

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

नाम के रूप में "Martha" पास करें

```swift
    func testAnotherNameGiven() {
        let expected = "One for Martha, one for me."
        XCTAssertEqual(twoForOne(name: "Martha"), expected, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testNoNameGiven", testNoNameGiven),
            ("testANameGiven", testANameGiven),
            ("testAnotherNameGiven", testAnotherNameGive),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func twoForOne(name: String? = nil) -> String {
    if let validName = name {
        return "One for \(validName), one for me."
    }
    return "One for you, one for me."
}
```


