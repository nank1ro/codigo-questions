---
language: swift
exerciseType: 1
difficulty: 1
title: 10001st prime
---

# --description--

Listando os primeiros seis números primos: 2, 3, 5, 7, 11 e 13, podemos ver que o 6º primo é 13.

# --instructions--

Qual é o `n`-ésimo número primo?

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

`nthPrime(6)` deve retornar 13.

```swift
    func test1() {
        XCTAssertEqual(nthPrime(6), 13, "--err-t1--")
    }
```

`nthPrime(10)` deve retornar 29.

```swift
    func test2() {
        XCTAssertEqual(nthPrime(10), 29, "--err-t2--")
    }
```

`nthPrime(100)` deve retornar 541.

```swift
    func test3() {
        XCTAssertEqual(nthPrime(100), 541, "--err-t3--")
    }
```

`nthPrime(1000)` deve retornar 7919.

```swift
    func test4() {
        XCTAssertEqual(nthPrime(1000), 7919, "--err-t4--")
    }
```

`nthPrime(10001)` deve retornar 104743.

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
