---
language: swift
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

W roku kalendarzowym jest dokładnie 365,25 dnia. Jednak z czasem prowadzi to do zamieszania, ponieważ ludzie normalnie liczą przez dokładną podzielność przez 1, a nie z miejscami dziesiętnymi. Aby temu zapobiec, postanowiono sumować wszystkie 0,25 dnia w każdym cyklu czteroletnim i dawać temu rokowi 366 dni (włącznie z 29 lutego jako dniem przestępnym), nazywając go __rokiem przestępnym__. Pozostałe trzy lata w cyklu czteroletnim zawierają tylko 365 dni i __nie są latami przestępnymi__.

# --instructions--

W tym wyzwaniu podnosimy poprzeczkę — masz określić, czy dany rok jest rokiem przestępnym, bez użycia klasy `Date`, instrukcji `switch`, __bloków if__, __bloków if-else__ ani __operatora trójargumentowego__ (`x ? a : b`), ani operatorów logicznych __AND__ (`&&`) i __OR__ (`||`), z wyjątkiem operatora __NOT__ (`!`).

Zwróć `true` jeśli to rok przestępny, `false` w przeciwnym razie.

Przykład wywołania funkcji:
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

Użycie `Date`, `switch`, `if`, `else`, `&&`, `||` lub `?` jest niedozwolone.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Rok `2016` jest rokiem przestępnym.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

Rok `1996` jest rokiem przestępnym.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

Rok `1600` jest rokiem przestępnym.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

Rok `2020` jest rokiem przestępnym.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

Rok `2000` jest rokiem przestępnym.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

Rok `2008` jest rokiem przestępnym.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

Rok `1521` nie jest rokiem przestępnym.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

Rok `1800` nie jest rokiem przestępnym.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

Rok `2007` nie jest rokiem przestępnym.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

Rok `2002` nie jest rokiem przestępnym.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

Rok `1979` nie jest rokiem przestępnym.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

Rok `2006` nie jest rokiem przestępnym.

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
