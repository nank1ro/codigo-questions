---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crie uma função que receba um número como argumento e retorne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Se o número for um múltiplo de `3`, a saída deve ser `"Fizz"`
- Se o número dado for um múltiplo de `5`, a saída deve ser `"Buzz"`.
- Se o número dado for um múltiplo de `3` e `5`, a saída deve ser `"FizzBuzz"`.
- Se o número não for um múltiplo de `3` ou `5`, o número deve ser exibido por si só, como mostrado nos exemplos abaixo.
- A saída deve ser sempre uma string, mesmo que não seja um múltiplo de `3` ou `5`.

Exemplos:
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

O número `3` deve ser igual a `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

O número `5` deve ser igual a `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

O número `15` deve ser igual a `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

O número `10` deve ser igual a `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

O número `98` deve ser igual a `"98"`

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
