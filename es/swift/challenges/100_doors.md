---
language: swift
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

There son 100 doors en un row ese son todos initially closed.
You hacer 100 pasa por el doors.
el primero time through, visit cada door y 'toggle' el door (si el door es closed, abrir it; si lo es abrir, close it).
el segundo time, solo visit cada 2nd door (i.e., door #2, #4, #6, ...) y toggle it.
el tercero time, visit cada 3rd door (i.e., door #3, #6, #9, ...), etc., hasta you solo visit el 100th door.

# --instructions--

Implementa un funcion un determine el state de el doors despues el ultimo pasar.
Devuelve el final resultado en un arreglo, con solo el door numero included en el arreglo si lo es abrir.
> The metodo debe ser capaz un trabajar con un variable numero de doors.

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

Given 100 doors, return the correct list of open doors

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

Given 10 doors, return the correct list of open doors

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

Given 950 doors, return the correct list of open doors

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
