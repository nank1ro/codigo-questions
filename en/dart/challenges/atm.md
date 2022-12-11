---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James would like to withdraw N dollars from an ATM.
The cash machine will only accept the transaction if N is a multiple of 5, and James' account has enough cash to perform the withdrawal transaction (including bank charges).
For each successful withdrawal the bank charges `0.50$`.
Calculate James' account balance after an attempted transaction.
The inputs are in the following order:
1. the amount of cash which James wishes to withdraw is in the following range: `0 < N <= 2000`.
2. James' initial balance is gived with two digits of precision and is in the following range: `0 < B <= 2000`.

# --instructions--

Return the account balance after the attempted transaction, given as a number with two digits of precision.
If there is not enough money in the account to complete the transaction, return the current bank balance.

Example of function call:
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

Perform a successful transaction

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Insufficient funds

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Refused transaction, invalid amount

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Withdraw all money successfully

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
