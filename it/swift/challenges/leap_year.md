---
language: swift
exerciseType: 1
difficulty: 3
title: Anno bisestile
---

# --description--

In un anno solare ci sono esattamente 365.25 giorni. Ma questo poteva portare confusione perché gli esseri umani normalmente contano in base all'esatta divisibilità di 1 e non con i punti decimali. Quindi, per evitare quest'ultimo problema, si decise di sommare tutti gli 0.25 giorni ogni ciclo di quattro anni e dare a quell'anno 366 giorni (includendo il 29 febbraio come giorno intercalare) e chiamarlo __anno bisestile__. Gli altri tre anni del ciclo quadriennale contengono solo 365 giorni e non sono __anni bisestili__.

# --instructions--

In questa sfida ci spingeremo ad un nuovo livello, in cui dovremo determinare se si tratta di un anno bisestile o meno senza l'uso della classe `Date`, delle dichiarazioni `switch`, dei blocchi __if__, __if-else__ o delle __operazioni ausiliarie__ (`x ? a : b`) né degli operatori logici __AND__ (`&&`) e __OR__ (`||`) con l'eccezione dell'operatore __NOT__ (`!`).

Restituisci `true` se è un anno bisestile, `false` altrimenti.

Esempio di chiamata di funzione:
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

L'uso di `Date`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'anno `2016` è bisestile.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

L'anno `1996` è bisestile.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

L'anno `1600` è bisestile.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

L'anno `2020` è bisestile.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

L'anno `2000` è bisestile.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

L'anno `2008` è bisestile.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

L'anno `1521` non è bisestile.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

L'anno `1800` non è bisestile.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

L'anno `2007` non è bisestile.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

L'anno `2002` non è bisestile.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

L'anno `1979` non è bisestile.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

L'anno `2006` non è bisestile.

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
