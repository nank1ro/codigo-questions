---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James souhaite retirer N dollars d'un guichet automatique.
Le distributeur n'acceptera la transaction que si N est un multiple de 5, et le compte de James dispose de suffisamment de fonds pour effectuer la transaction de retrait (y compris les frais bancaires).
Pour chaque retrait réussi, la banque facture `0.50$`.
Calculez le solde du compte de James après une tentative de transaction.
Les entrées sont dans l'ordre suivant :
1. le montant en espèces que James souhaite retirer est dans la plage suivante : `0 < N <= 2000`.
2. Le solde initial de James est donné avec deux chiffres de précision et est dans la plage suivante : `0 < B <= 2000`.

# --instructions--

Retournez le solde du compte après la tentative de transaction, donné en tant que nombre avec deux chiffres de précision.
S'il n'y a pas assez d'argent sur le compte pour effectuer la transaction, retournez le solde bancaire actuel.

Exemple d'appel de fonction :
```kotlin
println(accountBalance(10, 20.00))
// affiche 9.5
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

Effectuer une transaction réussie

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

Fonds insuffisants

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

Transaction refusée, montant invalide

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

Retirer tout l'argent avec succès

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
