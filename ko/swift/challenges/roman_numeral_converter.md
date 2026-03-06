---
language: swift
exerciseType: 1
difficulty: 3
title: 로마 숫자 변환기
---

# --description--

양의 정수를 매개변수로 받아 해당 정수의 로마 숫자 표현을 포함하는 문자열을 반환하는 함수를 만드십시오. 현대 로마 숫자는 가장 왼쪽 자릿수부터 시작하여 각 자릿수를 별도로 표현하며, 값이 0인 자릿수는 건너뜁니다.

# --instructions--

예시:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 모든 로마 숫자는 대문자로 반환해야 합니다.
- 이 표기법으로 표현할 수 있는 가장 큰 수는 3,999입니다.

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

숫자 `2`는 `II`와 같아야 합니다

```swift
    func test1() {
        XCTAssertEqual(convertToRoman(2), "II", "--err-t1--")
    }
```

숫자 `12`는 `XII`와 같아야 합니다

```swift
    func test2() {
        XCTAssertEqual(convertToRoman(12), "XII", "--err-t2--")
    }
```

숫자 `16`은 `XVI`와 같아야 합니다

```swift
    func test3() {
        XCTAssertEqual(convertToRoman(16), "XVI", "--err-t3--")
    }
```

숫자 `44`는 `XLIV`와 같아야 합니다

```swift
    func test4() {
        XCTAssertEqual(convertToRoman(44), "XLIV", "--err-t4--")
    }
```

숫자 `68`은 `LXVIII`과 같아야 합니다

```swift
    func test5() {
        XCTAssertEqual(convertToRoman(68), "LXVIII", "--err-t5--")
    }
```

숫자 `400`은 `CD`와 같아야 합니다

```swift
    func test6() {
        XCTAssertEqual(convertToRoman(400), "CD", "--err-t6--")
    }
```

숫자 `798`은 `DCCXCVIII`과 같아야 합니다

```swift
    func test7() {
        XCTAssertEqual(convertToRoman(798), "DCCXCVIII", "--err-t7--")
    }
```

숫자 `1000`은 `M`과 같아야 합니다

```swift
    func test8() {
        XCTAssertEqual(convertToRoman(1000), "M", "--err-t8--")
    }
```

숫자 `3999`는 `MMMCMXCIX`와 같아야 합니다

```swift
    func test9() {
        XCTAssertEqual(convertToRoman(3999), "MMMCMXCIX", "--err-t9--")
    }
```

숫자 `649`는 `DCXLIX`와 같아야 합니다

```swift
    func test10() {
        XCTAssertEqual(convertToRoman(649), "DCXLIX", "--err-t10--")
    }
```

숫자 `1666`은 `MDCLXVI`와 같아야 합니다

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
