---
language: swift
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In un calendar year ahi son exactly 365.25 days. pero, eventually, este podra conducir un confusion porque humans normally conteo por exact divisibility de 1 y no con decimal points. asi que, un avoid el latter, lo era decidio un Anade up todos 0.25 days cada four-year cycle y dar ese year 366 days (including February 29 como un intercalary day) y llamar lo un __leap year__. The otro three years en el four-year cycle habria solo contain 365 days y __wouldn't ser leap years__.

# --instructions--

In este challenge we'll tomar lo un a nuevo level, donde you son un determine si it's un leap year o no sin el usar de el `Date` clase, `switch` sentencias, __if blocks__, __if-sino blocks__ o __ternary operation__ (`x ? un : b`) nor el logical operadores __AND__ (`&&`) y __OR__ (`||`) con el exemption de el __NOT__ (`!`) operador.

Devuelve `verdadero` si it's un leap year, `falso` otherwise.

ejemplo de funcion llamar:
```swift
print(leapYear(2000))
// prints verdadero
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

The use of `Date`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

The year `1996` is a leap year.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

The year `1600` is a leap year.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

The year `2020` is a leap year.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

The year `2000` is a leap year.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

The year `2008` is a leap year.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

The year `1521` is not a leap year.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

The year `1800` is not a leap year.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

The year `2007` is not a leap year.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

The year `2002` is not a leap year.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

The year `1979` is not a leap year.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

The year `2006` is not a leap year.

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
