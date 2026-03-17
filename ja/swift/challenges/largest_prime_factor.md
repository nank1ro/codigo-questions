---
language: swift
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

13195の素因数は5、7、13、29です。

# --instructions--

与えられた`number`の最大の素因数は何ですか？

# --seed--

```swift
func largestPrimeFactor(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`largestPrimeFactor(2)`は2を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(largestPrimeFactor(2), 2, "--err-t1--")
    }
```

`largestPrimeFactor(3)`は3を返すべきです。

```swift
    func test2() {
        XCTAssertEqual(largestPrimeFactor(3), 3, "--err-t2--")
    }
```

`largestPrimeFactor(5)`は5を返すべきです。

```swift
    func test3() {
        XCTAssertEqual(largestPrimeFactor(5), 5, "--err-t3--")
    }
```

`largestPrimeFactor(7)`は7を返すべきです。

```swift
    func test4() {
        XCTAssertEqual(largestPrimeFactor(7), 7, "--err-t4--")
    }
```

`largestPrimeFactor(8)`は2を返すべきです。

```swift
    func test5() {
        XCTAssertEqual(largestPrimeFactor(8), 2, "--err-t5--")
    }
```

`largestPrimeFactor(13195)`は29を返すべきです。

```swift
    func test6() {
        XCTAssertEqual(largestPrimeFactor(13195), 29, "--err-t6--")
    }
```

`largestPrimeFactor(600851475143)`は6857を返すべきです。

```swift
    func test7() {
        XCTAssertEqual(largestPrimeFactor(600851475143), 6857, "--err-t7--")
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
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func largestPrimeFactor(_ number: Int) -> Int {
    var largestFactor = number
    var i = 2
    while i * i <= largestFactor {
        if largestFactor % i == 0 {
            largestFactor /= i
        } else {
            i += 1
        }
    }
    return largestFactor
}
```
