---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James desea retirar N dólares de un cajero automático.
El cajero automático solo aceptará la transacción si N es un múltiplo de 5 y la cuenta de James tiene suficiente efectivo para realizar la transacción de retiro (incluidos los cargos bancarios).
Por cada retiro exitoso, el banco cobra `0.50$`.
Calcula el saldo de la cuenta de James después de un intento de transacción.
Las entradas están en el siguiente orden:
1. la cantidad de efectivo que James desea retirar está en el siguiente rango: `0 < N <= 2000`.
2. El saldo inicial de James se proporciona con dos dígitos de precisión y está en el siguiente rango: `0 < B <= 2000`.

# --instructions--

Retorna el saldo de la cuenta después del intento de transacción, dado como un número con dos dígitos de precisión.
Si no hay suficiente dinero en la cuenta para completar la transacción, retorna el saldo bancario actual.

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function accountBalance() {
  
}
```

# --asserts--

Realizar una transacción exitosa

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

Fondos insuficientes

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

Transacción rechazada, cantidad inválida

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

Retirar todo el dinero con éxito

```javascript
tryCatch(accountBalance(95, 95.50) === 0.00);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function accountBalance(withdraw, balance) {
  if ((withdraw % 5 == 0) && (balance >= (withdraw + 0.50))) {
    return balance - withdraw - 0.50;
  }
  return balance;
}
```
