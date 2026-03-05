---
language: kotlin
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

Example of function call:
```kotlin
println(accountBalance(10, 20.00))
// prints 9.5
```

# --seed--

```kotlin
fun accountBalance(): Double {
    return
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Perform a successful transaction

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

Insufficient funds

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

Refused transaction, invalid amount

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

Withdraw all money successfully

```kotlin
    tryCatch(accountBalance(95, 95.50) == 0.00)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun accountBalance(withdraw: Int, balance: Double): Double {
    val isMultipleOf5 = withdraw.rem(5) == 0;
    val isAmountAvailable = balance >= (withdraw + 0.50)
    if (isMultipleOf5 && isAmountAvailable) {
        return balance - withdraw - 0.50
    }
    return balance
}
```
