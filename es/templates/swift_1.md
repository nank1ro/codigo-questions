---
language: swift
exerciseType: 1
difficulty: 1
title: Suma
---

# --description--

Dados dos enteros `numero1` y `numero2`, escribe un programa para sumar estos dos números

# --instructions--

Escribe una función que devuelva la suma de dos números.
> PISTA: omite las etiquetas de argumento con `_` (guion bajo)

Ejemplo de llamada a la función:
```swift
print(suma(1, 2))
// imprime 3
```

# --seed--

```swift
func suma() {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class PruebasCodigo: XCTestCase {
```

# --asserts--

La suma de 1 y 3 debe ser igual a 4

```swift
    func test1() {
        XCTAssertEqual(suma(1, 3), 4, "--err-t1--")
    }
```

La suma de 200 y 210 debe ser igual a 410

```swift
    func test2() {
        XCTAssertEqual(suma(200, 210), 410, "--err-t2--")
    }
```

La suma de 15 y 35 debe ser igual a 50

```swift
    func test3() {
        XCTAssertEqual(suma(15, 35), 50, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension PruebasCodigo {
    static var allTests : [(String, (PruebasCodigo) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
        ]
    }
}

XCTMain([testCase(PruebasCodigo.allTests)])
```

# --solutions--

```swift
func suma(_ numero1: Int, _ numero2: Int) -> Int {
    return numero1 + numero2
}
```
