---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

フィボナッチ数列の各新しい項は、前の2つの項を加算することで生成されます。1と2から始めると、最初の10項は `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...` となります。

# --instructions--

`n`を超えない値を持つフィボナッチ数列の項を考え、偶数値の項の合計を求めてください。

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

関数は偶数値を返すべきです。

```swift
    func test1() {
        XCTAssertEqual(fibonacciEvenSum(10) % 2, 0, "--err-t1--")
    }
```

`fibonacciEvenSum(8)`は10を返すべきです。

```swift
    func test2() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t2--")
    }
```

`fibonacciEvenSum(10)`は10を返すべきです。

```swift
    func test3() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t3--")
    }
```

`fibonacciEvenSum(34)`は44を返すべきです。

```swift
    func test4() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t4--")
    }
```

`fibonacciEvenSum(60)`は44を返すべきです。

```swift
    func test5() {
        XCTAssertEqual(fibonacciEvenSum(60), 44, "--err-t5--")
    }
```

`fibonacciEvenSum(1000)`は798を返すべきです。

```swift
    func test6() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t6--")
    }
```

`fibonacciEvenSum(100000)`は60696を返すべきです。

```swift
    func test7() {
        XCTAssertEqual(fibonacciEvenSum(100000), 60696, "--err-t7--")
    }
```

`fibonacciEvenSum(4000000)`は4613732を返すべきです。

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
