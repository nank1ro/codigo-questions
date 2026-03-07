---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Создайте функцию, которая принимает число в качестве аргумента и возвращает `"Fizz"`, `"Buzz"` или `"FizzBuzz"`.

# --instructions--

- Если число кратно `3`, вывод должен быть `"Fizz"`
- Если число кратно `5`, вывод должен быть `"Buzz"`.
- Если число кратно и `3`, и `5`, вывод должен быть `"FizzBuzz"`.
- Если число не кратно ни `3`, ни `5`, число должно быть выведено как есть, как показано в примерах ниже.
- Вывод всегда должен быть строкой, даже если число не кратно `3` или `5`.

Примеры:
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

Число `3` должно равняться `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

Число `5` должно равняться `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

Число `15` должно равняться `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

Число `10` должно равняться `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

Число `98` должно равняться `"98"`

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
