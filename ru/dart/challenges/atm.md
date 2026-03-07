---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

Джеймс хочет снять N долларов из ATM.
Банкомат примет транзакцию только в том случае, если N кратно 5, и на счету Джеймса достаточно средств для выполнения операции снятия (включая банковскую комиссию).
За каждое успешное снятие банк взимает `0.50$`.
Рассчитайте баланс счёта Джеймса после попытки транзакции.
Входные данные указаны в следующем порядке:
1. сумма наличных, которую Джеймс хочет снять, находится в следующем диапазоне: `0 < N <= 2000`.
2. начальный баланс Джеймса задаётся с двумя знаками после запятой и находится в следующем диапазоне: `0 < B <= 2000`.

# --instructions--

Верните баланс счёта после попытки транзакции, заданный как число с двумя знаками после запятой.
Если на счёте недостаточно средств для завершения транзакции, верните текущий баланс.

Пример вызова функции:
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

Выполнить успешную транзакцию

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Недостаточно средств

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Отклонённая транзакция, недопустимая сумма

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Успешное снятие всех средств

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
