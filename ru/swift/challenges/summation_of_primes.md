---
language: swift
exerciseType: 1
difficulty: 2
title: Summation of primes
---

# --description--

Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

# --instructions--

Напишите функцию, которая находит сумму всех простых чисел меньше заданного числа.

Пример вызова функции:
```swift
print(primeSummation(10))
// prints 17
```

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

Сумма всех простых чисел меньше 10 должна быть равна 17

```swift
    func testPrimeSummation1() {
        XCTAssertEqual(primeSummation(10), 17, "--err-t1--")
    }
```

Сумма всех простых чисел меньше 1000 должна быть равна 76127

```swift
    func testPrimeSummation2() {
        XCTAssertEqual(primeSummation(1000), 76127, "--err-t2--")
    }
```

Сумма всех простых чисел меньше 100000 должна быть равна 454396537

```swift
    func testPrimeSummation3() {
        XCTAssertEqual(primeSummation(100000), 454396537, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testPrimeSummation1", testPrimeSummation1),
            ("testPrimeSummation2", testPrimeSummation2),
            ("testPrimeSummation3", testPrimeSummation3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func primeSummation(_ n: Int) -> Int {
    var sieve = [Bool](repeating: true, count: n)
    if n > 0 { sieve[0] = false }
    if n > 1 { sieve[1] = false }
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
    return sieve.indices.filter { sieve[$0] }.reduce(0, +)
}
```
