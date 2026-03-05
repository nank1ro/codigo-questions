---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Créez une fonction qui prend un nombre comme argument et retourne `"Fizz"`, `"Buzz"` ou `"FizzBuzz"`.

# --instructions--

- Si le nombre est un multiple de `3`, la sortie doit être `"Fizz"`
- Si le nombre donné est un multiple de `5`, la sortie doit être `"Buzz"`.
- Si le nombre donné est un multiple de `3` et de `5`, la sortie doit être `"FizzBuzz"`.
- Si le nombre n'est pas un multiple de `3` ou de `5`, le nombre doit être sorti seul comme indiqué dans les exemples ci-dessous.
- La sortie doit toujours être une chaîne même si elle n'est pas un multiple de `3` ou de `5`.

Exemples :
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

Le nombre `3` doit être égal à `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

Le nombre `5` doit être égal à `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

Le nombre `15` doit être égal à `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

Le nombre `10` doit être égal à `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

Le nombre `98` doit être égal à `"98"`

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
