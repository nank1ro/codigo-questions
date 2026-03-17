---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Chaque nouveau terme de la suite de Fibonacci est obtenu en ajoutant les deux termes précédents. En commençant par 1 et 2, les 10 premiers termes sont : 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

En considérant les termes de la suite de Fibonacci dont les valeurs ne dépassent pas le nombre donné, trouve la somme des termes de valeur paire.

# --instructions--

Écris une fonction qui retourne la somme de tous les nombres de Fibonacci pairs jusqu'à la limite donnée incluse.

Exemple d'appel de fonction :
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

La somme des nombres de Fibonacci pairs jusqu'à 8 doit être égale à 10

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

La somme des nombres de Fibonacci pairs jusqu'à 10 doit être égale à 10

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

La somme des nombres de Fibonacci pairs jusqu'à 34 doit être égale à 44

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

La somme des nombres de Fibonacci pairs jusqu'à 1000 doit être égale à 798

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

La somme des nombres de Fibonacci pairs jusqu'à 4000000 doit être égale à 4613732

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
