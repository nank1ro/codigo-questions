---
language: swift
exerciseType: 1
difficulty: 1
title: Gocce di pioggia
---

# --description--

Il tuo compito e' quello di convertiire un numero in una stringa che contiene suoni di gocce di pioggia corrispondenti a determinati fattori potenziali.
Un fattore e' un numero che si divide uniformemente in un altro numero, senza lasciare alcun resto.
Il modo piu' semplice per verificare se un numero e' un fattore di un altro e' utilizzare l'operazione modulo.
Le regole delle gocce di pioggia sono che se un dato numero:

- ha 3 come fattore, aggiungi 'Pling' al risultato.
- ha 5 come fattore, aggiungi 'Plang' al risultato.
- ha 7 come fattore, aggiungi 'Plong' al risultato.
- non ha 3, 5 o 7 come fattore, il risultato dovrebbe essere costituito dalle cifre del numero.

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

- 28 ha 7 come fattore, ma non 3 o 5, quindi il risultato e' `Plong`.
- 30 ha sia 3 che 5 come fattori, ma non 7, quindi il risultato e' `PlingPlang`.
- 34 non e' fattorizzato da 3, 5, o 7, quindi il risultato e' "34".

> SUGGERIMENTO: ometti il nome dell'argomento con l'underscore `_`

Esempio di chiamata della funzione:
```swift
print(gocceDiPioggia(28))
// stampa "Plong"
```

# --seed--

```swift
func gocceDiPioggia() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Il suono per 1 è "1"

```swift
    func test1() {
        XCTAssertEqual("1", gocceDiPioggia(1), "--err-t1--")
    }
```

Il suono per 3 è "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", gocceDiPioggia(3), "--err-t2--")
    }
```

Il suono per 5 è "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", gocceDiPioggia(5), "--err-t3--")
    }
```

Il suono per 7 è "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", gocceDiPioggia(7), "--err-t4--")
    }
```

Il suono per 6 è "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", gocceDiPioggia(6), "--err-t5--")
    }
```

Il suono per 8 è "8"

```swift
    func test8() {
        XCTAssertEqual("8", gocceDiPioggia(8), "--err-t6--")
    }
```

Il suono per 9 è "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", gocceDiPioggia(9), "--err-t7--")
    }
```

Il suono per 10 è "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", gocceDiPioggia(10), "--err-t8--")
    }
```

Il suono per 14 è "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", gocceDiPioggia(14), "--err-t9--")
    }
```

Il suono per 15 è "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", gocceDiPioggia(15), "--err-t10--")
    }
```

Il suono per 21 è "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", gocceDiPioggia(21), "--err-t11--")
    }
```

Il suono per 25 è "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", gocceDiPioggia(25), "--err-t12--")
    }
```

Il suono per 27 è "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", gocceDiPioggia(27), "--err-t13--")
    }
```

Il suono per 35 è "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", gocceDiPioggia(35), "--err-t14--")
    }
```

Il suono per 49 è "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", gocceDiPioggia(49), "--err-t15--")
    }
```

Il suono per 52 è "52"

```swift
    func test52() {
        XCTAssertEqual("52", gocceDiPioggia(52), "--err-t16--")
    }
```

Il suono per 105 è "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", gocceDiPioggia(105), "--err-t17--")
    }
```

Il suono per 3125 è "Plang"

```swift
    func test3125() {
        XCTAssertEqual("Plang", gocceDiPioggia(3125), "--err-t18--")
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
func gocceDiPioggia(_ num: Int) -> String {
    var risultato = ""
    if (num % 3 == 0) {
        risultato += "Pling"
    } 
    if (num % 5 == 0) {
        risultato += "Plang"
    }
    if (num % 7 == 0) {
        risultato += "Plong"
    }
    if (risultato.isEmpty) {
        risultato = String(num)
    }

    return risultato
}
```



