---
language: swift
exerciseType: 1
difficulty: 1
title: 100 puertas
---

# --description--

Hay 100 puertas en una fila que inicialmente están todas cerradas.
Haces 100 pasadas por las puertas.
La primera vez, visita cada puerta y 'alterna' la puerta (si la puerta está cerrada, ábrela; si está abierta, ciérrala).
La segunda vez, solo visita cada 2ª puerta (es decir, puerta #2, #4, #6, ...) y altérnala.
La tercera vez, visita cada 3ª puerta (es decir, puerta #3, #6, #9, ...), etc., hasta que solo visites la puerta 100.

# --instructions--

Implementa una función para determinar el estado de las puertas después del último paso.
Devuelve el resultado final en una matriz, con solo el número de puerta incluido en la matriz si está abierta.
> El método debe poder funcionar con un número variable de puertas.

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Dado 100 puertas, devuelve la lista correcta de puertas abiertas

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

Dado 10 puertas, devuelve la lista correcta de puertas abiertas

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

Dado 950 puertas, devuelve la lista correcta de puertas abiertas

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
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
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
