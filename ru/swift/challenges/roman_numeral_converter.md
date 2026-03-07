---
language: swift
exerciseType: 1
difficulty: 3
title: Конвертер римских чисел
---

# --description--

Создайте функцию, принимающую положительное целое число в качестве параметра и возвращающую строку с представлением этого числа в римских цифрах. Современные римские цифры записываются путём выражения каждой цифры отдельно, начиная с крайней левой цифры и пропуская цифры со значением ноль.

# --instructions--

Примеры:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- Все римские цифры должны возвращаться в верхнем регистре.
- Наибольшее число, которое может быть представлено в этой нотации — 3 999.

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

Число `2` должно равняться `II`

```swift
    func test1() {
        XCTAssertEqual(convertToRoman(2), "II", "--err-t1--")
    }
```

Число `12` должно равняться `XII`

```swift
    func test2() {
        XCTAssertEqual(convertToRoman(12), "XII", "--err-t2--")
    }
```

Число `16` должно равняться `XVI`

```swift
    func test3() {
        XCTAssertEqual(convertToRoman(16), "XVI", "--err-t3--")
    }
```

Число `44` должно равняться `XLIV`

```swift
    func test4() {
        XCTAssertEqual(convertToRoman(44), "XLIV", "--err-t4--")
    }
```

Число `68` должно равняться `LXVIII`

```swift
    func test5() {
        XCTAssertEqual(convertToRoman(68), "LXVIII", "--err-t5--")
    }
```

Число `400` должно равняться `CD`

```swift
    func test6() {
        XCTAssertEqual(convertToRoman(400), "CD", "--err-t6--")
    }
```

Число `798` должно равняться `DCCXCVIII`

```swift
    func test7() {
        XCTAssertEqual(convertToRoman(798), "DCCXCVIII", "--err-t7--")
    }
```

Число `1000` должно равняться `M`

```swift
    func test8() {
        XCTAssertEqual(convertToRoman(1000), "M", "--err-t8--")
    }
```

Число `3999` должно равняться `MMMCMXCIX`

```swift
    func test9() {
        XCTAssertEqual(convertToRoman(3999), "MMMCMXCIX", "--err-t9--")
    }
```

Число `649` должно равняться `DCXLIX`

```swift
    func test10() {
        XCTAssertEqual(convertToRoman(649), "DCXLIX", "--err-t10--")
    }
```

Число `1666` должно равняться `MDCLXVI`

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
