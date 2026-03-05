---
language: swift
exerciseType: 1
difficulty: 3
title: Schaltjahr
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Dies führt jedoch schließlich zu Verwirrung, da Menschen normalerweise durch genaue Teilbarkeit durch 1 zählen und nicht mit Dezimalzahlen. Um das zu vermeiden, wurde beschlossen, alle 0,25 Tage in jedem Vier-Jahres-Zyklus zu addieren und diesem Jahr 366 Tage (einschließlich 29. Februar als Schalttag) zu geben und es ein __Schaltjahr__ zu nennen. Die anderen drei Jahre im Vier-Jahres-Zyklus würden nur 365 Tage haben und __wären keine Schaltjahre__.

# --instructions--

In dieser Herausforderung werden wir es auf ein neues Niveau heben, wo Sie bestimmen müssen, ob es ein Schaltjahr ist oder nicht, ohne die `Date`-Klasse, `switch`-Anweisungen, __if-Blöcke__, __if-else-Blöcke__ oder __ternäre Operatoren__ (`x ? a : b`) zu verwenden, noch die logischen Operatoren __AND__ (`&&`) und __OR__ (`||`), mit Ausnahme des __NOT__-Operators (`!`).

Geben Sie `true` zurück, wenn es ein Schaltjahr ist, `false` ansonsten.

Beispiel für einen Funktionsaufruf:
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

Die Verwendung von `Date`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht erlaubt.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

Das Jahr `1996` ist ein Schaltjahr.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

Das Jahr `1600` ist ein Schaltjahr.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

Das Jahr `2020` ist ein Schaltjahr.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

Das Jahr `2000` ist ein Schaltjahr.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

Das Jahr `2008` ist ein Schaltjahr.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

Das Jahr `1521` ist kein Schaltjahr.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

Das Jahr `1800` ist kein Schaltjahr.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

Das Jahr `2007` ist kein Schaltjahr.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

Das Jahr `2002` ist kein Schaltjahr.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

Das Jahr `1979` ist kein Schaltjahr.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

Das Jahr `2006` ist kein Schaltjahr.

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
