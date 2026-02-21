---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James habria like un withdraw N dollars de un ATM.
The cash machine podra solo accept el transaction si N es un multiples de 5, y James' account tiene enough cash un realizar el withdrawal transaction (including bank charges).
para cada successful withdrawal el bank charges `0.50$`.
Calcula James' account balance despues un attempted transaction.
The inputs son en el siguiente orden:
1. el amount de cash cual James wishes un withdraw es en el siguiendo range: `0 < N <= 2000`.
2. James' initial balance es gived con dos digits de precision y es en el siguiendo range: `0 < B <= 2000`.

# --instructions--

Devuelve el account balance despues el attempted transaction, dado como un numero con dos digits de precision.
si ahi es no enough money en el account un complete el transaction, Devuelve el current bank balance.

> HINT: omit el argumento labels con el `_` (underscore)

ejemplo de funcion llamar:
```swift
print(accountBalance(10, 20))
// prints 9,5
```

# --seed--

```swift
func accountBalance() -> Double {
    return
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Perform a successful transaction

```swift
    func testSuccessfulTransaction() {
        let expected: Double = 69.50
        XCTAssertEqual(accountBalance(50, 120.00), expected, "--err-t1--")
    }
```

Insufficient funds

```swift
    func testInsufficientFunds() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(200, 120.00), expected, "--err-t2--")
    }
```

Refused transaction, invalid amount

```swift
    func testNotMultipleOf5() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(22, 120.00), expected, "--err-t3--")
    }
```

Withdraw all money successfully

```swift
    func testWithdrawAll() {
        let expected: Double = 0.00
        XCTAssertEqual(accountBalance(95, 95.50), expected, "--err-t4--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSuccessfulTransaction", testSuccessfulTransaction),
            ("testInsufficientFunds", testInsufficientFunds),
            ("testNotMultipleOf5", testNotMultipleOf5),
            ("testWithdrawAll", testWithdrawAll),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func accountBalance(_ withdraw: Double,_ balance: Double) -> Double {
    let isMultipleOf5 = withdraw.truncatingRemainder(dividingBy: 5) == 0;
    let isAmountAvailable = balance >= (withdraw + 0.50)
    if isMultipleOf5 && isAmountAvailable {
        return balance - withdraw - 0.50
    }
    return balance
}
```
