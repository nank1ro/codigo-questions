---
language: swift
exerciseType: 1
difficulty: 1
title: "Média aritmética"
---

# --description--

Escreva uma função chamada `mean` para encontrar a _média aritmética_ de um vetor numérico.

# --instructions--

Escreva uma função que retorne a média de um vetor numérico.

Exemplo de chamada da função:
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

A média de `[1, 2, 3, 4, 5, 6, 7]` deve ser igual a 4.0

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

A média de `[4, 5, 6]` deve ser igual a 5.0

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

A média de `[12, 34, 56, 78]` deve ser igual a 45.0

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
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
