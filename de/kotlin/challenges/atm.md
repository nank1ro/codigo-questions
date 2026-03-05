---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James möchte N Dollar von einem Geldautomaten abheben.
Der Geldautomat akzeptiert die Transaktion nur, wenn N ein Vielfaches von 5 ist und James' Konto genug Geld für die Abhebung hat (einschließlich Bankgebühren).
Für jede erfolgreiche Abhebung berechnet die Bank `0,50 $`.
Berechnen Sie James' Kontostand nach einer versuchten Transaktion.
Die Eingaben sind in der folgenden Reihenfolge:
1. Der Betrag, den James abheben möchte, liegt in folgendem Bereich: `0 < N <= 2000`.
2. James' ursprünglicher Kontostand wird mit zwei Dezimalstellen angegeben und liegt in folgendem Bereich: `0 < B <= 2000`.

# --instructions--

Geben Sie den Kontostand nach der versuchten Transaktion mit zwei Dezimalstellen zurück.
Wenn nicht genug Geld auf dem Konto vorhanden ist, um die Transaktion abzuschließen, geben Sie den aktuellen Kontostand zurück.

Beispiel für einen Funktionsaufruf:
```kotlin
println(accountBalance(10, 20.00))
// gibt 9.5 aus
```

# --seed--

```kotlin
fun accountBalance(): Double {
    return
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Erfolgreiche Transaktion durchführen

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

Unzureichende Deckung

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

Transaktion abgelehnt, ungültiger Betrag

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

Erfolgreich das ganze Geld abheben

```kotlin
    tryCatch(accountBalance(95, 95.50) == 0.00)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun accountBalance(withdraw: Int, balance: Double): Double {
    val isMultipleOf5 = withdraw.rem(5) == 0;
    val isAmountAvailable = balance >= (withdraw + 0.50)
    if (isMultipleOf5 && isAmountAvailable) {
        return balance - withdraw - 0.50
    }
    return balance
}
```
