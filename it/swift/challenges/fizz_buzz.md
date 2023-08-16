---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una funzione che prenda un numero come argomento e restituisca `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Se il numero è un multiplo di `3`, l'output deve essere `"Fizz"`.
- Se il numero è un multiplo di `5`, l'output deve essere `"Buzz"`.
- Se il numero è un multiplo sia di `3` che di `5`, l'output deve essere `"FizzBuzz"`.
- Se il numero non è un multiplo né di `3` né di `5`, il numero deve essere stampato come stringa, come mostrato negli esempi seguenti.
- L'output deve sempre essere una stringa, anche se non è un multiplo di `3` o `5`.

Esempi:
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

Il numero `3` deve essere uguale a `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

Il numero `5` deve essere uguale a `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

Il numero `15` deve essere uguale a `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

Il numero `10` deve essere uguale a `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

Il numero `98` deve essere uguale a `"98"`

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
