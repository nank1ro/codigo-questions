---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James chciałby wypłacić N dolarów z bankomatu.
Automat zaakceptuje transakcję tylko wtedy, gdy N jest wielokrotnością 5, a konto Jamesa ma wystarczające środki na przeprowadzenie transakcji wypłaty (wraz z opłatami bankowymi).
Za każdą pomyślną wypłatę bank pobiera `0.50$`.
Oblicz stan konta Jamesa po próbie transakcji.
Dane wejściowe podane są w następującej kolejności:
1. kwota, którą James chce wypłacić, mieści się w zakresie: `0 < N <= 2000`.
2. początkowe saldo Jamesa podane jest z dokładnością do dwóch cyfr i mieści się w zakresie: `0 < B <= 2000`.

# --instructions--

Zwróć stan konta po próbie transakcji, podany jako liczba z dokładnością do dwóch miejsc po przecinku.
Jeśli na koncie nie ma wystarczających środków do realizacji transakcji, zwróć bieżące saldo bankowe.

> WSKAZÓWKA: pomiń etykiety argumentów używając `_` (podkreślnika)

Przykład wywołania funkcji:
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

Wykonaj pomyślną transakcję

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Niewystarczające środki

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Transakcja odrzucona, nieprawidłowa kwota

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Wypłać wszystkie środki pomyślnie

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
