---
language: swift
exerciseType: 1
difficulty: 1
title: Aritmetic mean
---

# --description--

Écrivez une fonction appelée `mean` pour trouver la _moyenne arithmétique_ d'un vecteur numérique.

# --instructions--

Écrivez une fonction qui retourne la moyenne d'un vecteur numérique.

Exemple d'appel de fonction :
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

La moyenne de `[1, 2, 3, 4, 5, 6, 7]` doit être égale à 4.0

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

La moyenne de `[4, 5, 6]` doit être égale à 5.0

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

La moyenne de `[12, 34, 56, 78]` doit être égale à 45.0

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
