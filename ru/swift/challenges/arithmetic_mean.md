---
language: swift
exerciseType: 1
difficulty: 1
title: Среднее арифметическое
---

# --description--

Напишите функцию `mean` для нахождения _среднего арифметического_ числового вектора.

# --instructions--

Напишите функцию, которая возвращает среднее арифметическое числового вектора.

Пример вызова функции:
```swift
print(mean([1, 2, 3]))
// prints 2.0
```

# --seed--

```swift
func mean() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Среднее арифметическое `[1, 2, 3, 4, 5, 6, 7]` должно быть равно 4.0

```swift
    func test1() {
        XCTAssertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, "--err-t1--")
    }
```

Среднее арифметическое `[4, 5, 6]` должно быть равно 5.0

```swift
    func test2() {
        XCTAssertEqual(mean([4, 5, 6]), 5.0, "--err-t2--")
    }
```

Среднее арифметическое `[12, 34, 56, 78]` должно быть равно 45.0

```swift
    func test3() {
        XCTAssertEqual(mean([12, 34, 56, 78]), 45.0, "--err-t3--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func mean(_ numbers: [Double]) -> Double {
  return numbers.reduce(0, +) / Double(numbers.count)
}
```
