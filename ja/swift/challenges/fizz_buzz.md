---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

数値を引数として受け取り、`"Fizz"`、`"Buzz"`、または `"FizzBuzz"` を返す関数を作成してください。

# --instructions--

- 数が `3` の倍数の場合、出力は `"Fizz"` になります
- 与えられた数が `5` の倍数の場合、出力は `"Buzz"` になります。
- 与えられた数が `3` と `5` の両方の倍数の場合、出力は `"FizzBuzz"` になります。
- 数が `3` でも `5` の倍数でもない場合、以下の例に示すように数値そのものを出力します。
- 出力は `3` や `5` の倍数でなくても常に文字列でなければなりません。

例:
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

数 `3` は `"Fizz"` に等しくなければなりません

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

数 `5` は `"Buzz"` に等しくなければなりません

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

数 `15` は `"FizzBuzz"` に等しくなければなりません

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

数 `10` は `"Buzz"` に等しくなければなりません

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

数 `98` は `"98"` に等しくなければなりません

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
