---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James mochte N Dollar von einem Geldautomaten abheben.
Der Geldautomat akzeptiert die Transaktion nur, wenn N ein Vielfaches von 5 ist und James' Konto genug Geld hat, um die Abhebetransaktion durchzufuhren (einschlieich der Bankgebuhren).
Fur jede erfolgreiche Abhebung berechnet die Bank `0,50 $`.
Berechnen Sie das Guthaben auf James' Konto nach einem versuchten Handel.
Die Eingaben sind in folgender Reihenfolge:
1. Der Betrag, den James abheben mochte, liegt im folgenden Bereich: `0 < N <= 2000`.
2. James' Anfangsguthaben wird mit zwei Dezimalstellen angegeben und liegt im folgenden Bereich: `0 < B <= 2000`.

# --instructions--

Geben Sie das Kontoguthaben nach dem versuchten Handel zuruck, angegeben als eine Zahl mit zwei Dezimalstellen.
Wenn nicht genug Geld auf dem Konto vorhanden ist, um die Transaktion abzuschlieen, geben Sie das aktuelle Bankguthaben zuruck.

Beispiel fur einen Funktionsaufruf:
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

Fuhren Sie eine erfolgreiche Transaktion durch

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Unzureichende Mittel

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Abgelehnte Transaktion, ungultiger Betrag

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Heben Sie erfolgreich das gesamte Geld ab

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
