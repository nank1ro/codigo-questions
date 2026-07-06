---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Cada nuevo término de la sucesión de Fibonacci se genera sumando los dos términos anteriores. Comenzando con 1 y 2, los primeros 10 términos serán: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando los términos de la sucesión de Fibonacci cuyos valores no superan el número dado, encuentra la suma de los términos de valor par.

# --instructions--

Escribe una función que devuelva la suma de todos los números de Fibonacci de valor par hasta el límite dado, inclusive.

Ejemplo de llamada a la función:
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

La suma de los números de Fibonacci pares hasta 8 debe ser igual a 10

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

La suma de los números de Fibonacci pares hasta 10 debe ser igual a 10

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

La suma de los números de Fibonacci pares hasta 34 debe ser igual a 44

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

La suma de los números de Fibonacci pares hasta 1000 debe ser igual a 798

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

La suma de los números de Fibonacci pares hasta 4000000 debe ser igual a 4613732

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
