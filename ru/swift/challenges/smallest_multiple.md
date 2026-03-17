---
language: swift
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 — это наименьшее число, которое делится на каждое из чисел от 1 до 10 без остатка.

# --instructions--

Напишите функцию, которая возвращает наименьшее положительное число, равномерно делящееся на все числа от 1 до n.

Пример вызова функции:
```swift
print(smallestMultiple(10))
// prints 2520
```

# --seed--

```swift
func smallestMultiple(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Наименьшее кратное от 1 до 5 должно быть равно 60

```swift
    func testSmallestMultiple1() {
        XCTAssertEqual(smallestMultiple(5), 60, "--err-t1--")
    }
```

Наименьшее кратное от 1 до 10 должно быть равно 2520

```swift
    func testSmallestMultiple2() {
        XCTAssertEqual(smallestMultiple(10), 2520, "--err-t2--")
    }
```

Наименьшее кратное от 1 до 20 должно быть равно 232792560

```swift
    func testSmallestMultiple3() {
        XCTAssertEqual(smallestMultiple(20), 232792560, "--err-t3--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSmallestMultiple1", testSmallestMultiple1),
            ("testSmallestMultiple2", testSmallestMultiple2),
            ("testSmallestMultiple3", testSmallestMultiple3),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    return (1...n).reduce(1) { lcm($0, $1) }
}
```
