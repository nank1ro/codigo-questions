---
language: swift
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

पहले छह अभाज्य संख्याओं को सूचीबद्ध करने पर: 2, 3, 5, 7, 11 और 13, हम देख सकते हैं कि 6वीं अभाज्य संख्या 13 है।

# --instructions--

`n`वीं अभाज्य संख्या क्या है?

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

`nthPrime(6)` को 13 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(nthPrime(6), 13, "--err-t1--")
    }
```

`nthPrime(10)` को 29 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(nthPrime(10), 29, "--err-t2--")
    }
```

`nthPrime(100)` को 541 लौटाना चाहिए।

```swift
    func test3() {
        XCTAssertEqual(nthPrime(100), 541, "--err-t3--")
    }
```

`nthPrime(1000)` को 7919 लौटाना चाहिए।

```swift
    func test4() {
        XCTAssertEqual(nthPrime(1000), 7919, "--err-t4--")
    }
```

`nthPrime(10001)` को 104743 लौटाना चाहिए।

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
