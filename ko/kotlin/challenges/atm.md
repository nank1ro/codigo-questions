---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James는 ATM에서 N달러를 인출하려고 합니다.
ATM은 N이 5의 배수이고, James의 계좌에 인출 거래를 수행하기에 충분한 잔액이 있는 경우에만 (은행 수수료 포함) 거래를 승인합니다.
인출에 성공할 때마다 은행은 `0.50$`의 수수료를 부과합니다.
인출 시도 후 James의 계좌 잔액을 계산하세요.
입력은 다음 순서로 제공됩니다:
1. James가 인출하려는 금액은 다음 범위에 있습니다: `0 < N <= 2000`.
2. James의 초기 잔액은 소수점 두 자리로 제공되며 다음 범위에 있습니다: `0 < B <= 2000`.

# --instructions--

인출 시도 후의 계좌 잔액을 소수점 두 자리 숫자로 반환하세요.
계좌에 거래를 완료하기에 충분한 잔액이 없는 경우, 현재 은행 잔액을 반환하세요.

함수 호출 예시:
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

성공적인 거래 수행

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

잔액 부족

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

거래 거부, 유효하지 않은 금액

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

모든 잔액을 성공적으로 인출

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
