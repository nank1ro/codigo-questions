---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James desea retirar N dólares de un cajero automático.
La máquina de efectivo solo aceptará la transacción si N es múltiplo de 5, y la cuenta de James tiene suficiente dinero para realizar la transacción de retiro (incluyendo cargos bancarios).
Por cada retiro exitoso, el banco cobra `0.50$`.
Calcula el saldo de la cuenta de James después de un intento de transacción.
Las entradas están en el siguiente orden:
1. la cantidad de dinero que James desea retirar está en el siguiente rango: `0 < N <= 2000`.
2. El saldo inicial de James se proporciona con dos dígitos de precisión y está en el siguiente rango: `0 < B <= 2000`.

# --instructions--

Devuelve el saldo de la cuenta después del intento de transacción, dado como un número con dos dígitos de precisión.
Si no hay suficiente dinero en la cuenta para completar la transacción, devuelve el saldo bancario actual.

Ejemplo de llamada a la función:
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
