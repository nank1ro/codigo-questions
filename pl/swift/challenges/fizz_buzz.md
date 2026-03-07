---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Utwórz funkcję, która przyjmuje liczbę jako argument i zwraca `"Fizz"`, `"Buzz"` lub `"FizzBuzz"`.

# --instructions--

- Jeśli liczba jest wielokrotnością `3`, wynik powinien być `"Fizz"`
- Jeśli podana liczba jest wielokrotnością `5`, wynik powinien być `"Buzz"`.
- Jeśli podana liczba jest wielokrotnością zarówno `3`, jak i `5`, wynik powinien być `"FizzBuzz"`.
- Jeśli liczba nie jest wielokrotnością ani `3`, ani `5`, powinna zostać zwrócona sama liczba, jak pokazano w poniższych przykładach.
- Wynik powinien zawsze być ciągiem znaków, nawet jeśli nie jest wielokrotnością `3` ani `5`.

Przykłady:
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

Liczba `3` musi być równa `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

Liczba `5` musi być równa `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

Liczba `15` musi być równa `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

Liczba `10` musi być równa `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

Liczba `98` musi być równa `"98"`

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
