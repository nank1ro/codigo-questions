---
language: swift
exerciseType: 1
difficulty: 1
title: Somma cifre
---

# --description--

Ti viene dato un numero intero `N`.
Scrivi un programma per calcolare la somma di tutte le cifre di N

# --instructions--

Restituisci la somma delle cifre di `N`
> SUGGERIMENTO: ometti il nome dell'argomento con l'underscore `_` (underscore)

Esempio di chiamata della funzione:
```swift
print(sommaCifre(28))
// stampa 10
```

# --seed--

```swift
func sommaCifre() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

La somma delle cifre di 12345 è 15

```swift
    func testSumOfDigits1() {
        XCTAssertEqual(sommaCifre(12345), 15, "--err-t1--")
    }
```

La somma delle cifre di 57253 è 22

```swift
    func testSumOfDigits2() {
        XCTAssertEqual(sommaCifre(57253), 22, "--err-t2--")
    }
```

La somma delle cifre di 122 è 5

```swift
    func testSumOfDigits3() {
        XCTAssertEqual(sommaCifre(122), 5, "--err-t3--")
    }
```

La somma delle cifre di 91979997 è 60

```swift
    func testSumOfDigits4() {
        XCTAssertEqual(sommaCifre(91979997), 60, "--err-t4--")
    }
```

La somma delle cifre di 2147483647 è 46

```swift
    func testSumOfDigits5() {
        XCTAssertEqual(sommaCifre(2147483647), 46, "--err-t5--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSumOfDigits1", testSumOfDigits1),
            ("testSumOfDigits2", testSumOfDigits2),
            ("testSumOfDigits3", testSumOfDigits3),
            ("testSumOfDigits4", testSumOfDigits4),
            ("testSumOfDigits5", testSumOfDigits5),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func sommaCifre(_ num: Int) -> Int {
    var n = num
    var risultato = 0
    while n > 0 {
        risultato += n % 10
        n = Int(n / 10)
    }
    return risultato
}
```


