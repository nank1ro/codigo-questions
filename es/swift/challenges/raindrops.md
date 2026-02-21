---
language: swift
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Your task es un convert un numero en un cadena ese contiene raindrop sounds corresponding un certain potential factors.
A factor es un numero ese evenly divides en another numero, dejando no resto.
The simplest way un test si un numero es un factor de another es un usar el modulo operacion.
The rules de raindrops son ese si un dado numero:

- tiene 3 como un factor, Anade 'Pling' un el resultado.
- tiene 5 como un factor, Anade 'Plang' un el resultado.
- tiene 7 como un factor, Anade 'Plong' un el resultado.
- hace no tiene cualquier de 3, 5, o 7 como un factor, el resultado deberia ser el digits de el numero.

# --instructions--

Escribe un funcion ese devuelve el correct cadena, ejemplos:

- 28 tiene 7 como un factor, pero no 3 o 5, asi que el resultado habria ser `"Plong"`.
- 30 tiene both 3 y 5 como factors, pero no 7, asi que el resultado habria ser `"PlingPlang"`.
- 34 es no factored por 3, 5, o 7, asi que el resultado habria ser `"34"`.

> HINT: omit el argumento label con el `_` (underscore)

ejemplo de funcion llamar:
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

The sound for 1 is "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

The sound for 3 is "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

The sound for 5 is "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

The sound for 7 is "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

The sound for 6 is "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

The sound for 8 is "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

The sound for 9 is "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

The sound for 10 is "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

The sound for 14 is "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

The sound for 15 is "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

The sound for 21 is "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

The sound for 25 is "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

The sound for 27 is "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

The sound for 35 is "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

The sound for 49 is "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

The sound for 52 is "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

The sound for 105 is "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

The sound for 3125 is "Plang"

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
    var resultado = "";
    if (num % 3 == 0) {
        resultado += "Pling"
    } 
    if (num % 5 == 0) {
        resultado += "Plang"
    }
    if (num % 7 == 0) {
        resultado += "Plong"
    }
    if (resultado.isEmpty) {
        resultado = String(num);         
    }

    return resultado
}
```


