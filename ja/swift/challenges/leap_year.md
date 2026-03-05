---
language: swift
exerciseType: 1
difficulty: 3
title: うるう年
---

# --description--

暦年にはちょうど365.25日あります。しかし、最終的にこれは混乱を招きます。なぜなら、人間は通常、小数点ではなく1の正確な割り切りで数えるからです。そこで、後者を避けるために、4年周期ごとに0.25日をすべて足し合わせ、その年を366日（閏日として2月29日を含む）にして__うるう年__と呼ぶことが決められました。4年周期の他の3年は365日のみで、__うるう年ではありません__。

# --instructions--

このチャレンジでは、`Date` クラス、`switch` 文、__ifブロック__、__if-elseブロック__、__三項演算子__（`x ? a : b`）、論理演算子 __AND__（`&&`）および __OR__（`||`）を使用せずに、うるう年かどうかを判定します。ただし __NOT__（`!`）演算子は例外として使用できます。

うるう年の場合は `true` を、そうでない場合は `false` を返してください。

関数呼び出しの例:
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

`Date`、`switch`、`if`、`else`、`&&`、`||`、`?` の使用は許可されていません。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年 `2016` はうるう年です。

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

年 `1996` はうるう年です。

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

年 `1600` はうるう年です。

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

年 `2020` はうるう年です。

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

年 `2000` はうるう年です。

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

年 `2008` はうるう年です。

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

年 `1521` はうるう年ではありません。

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

年 `1800` はうるう年ではありません。

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

年 `2007` はうるう年ではありません。

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

年 `2002` はうるう年ではありません。

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

年 `1979` はうるう年ではありません。

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

年 `2006` はうるう年ではありません。

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
