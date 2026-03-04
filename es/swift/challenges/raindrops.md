---
language: swift
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Tu tarea es convertir un número en una cadena que contenga sonidos de gotas de lluvia correspondientes a ciertos factores potenciales.
Un factor es un número que divide uniformemente a otro número, sin dejar residuo.
La forma más simple de probar si un número es un factor de otro es usar la operación de módulo.
Las reglas de raindrops son que si un número dado:

- tiene 3 como factor, agrega 'Pling' al resultado.
- tiene 5 como factor, agrega 'Plang' al resultado.
- tiene 7 como factor, agrega 'Plong' al resultado.
- no tiene 3, 5 o 7 como factor, el resultado debe ser los dígitos del número.

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

- 28 tiene 7 como factor, pero no 3 o 5, por lo que el resultado sería `"Plong"`.
- 30 tiene tanto 3 como 5 como factores, pero no 7, por lo que el resultado sería `"PlingPlang"`.
- 34 no es factorizado por 3, 5 o 7, por lo que el resultado sería `"34"`.

> PISTA: omite la etiqueta de argumento con el `_` (guion bajo)

Ejemplo de llamada de función:
```swift
print(raindrops(28))
// prints "Plong"
```

# --seed--

```swift
func raindrops() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

El sonido para 1 es "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

El sonido para 3 es "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

El sonido para 5 es "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

El sonido para 7 es "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

El sonido para 6 es "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

El sonido para 8 es "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

El sonido para 9 es "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

El sonido para 10 es "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

El sonido para 14 es "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

El sonido para 15 es "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

El sonido para 21 es "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

El sonido para 25 es "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

El sonido para 27 es "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

El sonido para 35 es "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

El sonido para 49 es "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

El sonido para 52 es "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

El sonido para 105 es "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

El sonido para 3125 es "Plang"

```swift
    func test3125() {
        XCTAssertEqual("Plang", raindrops(3125), "--err-t18--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test3", test3),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test14", test14),
            ("test15", test15),
            ("test21", test21),
            ("test25", test25),
            ("test27", test27),
            ("test35", test35),
            ("test49", test49),
            ("test52", test52),
            ("test105", test105),
            ("test3125", test3125),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


