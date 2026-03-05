---
language: swift
exerciseType: 1
difficulty: 1
title: Regentropfen
---

# --description--

Ihre Aufgabe ist es, eine Zahl in einen String zu konvertieren, der Regensoundeffekte entsprechend bestimmten Faktoren enthält.
Ein Faktor ist eine Zahl, die eine andere Zahl gleichmäßig teilt, ohne einen Rest zu hinterlassen.
Der einfachste Weg, um zu testen, ob eine Zahl ein Faktor einer anderen ist, ist die Verwendung der Modulo-Operation.
Die Regeln der Regentropfen sind, dass wenn eine gegebene Zahl:

- 3 als Faktor hat, fügen Sie 'Pling' zum Ergebnis hinzu.
- 5 als Faktor hat, fügen Sie 'Plang' zum Ergebnis hinzu.
- 7 als Faktor hat, fügen Sie 'Plong' zum Ergebnis hinzu.
- keine der Zahlen 3, 5 oder 7 als Faktor hat, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zurückgibt, Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, also wäre das Ergebnis `"Plong"`.
- 30 hat sowohl 3 als auch 5 als Faktoren, aber nicht 7, also wäre das Ergebnis `"PlingPlang"`.
- 34 wird nicht von 3, 5 oder 7 geteilt, also wäre das Ergebnis `"34"`.

> HINWEIS: Lassen Sie die Argumentbezeichnung mit dem `_` (Unterstrich) weg

Beispiel für einen Funktionsaufruf:
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

Der Sound für 1 ist "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

Der Sound für 3 ist "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

Der Sound für 5 ist "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

Der Sound für 7 ist "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

Der Sound für 6 ist "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

Der Sound für 8 ist "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

Der Sound für 9 ist "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

Der Sound für 10 ist "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

Der Sound für 14 ist "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

Der Sound für 15 ist "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

Der Sound für 21 ist "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

Der Sound für 25 ist "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

Der Sound für 27 ist "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

Der Sound für 35 ist "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

Der Sound für 49 ist "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

Der Sound für 52 ist "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

Der Sound für 105 ist "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

Der Sound für 3125 ist "Plang"

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


