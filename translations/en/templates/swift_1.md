---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Given two integers `num1` and `num2`, write a program to add these two numbers

# --instructions--

Write a function that returns the sum of two numbers.
> HINT: omit the argument labels with the `_` (underscore)

Example of function call:
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

The sum of 1 and 3 must equal 4

```swift
    func test1() {
        XCTAssertEqual(addition(1, 3), 4, "--err-t1--")
    }
```

The sum of 200 and 210 must equal 410

```swift
    func test2() {
        XCTAssertEqual(addition(200, 210), 410, "--err-t2--")
    }
```

The sum of 15 and 35 must equal 50

```swift
    func test3() {
        XCTAssertEqual(addition(15, 35), 50, "--err-t3--")
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
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
