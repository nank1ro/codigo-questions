---
language: swift
exerciseType: 1
difficulty: 3
title: Römische Zahlenumrechner
---

# --description--

Erstellen Sie eine Funktion, die eine positive ganze Zahl als Parameter verwendet und einen String mit der römischen Zahlendarstellung dieser ganzen Zahl zurückgibt. Moderne römische Zahlen werden geschrieben, indem jede Ziffer separat ausgedrückt wird, beginnend mit der am weitesten links stehenden Ziffer und wobei jede Ziffer mit dem Wert Null übersprungen wird.

# --instructions--

Beispiele:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Alle römischen Zahlen sollten in Großbuchstaben zurückgegeben werden.
- Die größte Zahl, die in dieser Notation dargestellt werden kann, ist 3.999.

# --seed--

```swift
func convertToRoman(_ n: Int) -> String {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Die Zahl `2` muss gleich `II` sein

```swift
    func test1() {
        XCTAssertEqual(convertToRoman(2), "II", "--err-t1--")
    }
```

Die Zahl `12` muss gleich `XII` sein

```swift
    func test2() {
        XCTAssertEqual(convertToRoman(12), "XII", "--err-t2--")
    }
```

Die Zahl `16` muss gleich `XVI` sein

```swift
    func test3() {
        XCTAssertEqual(convertToRoman(16), "XVI", "--err-t3--")
    }
```

Die Zahl `44` muss gleich `XLIV` sein

```swift
    func test4() {
        XCTAssertEqual(convertToRoman(44), "XLIV", "--err-t4--")
    }
```

Die Zahl `68` muss gleich `LXVIII` sein

```swift
    func test5() {
        XCTAssertEqual(convertToRoman(68), "LXVIII", "--err-t5--")
    }
```

Die Zahl `400` muss gleich `CD` sein

```swift
    func test6() {
        XCTAssertEqual(convertToRoman(400), "CD", "--err-t6--")
    }
```

Die Zahl `798` muss gleich `DCCXCVIII` sein

```swift
    func test7() {
        XCTAssertEqual(convertToRoman(798), "DCCXCVIII", "--err-t7--")
    }
```

Die Zahl `1000` muss gleich `M` sein

```swift
    func test8() {
        XCTAssertEqual(convertToRoman(1000), "M", "--err-t8--")
    }
```

Die Zahl `3999` muss gleich `MMMCMXCIX` sein

```swift
    func test9() {
        XCTAssertEqual(convertToRoman(3999), "MMMCMXCIX", "--err-t9--")
    }
```

Die Zahl `649` muss gleich `DCXLIX` sein

```swift
    func test10() {
        XCTAssertEqual(convertToRoman(649), "DCXLIX", "--err-t10--")
    }
```

Die Zahl `1666` muss gleich `MDCLXVI` sein

```swift
    func test11() {
        XCTAssertEqual(convertToRoman(1666), "MDCLXVI", "--err-t11--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func convertToRoman(_ n: Int) -> String {
  var result = ""
  var number = n
  for (value, letter) in [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
  ] {
    while number >= value {
      result += letter
      number -= value
    }
  }
  return result
}
```
