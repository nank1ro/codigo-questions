---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

Джеймс хотел бы снять N долларов из ATM.
Банкомат примет транзакцию только если N кратно 5, и на счёте Джеймса достаточно средств для выполнения операции снятия (включая банковскую комиссию).
За каждое успешное снятие банк взимает комиссию `0.50$`.
Рассчитайте баланс счёта Джеймса после попытки транзакции.
Входные данные указаны в следующем порядке:
1. сумма наличных, которую Джеймс хочет снять, находится в диапазоне: `0 < N <= 2000`.
2. начальный баланс Джеймса указан с точностью до двух знаков после запятой и находится в диапазоне: `0 < B <= 2000`.

# --instructions--

Верните баланс счёта после попытки транзакции в виде числа с точностью до двух знаков после запятой.
Если на счёте недостаточно средств для завершения транзакции, верните текущий баланс.

Пример вызова функции:
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

Выполнить успешную транзакцию

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

Недостаточно средств

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

Отклонённая транзакция, недопустимая сумма

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

Успешное снятие всех средств

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
