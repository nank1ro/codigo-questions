---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

10未満の自然数のうち、3または5の倍数をリストすると、3、5、6、9が得られます。これらの倍数の合計は23です。

# --instructions--

指定されたパラメータ値`number`未満の3または5のすべての倍数の合計を求めてください。

# --seed--

```swift
func multiplesOf3and5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`multiplesOf3and5(10)`は23を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(multiplesOf3and5(10), 23, "--err-t1--")
    }
```

`multiplesOf3and5(1000)`は233168を返すべきです。

```swift
    func test2() {
        XCTAssertEqual(multiplesOf3and5(1000), 233168, "--err-t2--")
    }
```

`multiplesOf3and5(6987)`は11390208を返すべきです。

```swift
    func test3() {
        XCTAssertEqual(multiplesOf3and5(6987), 11390208, "--err-t3--")
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
func multiplesOf3and5(_ number: Int) -> Int {
    var total = 0
    for i in 0..<number {
        if i % 3 == 0 || i % 5 == 0 {
            total += i
        }
    }
    return total
}
```
