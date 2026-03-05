---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Erstellen Sie eine Funktion, die eine Zahl als Argument akzeptiert und `"Fizz"`, `"Buzz"` oder `"FizzBuzz"` zurückgibt.

# --instructions--

- Wenn die Zahl ein Vielfaches von `3` ist, sollte die Ausgabe `"Fizz"` sein
- Wenn die angegebene Zahl ein Vielfaches von `5` ist, sollte die Ausgabe `"Buzz"` sein.
- Wenn die angegebene Zahl ein Vielfaches von beiden `3` und `5` ist, sollte die Ausgabe `"FizzBuzz"` sein.
- Wenn die Zahl kein Vielfaches von `3` oder `5` ist, sollte die Zahl selbst als Ausgabe erfolgen, wie in den Beispielen unten gezeigt.
- Die Ausgabe sollte immer ein String sein, auch wenn es kein Vielfaches von `3` oder `5` ist.

Examples:
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

Die Zahl `3` muss gleich `"Fizz"` sein

```swift
    func test1() {
        XCTAssertEqual(fizzBuzz(3), "Fizz", "--err-t1--")
    }
```

Die Zahl `5` muss gleich `"Buzz"` sein

```swift
    func test2() {
        XCTAssertEqual(fizzBuzz(5), "Buzz", "--err-t2--")
    }
```

Die Zahl `15` muss gleich `"FizzBuzz"` sein

```swift
    func test3() {
        XCTAssertEqual(fizzBuzz(15), "FizzBuzz", "--err-t3--")
    }
```

Die Zahl `10` muss gleich `"Buzz"` sein

```swift
    func test4() {
        XCTAssertEqual(fizzBuzz(10), "Buzz", "--err-t4--")
    }
```

Die Zahl `98` muss gleich `"98"` sein

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
