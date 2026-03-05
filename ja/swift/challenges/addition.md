---
language: swift
exerciseType: 1
difficulty: 1
title: 足し算
---

# --description--

2つの整数 `num1` と `num2` が与えられた場合、これら2つの数を足すプログラムを書いてください

# --instructions--

2つの数の合計を返す関数を書いてください。
> ヒント: `_`（アンダースコア）で引数ラベルを省略してください

関数呼び出しの例:
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

1と3の合計は4でなければなりません

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

200と210の合計は410でなければなりません

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

15と35の合計は50でなければなりません

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
