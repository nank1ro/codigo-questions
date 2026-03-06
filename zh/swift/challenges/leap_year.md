---
language: swift
exerciseType: 1
difficulty: 3
title: 闰年
---

# --description--

一个日历年恰好有365.25天。但是，这最终会导致混淆，因为人类通常按整除1来计数，而不是用小数点。因此，为了避免后者，人们决定将每四年周期中的所有0.25天累加起来，给那一年366天（包括2月29日作为闰日），并称之为__闰年__。四年周期中的其他三年只有365天，__不是闰年__。

# --instructions--

在这个挑战中，我们将提升难度，你需要在不使用 `Date` 类、`switch` 语句、__if 代码块__、__if-else 代码块__或__三元运算符__（`x ? a : b`）以及逻辑运算符 __AND__（`&&`）和 __OR__（`||`）的情况下判断是否为闰年，但可以使用 __NOT__（`!`）运算符。

如果是闰年返回 `true`，否则返回 `false`。

函数调用示例：
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

不允许使用 `Date`、`switch`、`if`、`else`、`&&`、`||` 或 `?`。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年份 `2016` 是闰年。

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

年份 `1996` 是闰年。

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

年份 `1600` 是闰年。

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

年份 `2020` 是闰年。

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

年份 `2000` 是闰年。

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

年份 `2008` 是闰年。

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

年份 `1521` 不是闰年。

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

年份 `1800` 不是闰年。

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

年份 `2007` 不是闰年。

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

年份 `2002` 不是闰年。

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

年份 `1979` 不是闰年。

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

年份 `2006` 不是闰年。

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
