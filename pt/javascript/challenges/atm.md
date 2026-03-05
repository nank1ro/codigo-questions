---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James gostaria de sacar N dólares de um ATM.
O caixa eletrônico só aceitará a transação se N for um múltiplo de 5, e a conta de James tiver saldo suficiente para realizar a transação de saque (incluindo taxas bancárias).
Para cada saque bem-sucedido, o banco cobra `0.50$`.
Calcule o saldo da conta de James após uma tentativa de transação.
As entradas estão na seguinte ordem:
1. o valor em dinheiro que James deseja sacar está no seguinte intervalo: `0 < N <= 2000`.
2. o saldo inicial de James é dado com duas casas decimais e está no seguinte intervalo: `0 < B <= 2000`.

# --instructions--

Retorne o saldo da conta após a tentativa de transação, dado como um número com duas casas decimais.
Se não houver dinheiro suficiente na conta para completar a transação, retorne o saldo bancário atual.

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

Realizar uma transação bem-sucedida

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

Fundos insuficientes

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

Transação recusada, valor inválido

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

Sacar todo o dinheiro com sucesso

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
