---
language: swift
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

最初の6つの素数をリストすると: 2, 3, 5, 7, 11, 13 であり、6番目の素数は13であることがわかります。

# --instructions--

`n`番目の素数は何ですか？

# --seed--

```swift
func nthPrime(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`nthPrime(6)`は13を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(nthPrime(6), 13, "--err-t1--")
    }
```

`nthPrime(10)`は29を返すべきです。

```swift
    func test2() {
        XCTAssertEqual(nthPrime(10), 29, "--err-t2--")
    }
```

`nthPrime(100)`は541を返すべきです。

```swift
    func test3() {
        XCTAssertEqual(nthPrime(100), 541, "--err-t3--")
    }
```

`nthPrime(1000)`は7919を返すべきです。

```swift
    func test4() {
        XCTAssertEqual(nthPrime(1000), 7919, "--err-t4--")
    }
```

`nthPrime(10001)`は104743を返すべきです。

```swift
    func test5() {
        XCTAssertEqual(nthPrime(10001), 104743, "--err-t5--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func nthPrime(_ n: Int) -> Int {
    var pN = 2
    var step = 0
    while step < n {
        var isPrime = true
        let rootN = Int(Double(pN).squareRoot())
        for i in 2...max(2, rootN) {
            if i > rootN { break }
            if pN % i == 0 {
                isPrime = false
                break
            }
        }
        if isPrime { step += 1 }
        if step < n { pN += 1 }
    }
    return pN
}
```
