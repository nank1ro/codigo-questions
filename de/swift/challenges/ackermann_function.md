---
language: swift
exerciseType: 1
difficulty: 1
title: Ackermann-Funktion
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel einer rekursiven Funktion, besonders bemerkenswert, weil sie keine primitive rekursive Funktion ist. Ihr Wert und die Größe ihres Aufrufbaums wachsen sehr schnell.

Die Ackermann-Funktion wird normalerweise wie folgt definiert:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ihre Argumente sind niemals negativ und sie beendet sich immer

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zurückgibt.

# --seed--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`ack(0, 0)` sollte 1 zurückgeben.

```swift
    func test1() {
        XCTAssertEqual(ack(0, 0), 1, "--err-t1--")
    }
```

`ack(1, 1)` sollte 3 zurückgeben.

```swift
    func test2() {
        XCTAssertEqual(ack(1, 1), 3, "--err-t2--")
    }
```

`ack(2, 5)` sollte 13 zurückgeben.

```swift
    func test3() {
        XCTAssertEqual(ack(2, 5), 13, "--err-t3--")
    }
```

`ack(3, 3)` sollte 61 zurückgeben.

```swift
    func test4() {
        XCTAssertEqual(ack(3, 3), 61, "--err-t4--")
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
            ("test4", test4),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
