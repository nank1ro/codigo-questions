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

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func accountBalance() -> Double {
    return
}
```

# --asserts--

Perform a successful transaction

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Insufficient funds

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Refused transaction, invalid amount

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Withdraw all money successfully

```swift
do {
    let expected: Double = 0.00
    tryCatch(accountBalance(95, 95.50) == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
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
