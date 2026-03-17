---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Каждый новый член последовательности Фибоначчи получается сложением двух предыдущих членов. Начиная с 1 и 2, первые 10 членов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Рассматривая члены последовательности Фибоначчи, значения которых не превышают заданного числа, найдите сумму членов с чётными значениями.

# --instructions--

Напишите функцию, которая возвращает сумму всех чётных чисел Фибоначчи до заданного предела включительно.

Пример вызова функции:
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

Сумма чётных чисел Фибоначчи до 8 должна быть равна 10

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

Сумма чётных чисел Фибоначчи до 10 должна быть равна 10

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

Сумма чётных чисел Фибоначчи до 34 должна быть равна 44

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

Сумма чётных чисел Фибоначчи до 1000 должна быть равна 798

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

Сумма чётных чисел Фибоначчи до 4000000 должна быть равна 4613732

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
