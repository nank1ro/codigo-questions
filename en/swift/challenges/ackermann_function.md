---
language: swift
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

The Ackermann function is a classic example of a recursive function, notable especially because it is not a primitive recursive function. It grows very quickly in value, as does the size of its call tree.

The Ackermann function is usually defined as follows:

![ackermann_function](https://bit.ly/3z9u4zh)

Its arguments are never negative and it always terminates

# --instructions--

Write a function which returns the value of the Ackermann function.

# --seed--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`ack(0, 0)` should return 1.

```swift
    func test1() {
        XCTAssertEqual(ack(0, 0), 1, "--err-t1--")
    }
```

`ack(1, 1)` should return 3.

```swift
    func test2() {
        XCTAssertEqual(ack(1, 1), 3, "--err-t2--")
    }
```

`ack(2, 5)` should return 13.

```swift
    func test3() {
        XCTAssertEqual(ack(2, 5), 13, "--err-t3--")
    }
```

`ack(3, 3)` should return 61.

```swift
    func test4() {
        XCTAssertEqual(ack(3, 3), 61, "--err-t4--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
