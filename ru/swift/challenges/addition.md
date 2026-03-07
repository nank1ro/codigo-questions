---
language: swift
exerciseType: 1
difficulty: 1
title: Сложение
---

# --description--

Даны два целых числа `num1` и `num2`, напишите программу для сложения этих двух чисел

# --instructions--

Напишите функцию, которая возвращает сумму двух чисел.
> ПОДСКАЗКА: опустите метки аргументов с помощью `_` (нижнее подчёркивание)

Пример вызова функции:
```swift
print(addition(1, 2))
// prints 3
```

# --seed--

```swift
func addition() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Сумма 1 и 3 должна быть равна 4

```swift
    func testAddition1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

Сумма 200 и 210 должна быть равна 410

```swift
    func testAddition2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

Сумма 15 и 35 должна быть равна 50

```swift
    func testAddition3() {
        XCTAssertEqual(addition(15, 35), 50, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testAddition1", testAddition1),
            ("testAddition2", testAddition2),
            ("testAddition3", testAddition3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
