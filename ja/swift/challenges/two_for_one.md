---
language: swift
exerciseType: 1
difficulty: 1
title: 2対1
---

# --description--

名前が与えられた場合、次のメッセージを含む文字列を返します:
`One for X, one for me.`
ここで `X` は与えられた名前です。
ただし、名前がない場合は、次の文字列を返します:
`One for you, one for me.`

# --instructions--

正しい文字列を返す関数を書いてください。例:

**入力**: `Walter`
**出力**: `One for Walter, one for me.`

**入力**: `James`
**出力**: `One for James, one for me.`

**入力**: `Martha`
**出力**: `One for Martha, one for me.`

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

名前が指定されていない場合

```swift
    func testNoNameGiven() {
        let expected = "One for you, one for me."
        XCTAssertEqual(twoForOne(), expected, "--err-t1--")
    }
```

名前に "James" を渡す

```swift
    func testANameGiven() {
        let expected = "One for James, one for me."
        XCTAssertEqual(twoForOne(name: "James"), expected, "--err-t2--")
    }
```

名前に "Martha" を渡す

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


