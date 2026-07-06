---
language: swift
exerciseType: 1
difficulty: 2
title: Largest product in a series
---

# --description--

Cztery sąsiadujące cyfry w liczbie 1000-cyfrowej, które mają największy iloczyn, to 9 × 9 × 8 × 9 = 5832.

# --instructions--

Napisz funkcję, która znajduje n sąsiadujących cyfr w liczbie 1000-cyfrowej o największym iloczynie i zwraca ten iloczyn.

Przykład wywołania funkcji:
```swift
print(largestProductInASeries(4))
// prints 5832
```

# --seed--

```swift
func largestProductInASeries(_ n: Int) -> Int {

}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Największy iloczyn 4 sąsiadujących cyfr musi być równy 5832

```swift
    func testLargestProduct1() {
        XCTAssertEqual(largestProductInASeries(4), 5832, "--err-t1--")
    }
```

Największy iloczyn 13 sąsiadujących cyfr musi być równy 23514624000

```swift
    func testLargestProduct2() {
        XCTAssertEqual(largestProductInASeries(13), 23514624000, "--err-t2--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testLargestProduct1", testLargestProduct1),
            ("testLargestProduct2", testLargestProduct2),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func largestProductInASeries(_ n: Int) -> Int {
    let number = "73167176531330624919225119674426574742355349194934" +
        "96983520312774506326239578318016984801869478851843" +
        "85861560789112949495459501737958331952853208805511" +
        "12540698747158523863050715693290963295227443043557" +
        "66896648950445244523161731856403098711121722383113" +
        "62229893423380308135336276614282806444486645238749" +
        "30358907296290491560440772390713810515859307960866" +
        "70172427121883998797908792274921901699720888093776" +
        "65727333001053367881220235421809751254540594752243" +
        "52584907711670556013604839586446706324415722155397" +
        "53697817977846174064955149290862569321978468622482" +
        "83972241375657056057490261407972968652414535100474" +
        "82166370484403199890008895243450658541227588666881" +
        "16427171479924442928230863465674813919123162824586" +
        "17866458359124566529476545682848912883142607690042" +
        "24219022671055626321111109370544217506941658960408" +
        "07198403850962455444362981230987879927244284909188" +
        "84580156166097919133875499200524063689912560717606" +
        "05886116467109405077541002256983155200055935729725" +
        "71636269561882670428252483600823257530420752963450"
    let digits = number.compactMap { $0.wholeNumberValue }
    var largest = 0
    for i in 0...(digits.count - n) {
        let product = digits[i..<(i + n)].reduce(1, *)
        if product > largest {
            largest = product
        }
    }
    return largest
}
```
