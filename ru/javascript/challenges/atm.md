---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

Джеймс хотел бы снять N долларов из ATM.
Банкомат примет транзакцию только если N кратно 5, и на счету Джеймса достаточно средств для выполнения операции снятия (включая банковскую комиссию).
За каждое успешное снятие банк взимает комиссию `0.50$`.
Рассчитайте баланс счёта Джеймса после попытки транзакции.
Входные данные расположены в следующем порядке:
1. сумма наличных, которую Джеймс хочет снять, находится в следующем диапазоне: `0 < N <= 2000`.
2. начальный баланс Джеймса задан с точностью до двух знаков после запятой и находится в следующем диапазоне: `0 < B <= 2000`.

# --instructions--

Верните баланс счёта после попытки транзакции в виде числа с точностью до двух знаков после запятой.
Если на счету недостаточно средств для завершения транзакции, верните текущий банковский баланс.

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

Выполнить успешную транзакцию

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

Недостаточно средств

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

Отклонённая транзакция, недопустимая сумма

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

Успешно снять все деньги

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
