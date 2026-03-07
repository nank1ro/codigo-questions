---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James chce wypłacić N dolarów z bankomatu.
Maszyna zaakceptuje transakcję tylko wtedy, gdy N jest wielokrotnością 5, a saldo konta Jamesa jest wystarczające do przeprowadzenia transakcji (łącznie z opłatą bankową).
Za każdą udaną wypłatę bank pobiera `0.50$`.
Oblicz saldo konta Jamesa po próbie transakcji.
Dane wejściowe są w następującej kolejności:
1. kwota, którą James chce wypłacić, jest w zakresie: `0 < N <= 2000`.
2. początkowe saldo Jamesa podane jest z dokładnością do dwóch miejsc po przecinku i jest w zakresie: `0 < B <= 2000`.

# --instructions--

Zwróć saldo konta po próbie transakcji jako liczbę z dokładnością do dwóch miejsc po przecinku.
Jeśli na koncie nie ma wystarczających środków do przeprowadzenia transakcji, zwróć aktualne saldo.

Przykład wywołania funkcji:
```kotlin
println(accountBalance(10, 20.00))
// prints 9.5
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

Przeprowadź udaną transakcję

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

Niewystarczające środki

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

Odrzucona transakcja, nieprawidłowa kwota

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

Wypłać wszystkie środki

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
