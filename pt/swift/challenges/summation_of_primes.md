---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

A soma dos primos abaixo de 10 é 2 + 3 + 5 + 7 = 17.

# --instructions--

Encontre a soma de todos os primos abaixo de `n`.

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

`primeSummation(17)` deve retornar 41.

```swift
    func test1() {
        XCTAssertEqual(primeSummation(17), 41, "--err-t1--")
    }
```

`primeSummation(2001)` deve retornar 277050.

```swift
    func test2() {
        XCTAssertEqual(primeSummation(2001), 277050, "--err-t2--")
    }
```

`primeSummation(140759)` deve retornar 873608362.

```swift
    func test3() {
        XCTAssertEqual(primeSummation(140759), 873608362, "--err-t3--")
    }
```

`primeSummation(2000000)` deve retornar 142913828922.

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
