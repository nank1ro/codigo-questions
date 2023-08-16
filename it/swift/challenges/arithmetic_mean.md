---
language: swift
exerciseType: 1
difficulty: 1
title: Media aritmetica
---

# --description--

Scrivi una funzione chiamata `mean` per trovare la _media aritmetica_ di un vettore numerico.

# --instructions--

Scrivi una funzione che restituisca la media di un vettore numerico.

Esempio di chiamata di funzione:
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

La media di `[1, 2, 3, 4, 5, 6, 7]` deve essere uguale a 4.0

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

La media di `[4, 5, 6]` deve essere uguale a 5.0

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

La media di `[12, 34, 56, 78]` deve essere uguale a 45.0

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
