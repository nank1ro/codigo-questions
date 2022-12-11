---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James vorrebbe prelevare N euro da un bancomat.
Il bancomat accetterà la transazione solo se N è un multiplo di 5 e il conto di James ha abbastanza contante per eseguire il prelievo (incluse le commissioni bancarie).
Per ogni prelievo effettuato con successo, la banca addebita 0.50€.
Calcola il saldo del conto di James dopo un tentativo di transazione.
Gli input sono nell'ordine seguente:
1. la quantità di contanti che James desidera prelevare è nel seguente intervallo: `0 < N <= 2000`.
2. Il saldo iniziale di James viene fornito con due cifre decimali ed è nel seguente intervallo: `0 < B <= 2000`.

# --instructions--

Restituisci il saldo del conto, con due cifre decimali, dopo il tentativo di transazione.
Se non c'è abbastanza denaro nel conto per completare l'operazione, restituire il saldo bancario corrente.

Esempio di chiamata della funzione:
```dart
print(accountBalance(10, 20.00))
// stampa 9.5
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

Esegui una transazione con successo

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Fondi insufficienti

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Transazione rifiutata, importo non valido

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Preleva tutti i soldi con successo

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
