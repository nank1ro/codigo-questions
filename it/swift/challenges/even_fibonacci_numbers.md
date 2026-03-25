---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Ogni nuovo termine della sequenza di Fibonacci viene generato sommando i due termini precedenti. Partendo da 1 e 2, i primi 10 termini sono: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando i termini della sequenza di Fibonacci i cui valori non superano il numero dato, trova la somma dei termini di valore pari.

# --instructions--

Scrivi una funzione che restituisce la somma di tutti i numeri di Fibonacci pari fino al limite dato incluso.

Esempio di chiamata alla funzione:
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

La somma dei numeri di Fibonacci pari fino a 8 deve essere uguale a 10

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

La somma dei numeri di Fibonacci pari fino a 10 deve essere uguale a 10

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

La somma dei numeri di Fibonacci pari fino a 34 deve essere uguale a 44

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

La somma dei numeri di Fibonacci pari fino a 1000 deve essere uguale a 798

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

La somma dei numeri di Fibonacci pari fino a 4000000 deve essere uguale a 4613732

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
