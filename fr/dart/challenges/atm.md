---
language: dart
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James aimerait retirer N dollars d'un guichet automatique.
La machine à espèces n'acceptera la transaction que si N est un multiple de 5, et que le compte de James dispose d'assez d'argent pour effectuer la transaction de retrait (y compris les frais bancaires).
Pour chaque retrait réussi, la banque facture `0,50 $`.
Calculez le solde du compte de James après une tentative de transaction.
Les entrées sont dans l'ordre suivant :
1. le montant en espèces que James souhaite retirer est dans la plage suivante : `0 < N <= 2000`.
2. Le solde initial de James est donné avec deux chiffres de précision et est dans la plage suivante : `0 < B <= 2000`.

# --instructions--

Retournez le solde du compte après la tentative de transaction, donné sous la forme d'un nombre avec deux chiffres de précision.
S'il n'y a pas assez d'argent sur le compte pour effectuer la transaction, retournez le solde bancaire actuel.

Exemple d'appel de fonction :
```dart
print(accountBalance(10, 20.00))
// prints 9.5
```

# --seed--

```dart
double accountBalance() {
    return
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

Effectuer une transaction réussie

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Fonds insuffisants

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Transaction refusée, montant invalide

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Retirer tout l'argent avec succès

```dart
    test('test4', () {
      expect(accountBalance(95, 95.50), 0.00, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
double accountBalance(int withdraw, double balance) {
  final isMultipleOf5 = withdraw % 5 == 0;
  final isAmountAvailable = balance >= (withdraw + 0.50);
  if (isMultipleOf5 && isAmountAvailable) {
    return balance - withdraw - 0.50;
  }
  return balance;
}
```
