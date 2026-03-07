---
language: swift
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Twoim zadaniem jest zamiana liczby na ciąg znaków zawierający dźwięki kropli deszczu odpowiadające określonym potencjalnym dzielnikOm.
Dzielnik to liczba, która dzieli inną liczbę bez reszty.
Najprostszym sposobem sprawdzenia, czy liczba jest dzielnikiem innej, jest użycie operacji modulo.
Zasady Raindrops są następujące — jeśli dana liczba:

- ma 3 jako dzielnik, dodaj 'Pling' do wyniku.
- ma 5 jako dzielnik, dodaj 'Plang' do wyniku.
- ma 7 jako dzielnik, dodaj 'Plong' do wyniku.
- nie ma żadnego z 3, 5 ani 7 jako dzielnika, wynikiem powinny być cyfry tej liczby.

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

- 28 ma 7 jako dzielnik, ale nie 3 ani 5, więc wynik to `"Plong"`.
- 30 ma zarówno 3, jak i 5 jako dzielniki, ale nie 7, więc wynik to `"PlingPlang"`.
- 34 nie jest podzielne przez 3, 5 ani 7, więc wynik to `"34"`.

> WSKAZÓWKA: pomiń etykietę argumentu używając `_` (podkreślnika)

Przykład wywołania funkcji:
```swift
print(raindrops(28))
// prints "Plong"
```

# --seed--

```swift
func raindrops() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Dźwięk dla 1 to "1"

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

Dźwięk dla 3 to "Pling"

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

Dźwięk dla 5 to "Plang"

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

Dźwięk dla 7 to "Plong"

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

Dźwięk dla 6 to "Pling"

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

Dźwięk dla 8 to "8"

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

Dźwięk dla 9 to "Pling"

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

Dźwięk dla 10 to "Plang"

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

Dźwięk dla 14 to "Plong"

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

Dźwięk dla 15 to "PlingPlang"

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

Dźwięk dla 21 to "PlingPlong"

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

Dźwięk dla 25 to "Plang"

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

Dźwięk dla 27 to "Pling"

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

Dźwięk dla 35 to "PlangPlong"

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

Dźwięk dla 49 to "Plong"

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

Dźwięk dla 52 to "52"

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

Dźwięk dla 105 to "PlingPlangPlong"

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

Dźwięk dla 3125 to "Plang"

```swift
    func test3125() {
        XCTAssertEqual("Plang", raindrops(3125), "--err-t18--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test3", test3),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test14", test14),
            ("test15", test15),
            ("test21", test21),
            ("test25", test25),
            ("test27", test27),
            ("test35", test35),
            ("test49", test49),
            ("test52", test52),
            ("test105", test105),
            ("test3125", test3125),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


