---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James möchte N Dollar von einem Geldautomaten abheben.
Der Geldautomat akzeptiert die Transaktion nur, wenn N ein Vielfaches von 5 ist und James' Konto genug Geld hat, um die Abhebung (einschließlich Bankgebühren) durchzuführen.
Für jede erfolgreiche Abhebung berechnet die Bank `0,50$`.
Berechnen Sie James' Kontostand nach einem Abhebungsversuch.
Die Eingaben sind in der folgenden Reihenfolge:
1. der Geldbetrag, den James abheben möchte, liegt in folgendem Bereich: `0 < N <= 2000`.
2. James' anfänglicher Kontostand wird mit zwei Dezimalstellen angegeben und liegt im Bereich: `0 < B <= 2000`.

# --instructions--

Geben Sie den Kontostand nach dem versuchten Geschäft zurück, ausgedrückt als Zahl mit zwei Dezimalstellen.
Wenn nicht genug Geld auf dem Konto ist, um die Transaktion abzuschließen, geben Sie den aktuellen Bankguthaben zurück.

> HINWEIS: Lassen Sie die Argumentbezeichnungen mit dem `_` (Unterstrich) weg

Beispiel für einen Funktionsaufruf:
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

Führen Sie eine erfolgreiche Transaktion durch

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Unzureichende Deckung

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Transaktion abgelehnt, ungültiger Betrag

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Heben Sie das ganze Geld erfolgreich ab

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
