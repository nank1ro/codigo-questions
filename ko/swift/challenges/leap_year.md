---
language: swift
exerciseType: 1
difficulty: 3
title: 윤년
---

# --description--

달력의 1년은 정확히 365.25일입니다. 하지만 결국 이것은 혼란을 초래할 수 있는데, 인간은 보통 소수점이 아닌 1의 정확한 나눗셈으로 계산하기 때문입니다. 따라서 이를 피하기 위해 4년 주기마다 0.25일을 모두 합산하여 그 해를 366일로 만들고 (2월 29일을 윤일로 포함) 이를 __윤년__이라고 부르기로 했습니다. 4년 주기의 나머지 3년은 365일만 포함하며 __윤년이 아닙니다__.

# --instructions--

이 도전에서는 한 단계 더 나아가, `Date` 클래스, `switch` 문, __if 블록__, __if-else 블록__ 또는 __삼항 연산__ (`x ? a : b`)을 사용하지 않고, 또한 논리 연산자 __AND__ (`&&`)와 __OR__ (`||`)도 사용하지 않고 (단, __NOT__ (`!`) 연산자는 예외) 윤년인지 아닌지를 판별해야 합니다.

윤년이면 `true`를, 그렇지 않으면 `false`를 반환하십시오.

함수 호출 예시:
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

`Date`, `switch`, `if`, `else`, `&&`, `||` 또는 `?`의 사용은 허용되지 않습니다.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`년은 윤년입니다.

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

`1996`년은 윤년입니다.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

`1600`년은 윤년입니다.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

`2020`년은 윤년입니다.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

`2000`년은 윤년입니다.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

`2008`년은 윤년입니다.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

`1521`년은 윤년이 아닙니다.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

`1800`년은 윤년이 아닙니다.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

`2007`년은 윤년이 아닙니다.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

`2002`년은 윤년이 아닙니다.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

`1979`년은 윤년이 아닙니다.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

`2006`년은 윤년이 아닙니다.

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
