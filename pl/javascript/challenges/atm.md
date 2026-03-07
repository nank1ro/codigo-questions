---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James chciałby wypłacić N dolarów z bankomatu.
Bankomat zaakceptuje transakcję tylko wtedy, gdy N jest wielokrotnością 5, a konto Jamesa ma wystarczające środki na dokonanie wypłaty (wliczając opłaty bankowe).
Za każdą udaną wypłatę bank pobiera `0,50$`.
Oblicz stan konta Jamesa po próbie transakcji.
Dane wejściowe są w następującej kolejności:
1. kwota, którą James chce wypłacić, mieści się w zakresie: `0 < N <= 2000`.
2. początkowe saldo Jamesa podane jest z dokładnością do dwóch miejsc po przecinku i mieści się w zakresie: `0 < B <= 2000`.

# --instructions--

Zwróć stan konta po próbie transakcji, jako liczbę z dokładnością do dwóch miejsc po przecinku.
Jeśli na koncie nie ma wystarczających środków do zrealizowania transakcji, zwróć bieżące saldo konta.

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

Wykonaj udaną transakcję

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

Niewystarczające środki

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

Odrzucona transakcja, nieprawidłowa kwota

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

Wypłać wszystkie pieniądze pomyślnie

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
