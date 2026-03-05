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

Effectuer une transaction réussie

```swift
    func testSuccessfulTransaction() {
        let expected: Double = 69.50
        XCTAssertEqual(accountBalance(50, 120.00), expected, "--err-t1--")
    }
```

Fonds insuffisants

```swift
    func testInsufficientFunds() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(200, 120.00), expected, "--err-t2--")
    }
```

Transaction refusée, montant invalide

```swift
    func testNotMultipleOf5() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(22, 120.00), expected, "--err-t3--")
    }
```

Retirer tout l'argent avec succès

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
