---
language: swift
exerciseType: 1
difficulty: 1
title: 雨粒
---

# --description--

あなたのタスクは、数値を特定の因数に対応する雨音を含む文字列に変換することです。
因数とは、別の数を余りなく割り切れる数のことです。
ある数が別の数の因数であるかどうかをテストする最も簡単な方法は、剰余演算を使用することです。
雨粒のルールは、与えられた数が:

- 3を因数に持つ場合、結果に 'Pling' を追加します。
- 5を因数に持つ場合、結果に 'Plang' を追加します。
- 7を因数に持つ場合、結果に 'Plong' を追加します。
- 3、5、7のいずれも因数に持たない場合、結果はその数の数字になります。

# --instructions--

正しい文字列を返す関数を書いてください。例:

- 28は7を因数に持ちますが、3や5は持たないので、結果は `"Plong"` になります。
- 30は3と5の両方を因数に持ちますが、7は持たないので、結果は `"PlingPlang"` になります。
- 34は3、5、7のいずれの因数も持たないので、結果は `"34"` になります。

> ヒント: `_`（アンダースコア）で引数ラベルを省略してください

関数呼び出しの例:
```swift
print(raindrops(28))
// prints "Plong"
```

# --seed--

```swift
func raindrops() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

1の音は "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

3の音は "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

5の音は "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

7の音は "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

6の音は "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

8の音は "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

9の音は "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

10の音は "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

14の音は "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

15の音は "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

21の音は "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

25の音は "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

27の音は "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

35の音は "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

49の音は "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

52の音は "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

105の音は "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

3125の音は "Plang"

```swift
    func test3125() {
        XCTAssertEqual("Plang", raindrops(3125), "--err-t18--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test3", test3),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test14", test14),
            ("test15", test15),
            ("test21", test21),
            ("test25", test25),
            ("test27", test27),
            ("test35", test35),
            ("test49", test49),
            ("test52", test52),
            ("test105", test105),
            ("test3125", test3125),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


