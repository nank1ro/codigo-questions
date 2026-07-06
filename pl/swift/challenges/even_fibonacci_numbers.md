---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Każdy nowy wyraz ciągu Fibonacciego jest generowany przez dodanie dwóch poprzednich wyrazów. Zaczynając od 1 i 2, pierwsze 10 wyrazów to: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Biorąc pod uwagę wyrazy ciągu Fibonacciego, których wartości nie przekraczają podanej liczby, znajdź sumę wyrazów o wartościach parzystych.

# --instructions--

Napisz funkcję, która zwraca sumę wszystkich parzystych liczb Fibonacciego do podanego limitu włącznie.

Przykład wywołania funkcji:
```swift
print(fibonacciEvenSum(8))
// prints 10
```

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

Suma parzystych liczb Fibonacciego do 8 musi być równa 10

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

Suma parzystych liczb Fibonacciego do 10 musi być równa 10

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

Suma parzystych liczb Fibonacciego do 34 musi być równa 44

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

Suma parzystych liczb Fibonacciego do 1000 musi być równa 798

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

Suma parzystych liczb Fibonacciego do 4000000 musi być równa 4613732

```swift
    func testFibonacci5() {
        XCTAssertEqual(fibonacciEvenSum(4000000), 4613732, "--err-t5--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testFibonacci1", testFibonacci1),
            ("testFibonacci2", testFibonacci2),
            ("testFibonacci3", testFibonacci3),
            ("testFibonacci4", testFibonacci4),
            ("testFibonacci5", testFibonacci5),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {
    var sum = 0
    var a = 1
    var b = 2
    while a <= n {
        if a % 2 == 0 {
            sum += a
        }
        let temp = a + b
        a = b
        b = temp
    }
    return sum
}
```
