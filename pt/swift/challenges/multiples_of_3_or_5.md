---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.

# --instructions--

Encontre a soma de todos os múltiplos de 3 ou 5 abaixo do valor do parâmetro fornecido `number`.

# --seed--

```swift
func multiplesOf3and5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`multiplesOf3and5(10)` deve retornar 23.

```swift
    func test1() {
        XCTAssertEqual(multiplesOf3and5(10), 23, "--err-t1--")
    }
```

`multiplesOf3and5(1000)` deve retornar 233168.

```swift
    func test2() {
        XCTAssertEqual(multiplesOf3and5(1000), 233168, "--err-t2--")
    }
```

`multiplesOf3and5(6987)` deve retornar 11390208.

```swift
    func test3() {
        XCTAssertEqual(multiplesOf3and5(6987), 11390208, "--err-t3--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func multiplesOf3and5(_ number: Int) -> Int {
    var total = 0
    for i in 0..<number {
        if i % 3 == 0 || i % 5 == 0 {
            total += i
        }
    }
    return total
}
```
