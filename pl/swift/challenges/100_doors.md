---
language: swift
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

W rzędzie znajduje się 100 drzwi, wszystkie początkowo zamknięte.
Wykonujesz 100 przejść obok drzwi.
Za pierwszym razem odwiedzasz każde drzwi i „przełączasz" je (jeśli drzwi są zamknięte, otwierasz je; jeśli są otwarte, zamykasz je).
Za drugim razem odwiedzasz tylko co 2. drzwi (tj. drzwi nr 2, 4, 6, ...) i przełączasz je.
Za trzecim razem odwiedzasz co 3. drzwi (tj. drzwi nr 3, 6, 9, ...) itd., aż do momentu gdy odwiedzisz tylko 100. drzwi.

# --instructions--

Zaimplementuj funkcję, która określa stan drzwi po ostatnim przejściu.
Zwróć końcowy wynik w tablicy, zawierającej tylko numery drzwi, które są otwarte.
> Metoda musi działać dla zmiennej liczby drzwi.

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Dla 100 drzwi zwróć poprawną listę otwartych drzwi

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

Dla 10 drzwi zwróć poprawną listę otwartych drzwi

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

Dla 950 drzwi zwróć poprawną listę otwartych drzwi

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
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
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
