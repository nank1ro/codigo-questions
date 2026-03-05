---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James möchte N Dollar von einem Geldautomaten abheben.
Der Geldautomat akzeptiert die Transaktion nur, wenn N ein Vielfaches von 5 ist und James' Konto genug Geld für die Abhebungstransaktion hat (inklusive Bankgebühren).
Für jede erfolgreiche Auszahlung berechnet die Bank `0,50$`.
Berechnen Sie James' Kontostand nach einer versuchten Transaktion.
Die Eingaben sind in der folgenden Reihenfolge:
1. Der Geldbetrag, den James abheben möchte, liegt in folgendem Bereich: `0 < N <= 2000`.
2. James' Anfangsguthaben wird mit zwei Dezimalstellen angegeben und liegt in folgendem Bereich: `0 < B <= 2000`.

# --instructions--

Geben Sie den Kontostand nach der versuchten Transaktion als Zahl mit zwei Dezimalstellen zurück.
Wenn nicht genug Geld auf dem Konto ist, um die Transaktion abzuschließen, geben Sie das aktuelle Bankguthaben zurück.

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

Eine erfolgreiche Transaktion durchführen

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

Unzureichende Deckung

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

Transaktion abgelehnt, ungültiger Betrag

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

Erfolgreich das ganze Geld abheben

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
