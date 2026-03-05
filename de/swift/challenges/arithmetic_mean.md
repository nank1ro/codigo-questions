---
language: swift
exerciseType: 1
difficulty: 1
title: Arithmetischer Durchschnitt
---

# --description--

Schreiben Sie eine Funktion namens `mean`, um den _arithmetischen Durchschnitt_ eines numerischen Vektors zu finden.

# --instructions--

Schreiben Sie eine Funktion, die den Durchschnitt eines numerischen Vektors zurückgibt.

Beispiel für einen Funktionsaufruf:
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

Der Durchschnitt von `[1, 2, 3, 4, 5, 6, 7]` muss gleich 4,0 sein

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

Der Durchschnitt von `[4, 5, 6]` muss gleich 5,0 sein

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

Der Durchschnitt von `[12, 34, 56, 78]` muss gleich 45,0 sein

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
