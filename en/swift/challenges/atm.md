---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James would like to withdraw N dollars from an ATM.
The cash machine will only accept the transaction if N is a multiple of 5, and James' account has enough cash to perform the withdrawal transaction (including bank charges).
For each successful withdrawal the bank charges `0.50$`.
Calculate James' account balance after an attempted transaction.
The inputs are in the following order:
1. the amount of cash which James wishes to withdraw is in the following range: `0 < N <= 2000`.
2. James' initial balance is gived with two digits of precision and is in the following range: `0 < B <= 2000`.

# --instructions--

Return the account balance after the attempted transaction, given as a number with two digits of precision.
If there is not enough money in the account to complete the transaction, return the current bank balance.

> HINT: omit the argument labels with the `_` (underscore)

Example of function call:
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

class ATMTests: XCTestCase {
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

extension ATMTests {
    static var allTests : [(String, (ATMTests) -> () throws -> Void)] {
        return [
            ("testSuccessfulTransaction", testSuccessfulTransaction),
            ("testInsufficientFunds", testInsufficientFunds),
            ("testNotMultipleOf5", testNotMultipleOf5),
            ("testWithdrawAll", testWithdrawAll),
        ]
    }
}

XCTMain([testCase(ATMTests.allTests)])
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
