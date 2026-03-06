---
language: swift
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与某些潜在因数对应的雨滴声的字符串。
因数是能够整除另一个数字且没有余数的数字。
测试一个数字是否是另一个数字的因数的最简单方法是使用取模运算。
雨滴的规则是，如果给定的数字：

- 有因数 3，则在结果中添加 'Pling'。
- 有因数 5，则在结果中添加 'Plang'。
- 有因数 7，则在结果中添加 'Plong'。
- 没有 3、5 或 7 作为因数，结果应该是该数字本身。

# --instructions--

编写一个返回正确字符串的函数，示例：

- 28 有因数 7，但没有 3 或 5，所以结果是 `"Plong"`。
- 30 同时有因数 3 和 5，但没有 7，所以结果是 `"PlingPlang"`。
- 34 不能被 3、5 或 7 整除，所以结果是 `"34"`。

> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
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

1 的声音是 "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

3 的声音是 "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

5 的声音是 "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

7 的声音是 "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

6 的声音是 "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

8 的声音是 "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

9 的声音是 "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

10 的声音是 "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

14 的声音是 "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

15 的声音是 "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

21 的声音是 "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

25 的声音是 "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

27 的声音是 "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

35 的声音是 "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

49 的声音是 "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

52 的声音是 "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

105 的声音是 "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

3125 的声音是 "Plang"

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


