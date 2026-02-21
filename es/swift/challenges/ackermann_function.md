---
language: swift
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

The Ackermann funcion es un classic ejemplo de un recursive funcion, notable especially porque lo es no un primitive recursive funcion. It crece muy quickly en valor, como hace el tamano de su llamar tree.

The Ackermann funcion es generalmente defined como sigue:

<latex>A(m, n) = \comenzar{cases} n + 1 &\texto{si } m = 0 \\ A(m - 1,1) &\texto{si } m > 0 \texto{ y } n = 0 \\ A(m -1, A(m, n - 1)) &\texto{si } m > 0 \texto{ y } n > 0 \terminar{cases}</latex>

Its argumentos son nunca negative y lo siempre terminates

# --instructions--

Escribe un funcion cual devuelve el valor de el Ackermann funcion.

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

`ack(0, 0)` should return 1.

```swift
    func test1() {
        XCTAssertEqual(ack(0, 0), 1, "--err-t1--")
    }
```

`ack(1, 1)` should return 3.

```swift
    func test2() {
        XCTAssertEqual(ack(1, 1), 3, "--err-t2--")
    }
```

`ack(2, 5)` should return 13.

```swift
    func test3() {
        XCTAssertEqual(ack(2, 5), 13, "--err-t3--")
    }
```

`ack(3, 3)` should return 61.

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
