---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea una función que tome un número como argumento y devuelva `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- Si el número es un múltiplo de `3`, la salida debe ser `"Fizz"`
- Si el número dado es un múltiplo de `5`, la salida debe ser `"Buzz"`.
- Si el número dado es un múltiplo de `3` y `5`, la salida debe ser `"FizzBuzz"`.
- Si el número no es un múltiplo de `3` o `5`, el número debe mostrarse por sí solo como se muestra en los ejemplos a continuación.
- La salida siempre debe ser una cadena incluso si no es un múltiplo de `3` o `5`.

Ejemplos:
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

El número `3` debe ser igual a `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

El número `5` debe ser igual a `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

El número `15` debe ser igual a `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

El número `10` debe ser igual a `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

El número `98` debe ser igual a `"98"`

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
