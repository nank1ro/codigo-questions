---
language: swift
exerciseType: 1
difficulty: 3
title: Año bisiesto
---

# --description--

En un año calendario hay exactamente 365.25 días. Sin embargo, eventualmente esto llevará a confusión porque los humanos normalmente cuentan por divisibilidad exacta de 1 y no con puntos decimales. Entonces, para evitar lo último, se decidió sumar los 0.25 días cada ciclo de cuatro años y darle a ese año 366 días (incluyendo el 29 de febrero como día intercalar) y llamarlo __año bisiesto__. Los otros tres años del ciclo de cuatro años solo tendrían 365 días y __no serían años bisiestos__.

# --instructions--

En este desafío lo llevaremos a un nuevo nivel, donde debes determinar si es un año bisiesto o no sin el uso de la clase `Date`, declaraciones `switch`, __bloques if__, __bloques if-else__ u __operación ternaria__ (`x ? a : b`) ni los operadores lógicos __AND__ (`&&`) y __OR__ (`||`) con la excepción del operador __NOT__ (`!`).

Devuelve `true` si es un año bisiesto, `false` en caso contrario.

Ejemplo de llamada de función:
```swift
print(leapYear(2000))
// prints true
```

# --seed--

```swift
func leapYear(_ year: Int) -> Bool {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

No se permite el uso de `Date`, `switch`, `if`, `else`, `&&`, `||` o `?`.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

El año `2016` es un año bisiesto.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

El año `1996` es un año bisiesto.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

El año `1600` es un año bisiesto.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

El año `2020` es un año bisiesto.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

El año `2000` es un año bisiesto.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

El año `2008` es un año bisiesto.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

El año `1521` no es un año bisiesto.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

El año `1800` no es un año bisiesto.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

El año `2007` no es un año bisiesto.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

El año `2002` no es un año bisiesto.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

El año `1979` no es un año bisiesto.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

El año `2006` no es un año bisiesto.

```swift
    func test12() {
        XCTAssertEqual(leapYear(2006), false, "--err-t12--")
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
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test11", test11),
            ("test12", test12), 
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
