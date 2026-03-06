---
language: swift
exerciseType: 1
difficulty: 3
title: 罗马数字转换器
---

# --description--

创建一个函数，接受一个正整数作为参数，并返回一个包含该整数罗马数字表示的字符串。现代罗马数字的书写方式是从最左边的数字开始，分别表示每个数字，跳过值为零的数字。

# --instructions--

示例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 所有罗马数字应以大写形式返回。
- 此表示法能表示的最大数字是 3,999。

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

数字 `2` 必须等于 `II`

```swift
    func test1() {
        XCTAssertEqual(convertToRoman(2), "II", "--err-t1--")
    }
```

数字 `12` 必须等于 `XII`

```swift
    func test2() {
        XCTAssertEqual(convertToRoman(12), "XII", "--err-t2--")
    }
```

数字 `16` 必须等于 `XVI`

```swift
    func test3() {
        XCTAssertEqual(convertToRoman(16), "XVI", "--err-t3--")
    }
```

数字 `44` 必须等于 `XLIV`

```swift
    func test4() {
        XCTAssertEqual(convertToRoman(44), "XLIV", "--err-t4--")
    }
```

数字 `68` 必须等于 `LXVIII`

```swift
    func test5() {
        XCTAssertEqual(convertToRoman(68), "LXVIII", "--err-t5--")
    }
```

数字 `400` 必须等于 `CD`

```swift
    func test6() {
        XCTAssertEqual(convertToRoman(400), "CD", "--err-t6--")
    }
```

数字 `798` 必须等于 `DCCXCVIII`

```swift
    func test7() {
        XCTAssertEqual(convertToRoman(798), "DCCXCVIII", "--err-t7--")
    }
```

数字 `1000` 必须等于 `M`

```swift
    func test8() {
        XCTAssertEqual(convertToRoman(1000), "M", "--err-t8--")
    }
```

数字 `3999` 必须等于 `MMMCMXCIX`

```swift
    func test9() {
        XCTAssertEqual(convertToRoman(3999), "MMMCMXCIX", "--err-t9--")
    }
```

数字 `649` 必须等于 `DCXLIX`

```swift
    func test10() {
        XCTAssertEqual(convertToRoman(649), "DCXLIX", "--err-t10--")
    }
```

数字 `1666` 必须等于 `MDCLXVI`

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
