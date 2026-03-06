---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James想从ATM取款N美元。
ATM只会在N是5的倍数且James的账户有足够的现金来执行取款交易（包括银行手续费）时才接受交易。
每次成功取款，银行收取 `0.50$` 的手续费。
计算James尝试交易后的账户余额。
输入按以下顺序排列：
1. James希望取款的金额在以下范围内：`0 < N <= 2000`。
2. James的初始余额精确到小数点后两位，范围为：`0 < B <= 2000`。

# --instructions--

返回尝试交易后的账户余额，精确到小数点后两位。
如果账户中没有足够的资金完成交易，返回当前银行余额。

函数调用示例：
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

执行一次成功的交易

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

资金不足

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

交易被拒绝，金额无效

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

成功取出所有资金

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
