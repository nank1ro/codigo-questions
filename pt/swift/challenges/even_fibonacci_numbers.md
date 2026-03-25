---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Cada novo termo na sequência de Fibonacci é gerado somando os dois termos anteriores. Começando com 1 e 2, os primeiros 10 termos serão: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Considerando os termos da sequência de Fibonacci cujos valores não excedem `n`, encontre a soma dos termos de valor par.

# --seed--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Sua função deve retornar um valor par.

```swift
    func test1() {
        XCTAssertEqual(fibonacciEvenSum(10) % 2, 0, "--err-t1--")
    }
```

`fibonacciEvenSum(8)` deve retornar 10.

```swift
    func test2() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t2--")
    }
```

`fibonacciEvenSum(10)` deve retornar 10.

```swift
    func test3() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t3--")
    }
```

`fibonacciEvenSum(34)` deve retornar 44.

```swift
    func test4() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t4--")
    }
```

`fibonacciEvenSum(60)` deve retornar 44.

```swift
    func test5() {
        XCTAssertEqual(fibonacciEvenSum(60), 44, "--err-t5--")
    }
```

`fibonacciEvenSum(1000)` deve retornar 798.

```swift
    func test6() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t6--")
    }
```

`fibonacciEvenSum(100000)` deve retornar 60696.

```swift
    func test7() {
        XCTAssertEqual(fibonacciEvenSum(100000), 60696, "--err-t7--")
    }
```

`fibonacciEvenSum(4000000)` deve retornar 4613732.

```swift
    func test8() {
        XCTAssertEqual(fibonacciEvenSum(4000000), 4613732, "--err-t8--")
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
            ("test8", test8),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func fibonacciEvenSum(_ number: Int) -> Int {
    if number <= 1 { return 0 }
    var evenSum = 0
    var prevFibNum = 1
    var fibNum = 2
    while fibNum <= number {
        if fibNum % 2 == 0 {
            evenSum += fibNum
        }
        let next = prevFibNum + fibNum
        prevFibNum = fibNum
        fibNum = next
    }
    return evenSum
}
```
