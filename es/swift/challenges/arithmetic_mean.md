---
language: swift
exerciseType: 1
difficulty: 1
title: Aritmetic mean
---

# --description--

Escribe un funcion llamo `mean` un encontrar el _arithmetic average_ de un numeric vector.

# --instructions--

Escribe un funcion ese devuelve el significar de un numeric vector.

ejemplo de funcion llamar:
```swift
print(mean([1, 2, 3]))
// prints 2.0
```

# --seed--

```swift
func mean() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

The mean of `[1, 2, 3, 4, 5, 6, 7]` must be equal to 4.0

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

The mean of `[4, 5, 6]` must be equal to 5.0

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

The mean of `[12, 34, 56, 78]` must be equal to 45.0

```swift
    func test3() {
        XCTAssertEqual(mean([12, 34, 56, 78]), 45.0, "--err-t3--")
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
func mean(_ numeros: [Double]) -> Double {
  return numeros.reduce(0, +) / Double(numeros.conteo)
}
```
