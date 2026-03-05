---
language: swift
exerciseType: 1
difficulty: 3
title: ローマ数字変換器
---

# --description--

正の整数をパラメータとして受け取り、その整数のローマ数字表現を含む文字列を返す関数を作成してください。現代のローマ数字は、左端の桁から始めて各桁を個別に表現し、値がゼロの桁はスキップして記述します。

# --instructions--

例:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- すべてのローマ数字は大文字で返す必要があります。
- この表記法で表現できる最大の数は3,999です。

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

数 `2` は `II` に等しくなければなりません

```swift
    func test1() {
        XCTAssertEqual(convertToRoman(2), "II", "--err-t1--")
    }
```

数 `12` は `XII` に等しくなければなりません

```swift
    func test2() {
        XCTAssertEqual(convertToRoman(12), "XII", "--err-t2--")
    }
```

数 `16` は `XVI` に等しくなければなりません

```swift
    func test3() {
        XCTAssertEqual(convertToRoman(16), "XVI", "--err-t3--")
    }
```

数 `44` は `XLIV` に等しくなければなりません

```swift
    func test4() {
        XCTAssertEqual(convertToRoman(44), "XLIV", "--err-t4--")
    }
```

数 `68` は `LXVIII` に等しくなければなりません

```swift
    func test5() {
        XCTAssertEqual(convertToRoman(68), "LXVIII", "--err-t5--")
    }
```

数 `400` は `CD` に等しくなければなりません

```swift
    func test6() {
        XCTAssertEqual(convertToRoman(400), "CD", "--err-t6--")
    }
```

数 `798` は `DCCXCVIII` に等しくなければなりません

```swift
    func test7() {
        XCTAssertEqual(convertToRoman(798), "DCCXCVIII", "--err-t7--")
    }
```

数 `1000` は `M` に等しくなければなりません

```swift
    func test8() {
        XCTAssertEqual(convertToRoman(1000), "M", "--err-t8--")
    }
```

数 `3999` は `MMMCMXCIX` に等しくなければなりません

```swift
    func test9() {
        XCTAssertEqual(convertToRoman(3999), "MMMCMXCIX", "--err-t9--")
    }
```

数 `649` は `DCXLIX` に等しくなければなりません

```swift
    func test10() {
        XCTAssertEqual(convertToRoman(649), "DCXLIX", "--err-t10--")
    }
```

数 `1666` は `MDCLXVI` に等しくなければなりません

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
