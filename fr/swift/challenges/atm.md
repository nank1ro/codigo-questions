---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James aimerait retirer N dollars d'un guichet automatique.
Le guichet automatique n'acceptera la transaction que si N est un multiple de 5 et que le compte de James a suffisamment d'argent pour effectuer la transaction de retrait (frais bancaires inclus).
Pour chaque retrait réussi, la banque facture `0,50 $`.
Calculez le solde du compte de James après une tentative de transaction.
Les entrées sont dans l'ordre suivant :
1. Le montant d'argent que James souhaite retirer est dans la plage suivante : `0 < N <= 2000`.
2. Le solde initial de James est donné avec deux décimales et est dans la plage suivante : `0 < B <= 2000`.

# --instructions--

Retournez le solde du compte après la tentative de transaction, donné sous forme de nombre avec deux décimales.
S'il n'y a pas assez d'argent sur le compte pour effectuer la transaction, retournez le solde bancaire actuel.

> ASTUCE : omettez les étiquettes d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
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

Effectuer une transaction réussie

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Fonds insuffisants

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Transaction refusée, montant invalide

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Retirer tout l'argent avec succès

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
