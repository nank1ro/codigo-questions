---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

숫자를 인수로 받아 `"Fizz"`, `"Buzz"` 또는 `"FizzBuzz"`를 반환하는 함수를 만드십시오.

# --instructions--

- 숫자가 `3`의 배수이면 출력은 `"Fizz"`여야 합니다
- 주어진 숫자가 `5`의 배수이면 출력은 `"Buzz"`여야 합니다.
- 주어진 숫자가 `3`과 `5`의 배수이면 출력은 `"FizzBuzz"`여야 합니다.
- 숫자가 `3`이나 `5`의 배수가 아니면 아래 예시와 같이 숫자 자체를 출력해야 합니다.
- 출력은 `3`이나 `5`의 배수가 아니더라도 항상 문자열이어야 합니다.

예시:
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

숫자 `3`은 `"Fizz"`와 같아야 합니다

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

숫자 `5`는 `"Buzz"`와 같아야 합니다

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

숫자 `15`는 `"FizzBuzz"`와 같아야 합니다

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

숫자 `10`은 `"Buzz"`와 같아야 합니다

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

숫자 `98`은 `"98"`과 같아야 합니다

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
