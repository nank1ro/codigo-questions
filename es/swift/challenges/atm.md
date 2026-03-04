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

Realizar una transacción exitosa

```swift
    func testSuccessfulTransaction() {
        let expected: Double = 69.50
        XCTAssertEqual(accountBalance(50, 120.00), expected, "--err-t1--")
    }
```

Fondos insuficientes

```swift
    func testInsufficientFunds() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(200, 120.00), expected, "--err-t2--")
    }
```

Transacción rechazada, cantidad inválida

```swift
    func testNotMultipleOf5() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(22, 120.00), expected, "--err-t3--")
    }
```

Retirar todo el dinero exitosamente

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
