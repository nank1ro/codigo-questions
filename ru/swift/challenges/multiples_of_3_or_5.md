---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Если перечислить все натуральные числа до 10, кратные 3 или 5, получим 3, 5, 6 и 9. Сумма этих кратных равна 23.

# --instructions--

Напишите функцию, которая находит сумму всех кратных 3 или 5, меньших заданного числа.

Пример вызова функции:
```swift
print(multiplesOf3And5(10))
// prints 23
```

# --seed--

```swift
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Сумма кратных 3 или 5, меньших 10, должна быть равна 23

```swift
    func testMultiples1() {
        XCTAssertEqual(multiplesOf3And5(10), 23, "--err-t1--")
    }
```

Сумма кратных 3 или 5, меньших 1000, должна быть равна 233168

```swift
    func testMultiples2() {
        XCTAssertEqual(multiplesOf3And5(1000), 233168, "--err-t2--")
    }
```

Сумма кратных 3 или 5, меньших 6987, должна быть равна 11390208

```swift
    func testMultiples3() {
        XCTAssertEqual(multiplesOf3And5(6987), 11390208, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testMultiples1", testMultiples1),
            ("testMultiples2", testMultiples2),
            ("testMultiples3", testMultiples3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
