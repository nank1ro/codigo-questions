---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Si listamos todos los números naturales menores de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

# --instructions--

Escribe una función que encuentre la suma de todos los múltiplos de 3 o 5 menores que el número dado.

Ejemplo de llamada a la función:
```swift
print(multiplesOf3And5(10))
// prints 23
```

# --seed--

```swift
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

La suma de los múltiplos de 3 o 5 menores de 10 debe ser igual a 23

```swift
    func testMultiples1() {
        XCTAssertEqual(multiplesOf3And5(10), 23, "--err-t1--")
    }
```

La suma de los múltiplos de 3 o 5 menores de 1000 debe ser igual a 233168

```swift
    func testMultiples2() {
        XCTAssertEqual(multiplesOf3And5(1000), 233168, "--err-t2--")
    }
```

La suma de los múltiplos de 3 o 5 menores de 6987 debe ser igual a 11390208

```swift
    func testMultiples3() {
        XCTAssertEqual(multiplesOf3And5(6987), 11390208, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testMultiples1", testMultiples1),
            ("testMultiples2", testMultiples2),
            ("testMultiples3", testMultiples3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
