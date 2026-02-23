---
language: swift
exerciseType: 1
difficulty: 3
title: Roman Numeral Converter
---

# --description--

Create a function taking a positive integer as its parameter and returning a string containing the Roman numeral representation of that integer. Modern Roman numerals are written by expressing each digit separately, starting with the left most digit and skipping any digit with a value of zero.

# --instructions--

Examples:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- All roman numerals should be returned as uppercase.
- The largest number that can be represented in this notation is 3,999.

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

The number `2` must equal `II` 

```swift
    func test1() {
        XCTAssertEqual(convertToRoman(2), "II", "--err-t1--")
    }
```

The number `12` must equal `XII` 

```swift
    func test2() {
        XCTAssertEqual(convertToRoman(12), "XII", "--err-t2--")
    }
```

The number `16` must equal `XVI` 

```swift
    func test3() {
        XCTAssertEqual(convertToRoman(16), "XVI", "--err-t3--")
    }
```

The number `44` must equal `XLIV` 

```swift
    func test4() {
        XCTAssertEqual(convertToRoman(44), "XLIV", "--err-t4--")
    }
```

The number `68` must equal `LXVIII` 

```swift
    func test5() {
        XCTAssertEqual(convertToRoman(68), "LXVIII", "--err-t5--")
    }
```

The number `400` must equal `CD` 

```swift
    func test6() {
        XCTAssertEqual(convertToRoman(400), "CD", "--err-t6--")
    }
```

The number `798` must equal `DCCXCVIII` 

```swift
    func test7() {
        XCTAssertEqual(convertToRoman(798), "DCCXCVIII", "--err-t7--")
    }
```

The number `1000` must equal `M` 

```swift
    func test8() {
        XCTAssertEqual(convertToRoman(1000), "M", "--err-t8--")
    }
```

The number `3999` must equal `MMMCMXCIX` 

```swift
    func test9() {
        XCTAssertEqual(convertToRoman(3999), "MMMCMXCIX", "--err-t9--")
    }
```

The number `649` must equal `DCXLIX` 

```swift
    func test10() {
        XCTAssertEqual(convertToRoman(649), "DCXLIX", "--err-t10--")
    }
```

The number `1666` must equal `MDCLXVI` 

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
