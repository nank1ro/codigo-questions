---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

10未満の素数の合計は 2 + 3 + 5 + 7 = 17 です。

# --instructions--

`n`未満のすべての素数の合計を求めてください。

# --seed--

```swift
func primeSummation(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`primeSummation(17)`は41を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(primeSummation(17), 41, "--err-t1--")
    }
```

`primeSummation(2001)`は277050を返すべきです。

```swift
    func test2() {
        XCTAssertEqual(primeSummation(2001), 277050, "--err-t2--")
    }
```

`primeSummation(140759)`は873608362を返すべきです。

```swift
    func test3() {
        XCTAssertEqual(primeSummation(140759), 873608362, "--err-t3--")
    }
```

`primeSummation(2000000)`は142913828922を返すべきです。

```swift
    func test4() {
        XCTAssertEqual(primeSummation(2000000), 142913828922, "--err-t4--")
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
func primeSummation(_ n: Int) -> Int {
    guard n > 2 else { return 0 }
    var sieve = [Bool](repeating: true, count: n)
    sieve[0] = false
    sieve[1] = false
    var i = 2
    while i * i < n {
        if sieve[i] {
            var j = i * i
            while j < n {
                sieve[j] = false
                j += i
            }
        }
        i += 1
    }
    return sieve.enumerated().filter { $0.element }.reduce(0) { $0 + $1.offset }
}
```
