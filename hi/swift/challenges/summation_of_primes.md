---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

10 से कम अभाज्य संख्याओं का योग 2 + 3 + 5 + 7 = 17 है।

# --instructions--

`n` से कम सभी अभाज्य संख्याओं का योग ज्ञात करें।

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

`primeSummation(17)` को 41 लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(primeSummation(17), 41, "--err-t1--")
    }
```

`primeSummation(2001)` को 277050 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(primeSummation(2001), 277050, "--err-t2--")
    }
```

`primeSummation(140759)` को 873608362 लौटाना चाहिए।

```swift
    func test3() {
        XCTAssertEqual(primeSummation(140759), 873608362, "--err-t3--")
    }
```

`primeSummation(2000000)` को 142913828922 लौटाना चाहिए।

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
