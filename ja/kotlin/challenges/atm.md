---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

ジェームズはATMからNドルを引き出したいと考えています。
ATMは、Nが5の倍数であり、かつジェームズの口座に引き出し取引を行うのに十分な残高がある場合（銀行手数料を含む）のみ取引を受け付けます。
引き出しが成功するたびに、銀行は`0.50$`の手数料を請求します。
引き出し取引の試行後のジェームズの口座残高を計算してください。
入力は以下の順序です：
1. ジェームズが引き出したい金額は次の範囲にあります：`0 < N <= 2000`。
2. ジェームズの初期残高は小数点以下2桁で示され、次の範囲にあります：`0 < B <= 2000`。

# --instructions--

引き出し取引の試行後の口座残高を、小数点以下2桁の数値として返してください。
口座に取引を完了するのに十分な残高がない場合は、現在の銀行残高を返してください。

関数呼び出しの例：
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

引き出し成功

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

残高不足

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

取引拒否、無効な金額

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

全額引き出し成功

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
