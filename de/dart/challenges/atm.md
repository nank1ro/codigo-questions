---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James möchte N Dollar von einem Geldautomaten abheben.
Der Geldautomat akzeptiert die Transaktion nur, wenn N ein Vielfaches von 5 ist und James' Konto genug Geld für die Abhebung hat (einschließlich Bankgebühren).
Für jede erfolgreiche Abhebung berechnet die Bank 0,50 Dollar.
Berechnen Sie James' Kontostand nach einer versuchten Transaktion.
Die Eingaben sind in dieser Reihenfolge:
1. Der Betrag, den James abheben möchte, liegt im folgenden Bereich: `0 < N <= 2000`.
2. James' Anfangssaldo wird mit zwei Dezimalstellen angegeben und liegt im folgenden Bereich: `0 < B <= 2000`.

# --instructions--

Geben Sie den Kontostand nach der versuchten Transaktion zurück, als Zahl mit zwei Dezimalstellen.
Wenn nicht genug Geld auf dem Konto ist, um die Transaktion abzuschließen, geben Sie den aktuellen Kontostand zurück.

Beispiel eines Funktionsaufrufs:
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

Erfolgreiche Transaktion durchführen

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Unzureichende Deckung

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Transaktion abgelehnt, ungültiger Betrag

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Erfolgreich das ganze Geld abheben

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
