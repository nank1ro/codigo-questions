---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Crea un funcion ese toma un numero como un argumento y devuelve `"Fizz"`, `"Buzz"` o `"FizzBuzz"`.

# --instructions--

- si el numero es un multiples de `3` el salida deberia ser `"Fizz"`
- si el numero dado es un multiples de `5`, el salida deberia ser `"Buzz"`.
- si el numero dado es un multiples de both `3` y `5`, el salida deberia ser `"FizzBuzz"`.
- si el numero es no un multiples de either `3` o `5`, el numero deberia ser salida en su propio como mostrado en el ejemplos below.
- The salida deberia siempre ser un cadena even si lo es no un multiples de `3` o `5`.

ejemplos:
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

The number `3` must equal `"Fizz"`

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

The number `5` must equal `"Buzz"`

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

The number `15` must equal `"FizzBuzz"`

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

The number `10` must equal `"Buzz"`

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

The number `98` must equal `"98"`

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
func fizzBuzz(_ numero: Int) -> String {
    if numero % 3 == 0 && numero % 5 == 0 {
        return "FizzBuzz"
    }
    if numero % 3 == 0 {
        return "Fizz"
    }
    if numero % 5 == 0 {
        return "Buzz"
    }
    return String(numero)
}
```
