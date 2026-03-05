---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James souhaite retirer N dollars d'un guichet automatique.
Le distributeur automatique n'acceptera la transaction que si N est un multiple de 5 et que le compte de James dispose de suffisamment de fonds pour effectuer la transaction de retrait (frais bancaires inclus).
Pour chaque retrait réussi, la banque facture `0,50 $`.
Calculez le solde du compte de James après une tentative de transaction.
Les entrées sont dans l'ordre suivant :
1. le montant en espèces que James souhaite retirer est dans la plage suivante : `0 < N <= 2000`.
2. Le solde initial de James est donné avec deux chiffres de précision et est dans la plage suivante : `0 < B <= 2000`.

# --instructions--

Retournez le solde du compte après la tentative de transaction, donné sous forme de nombre avec deux chiffres de précision.
S'il n'y a pas assez d'argent sur le compte pour effectuer la transaction, retournez le solde bancaire actuel.

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

Effectuer une transaction réussie

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

Fonds insuffisants

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

Transaction refusée, montant invalide

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

Retirer tout l'argent avec succès

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
