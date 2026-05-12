---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

Джеймс хотел бы снять N долларов из ATM.
Банкомат примет транзакцию только в том случае, если N кратно 5, и на счету Джеймса достаточно средств для выполнения операции снятия (включая банковскую комиссию).
За каждое успешное снятие банк взимает комиссию `0.50$`.
Рассчитайте баланс счёта Джеймса после попытки транзакции.
Входные данные указаны в следующем порядке:
1. сумма наличных, которую Джеймс хочет снять, находится в диапазоне: `0 < N <= 2000`.
2. начальный баланс Джеймса задан с точностью до двух знаков после запятой и находится в диапазоне: `0 < B <= 2000`.

# --instructions--

Верните баланс счёта после попытки транзакции в виде числа с точностью до двух знаков после запятой.
Если на счёте недостаточно средств для выполнения транзакции, верните текущий баланс.

> ПОДСКАЗКА: опустите метки аргументов с помощью `_` (нижнее подчёркивание)

Пример вызова функции:
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

Выполнение успешной транзакции

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Недостаточно средств

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Отклонённая транзакция, недопустимая сумма

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Успешное снятие всех средств

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
