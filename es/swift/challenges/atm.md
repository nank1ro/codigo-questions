---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James quiere retirar N dólares de un cajero automático.
La máquina de efectivo solo aceptará la transacción si N es un múltiplo de 5, y la cuenta de James tiene suficiente efectivo para realizar la transacción de retiro (incluidos los cargos bancarios).
Por cada retiro exitoso, el banco cobra `0.50$`.
Calcula el saldo de la cuenta de James después de un intento de transacción.
Las entradas están en el siguiente orden:
1. la cantidad de efectivo que James desea retirar está en el siguiente rango: `0 < N <= 2000`.
2. el saldo inicial de James se da con dos dígitos de precisión y está en el siguiente rango: `0 < B <= 2000`.

# --instructions--

Devuelve el saldo de la cuenta después del intento de transacción, dado como un número con dos dígitos de precisión.
Si no hay suficiente dinero en la cuenta para completar la transacción, devuelve el saldo bancario actual.

> PISTA: omite las etiquetas de argumento con el `_` (guion bajo)

Ejemplo de llamada de función:
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

Realizar una transacción exitosa

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Fondos insuficientes

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Transacción rechazada, cantidad inválida

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Retirar todo el dinero exitosamente

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
