---
language: swift
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Il y a exactement 365,25 jours dans une année civile. Cependant, cela finira par créer de la confusion car les humains comptent normalement par divisibilité exacte de 1 et non par des points décimaux. Donc, pour éviter ce problème, on a décidé d'additionner tous les 0,25 jours tous les quatre ans et de donner à cette année 366 jours (y compris le 29 février en tant que jour intercalaire) et de l'appeler une **année bissextile**. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et **ne seraient pas des années bissextiles**.

# --instructions--

Dans ce défi, nous allons le porter à un nouveau niveau, où vous devez déterminer si c'est une année bissextile ou non sans utiliser la classe `Date`, les instructions `switch`, les **blocs if**, les **blocs if-else** ou l'**opération ternaire** (`x ? a : b`) ni les opérateurs logiques **ET** (`&&`) et **OU** (`||`) à l'exception de l'opérateur **NON** (`!`).

Retournez `true` si c'est une année bissextile, `false` sinon.

Exemple d'appel de fonction :
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

L'utilisation de `Date`, `switch`, `if`, `else`, `&&`, `||` ou `?` n'est pas autorisée.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'année `2016` est une année bissextile.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

L'année `1996` est une année bissextile.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

L'année `1600` est une année bissextile.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

L'année `2020` est une année bissextile.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

L'année `2000` est une année bissextile.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

L'année `2008` est une année bissextile.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

L'année `1521` n'est pas une année bissextile.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

L'année `1800` n'est pas une année bissextile.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

L'année `2007` n'est pas une année bissextile.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

L'année `2002` n'est pas une année bissextile.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

L'année `1979` n'est pas une année bissextile.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

L'année `2006` n'est pas une année bissextile.

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
