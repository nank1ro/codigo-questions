---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

फिबोनाची अनुक्रम में प्रत्येक नया पद पिछले दो पदों को जोड़कर बनाया जाता है। 1 और 2 से शुरू करने पर पहले 10 पद होंगे: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

फिबोनाची अनुक्रम के उन पदों पर विचार करें जिनके मान `n` से अधिक नहीं हैं, और सम-मूल्य वाले पदों का योग ज्ञात करें।

# --seed--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

आपके फ़ंक्शन को एक सम मान लौटाना चाहिए।

```swift
    func test1() {
        XCTAssertEqual(fibonacciEvenSum(10) % 2, 0, "--err-t1--")
    }
```

`fibonacciEvenSum(8)` को 10 लौटाना चाहिए।

```swift
    func test2() {
        XCTAssertEqual(fibonacciEvenSum(8), 10, "--err-t2--")
    }
```

`fibonacciEvenSum(10)` को 10 लौटाना चाहिए।

```swift
    func test3() {
        XCTAssertEqual(fibonacciEvenSum(10), 10, "--err-t3--")
    }
```

`fibonacciEvenSum(34)` को 44 लौटाना चाहिए।

```swift
    func test4() {
        XCTAssertEqual(fibonacciEvenSum(34), 44, "--err-t4--")
    }
```

`fibonacciEvenSum(60)` को 44 लौटाना चाहिए।

```swift
    func test5() {
        XCTAssertEqual(fibonacciEvenSum(60), 44, "--err-t5--")
    }
```

`fibonacciEvenSum(1000)` को 798 लौटाना चाहिए।

```swift
    func test6() {
        XCTAssertEqual(fibonacciEvenSum(1000), 798, "--err-t6--")
    }
```

`fibonacciEvenSum(100000)` को 60696 लौटाना चाहिए।

```swift
    func test7() {
        XCTAssertEqual(fibonacciEvenSum(100000), 60696, "--err-t7--")
    }
```

`fibonacciEvenSum(4000000)` को 4613732 लौटाना चाहिए।

```swift
    func test8() {
        XCTAssertEqual(fibonacciEvenSum(4000000), 4613732, "--err-t8--")
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
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func fibonacciEvenSum(_ number: Int) -> Int {
    if number <= 1 { return 0 }
    var evenSum = 0
    var prevFibNum = 1
    var fibNum = 2
    while fibNum <= number {
        if fibNum % 2 == 0 {
            evenSum += fibNum
        }
        let next = prevFibNum + fibNum
        prevFibNum = fibNum
        fibNum = next
    }
    return evenSum
}
```
