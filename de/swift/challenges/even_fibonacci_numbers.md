---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Jedes neue Glied der Fibonacci-Folge entsteht durch Addition der beiden vorhergehenden Glieder. Ausgehend von 1 und 2 lauten die ersten 10 Glieder: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Betrachte die Glieder der Fibonacci-Folge, deren Werte den gegebenen Grenzwert nicht überschreiten, und finde die Summe der geradzahligen Glieder.

# --instructions--

Schreibe eine Funktion, die die Summe aller geradzahligen Fibonacci-Zahlen bis einschließlich des gegebenen Grenzwerts zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Die Summe der geraden Fibonacci-Zahlen bis 8 muss 10 ergeben

```swift
    func testFibonacci1() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t1--")
    }
```

Die Summe der geraden Fibonacci-Zahlen bis 10 muss 10 ergeben

```swift
    func testFibonacci2() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t2--")
    }
```

Die Summe der geraden Fibonacci-Zahlen bis 34 muss 44 ergeben

```swift
    func testFibonacci3() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t3--")
    }
```

Die Summe der geraden Fibonacci-Zahlen bis 1000 muss 798 ergeben

```swift
    func testFibonacci4() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t4--")
    }
```

Die Summe der geraden Fibonacci-Zahlen bis 4000000 muss 4613732 ergeben

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
