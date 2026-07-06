---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

피보나치 수열의 각 새 항은 이전 두 항을 더하여 생성됩니다. 1과 2로 시작하면 처음 10개의 항은 `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`입니다.

# --instructions--

값이 `n`을 초과하지 않는 피보나치 수열의 항을 고려하여 짝수 값을 가진 항의 합을 구하세요.

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

함수는 짝수 값을 반환해야 합니다.

```swift
    func test1() {
        XCTAssertEqual(fibonacciEvenSum(10) % 2, 0, "--err-t1--")
    }
```

`fibonacciEvenSum(8)`은 10을 반환해야 합니다.

```swift
    func test2() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t2--")
    }
```

`fibonacciEvenSum(10)`은 10을 반환해야 합니다.

```swift
    func test3() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t3--")
    }
```

`fibonacciEvenSum(34)`은 44를 반환해야 합니다.

```swift
    func test4() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t4--")
    }
```

`fibonacciEvenSum(60)`은 44를 반환해야 합니다.

```swift
    func test5() {
        XCTAssertEqual(fibonacciEvenSum(60), 44, "--err-t5--")
    }
```

`fibonacciEvenSum(1000)`은 798을 반환해야 합니다.

```swift
    func test6() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t6--")
    }
```

`fibonacciEvenSum(100000)`은 60696을 반환해야 합니다.

```swift
    func test7() {
        XCTAssertEqual(fibonacciEvenSum(100000), 60696, "--err-t7--")
    }
```

`fibonacciEvenSum(4000000)`은 4613732를 반환해야 합니다.

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
