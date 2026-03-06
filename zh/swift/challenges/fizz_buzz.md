---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

创建一个接受数字作为参数并返回 `"Fizz"`、`"Buzz"` 或 `"FizzBuzz"` 的函数。

# --instructions--

- 如果数字是 `3` 的倍数，输出应为 `"Fizz"`
- 如果给定的数字是 `5` 的倍数，输出应为 `"Buzz"`。
- 如果给定的数字同时是 `3` 和 `5` 的倍数，输出应为 `"FizzBuzz"`。
- 如果数字既不是 `3` 也不是 `5` 的倍数，则应按下面的示例输出数字本身。
- 输出应始终为字符串，即使它不是 `3` 或 `5` 的倍数。

示例：
```swift
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```swift
func fizzBuzz() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

数字 `3` 必须等于 `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

数字 `5` 必须等于 `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

数字 `15` 必须等于 `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

数字 `10` 必须等于 `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

数字 `98` 必须等于 `"98"`

```swift
    func test5() {
        XCTAssertEqual(fizzBuzz(98), "98", "--err-t5--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func fizzBuzz(_ number: Int) -> String {
    if number % 3 == 0 && number % 5 == 0 {
        return "FizzBuzz"
    }
    if number % 3 == 0 {
        return "Fizz"
    }
    if number % 5 == 0 {
        return "Buzz"
    }
    return String(number)
}
```
