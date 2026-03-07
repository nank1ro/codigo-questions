---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James chce wypłacić N dolarów z bankomatu.
Bankomat zaakceptuje transakcję tylko wtedy, gdy N jest wielokrotnością 5, a na koncie Jamesa jest wystarczająco dużo środków na przeprowadzenie transakcji wypłaty (łącznie z opłatami bankowymi).
Za każdą udaną wypłatę bank pobiera `0.50$`.
Oblicz saldo konta Jamesa po próbie transakcji.
Dane wejściowe są w następującej kolejności:
1. kwota gotówki, którą James chce wypłacić, mieści się w zakresie: `0 < N <= 2000`.
2. początkowe saldo Jamesa jest podane z dokładnością do dwóch miejsc po przecinku i mieści się w zakresie: `0 < B <= 2000`.

# --instructions--

Zwróć saldo konta po próbie transakcji, podane jako liczba z dokładnością do dwóch miejsc po przecinku.
Jeśli na koncie nie ma wystarczającej ilości pieniędzy, aby zakończyć transakcję, zwróć bieżące saldo konta.

Przykład wywołania funkcji:
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

Wykonaj udaną transakcję

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Niewystarczające środki

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Odrzucona transakcja, nieprawidłowa kwota

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Wypłata wszystkich środków zakończona sukcesem

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
