---
language: kotlin
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Twoim zadaniem jest zamiana liczby na ciąg znaków zawierający dźwięki kropel deszczu odpowiadające określonym potencjalnym czynnikom.
Czynnik to liczba, która dzieli inną liczbę bez reszty.
Najprostszym sposobem sprawdzenia, czy liczba jest czynnikiem innej, jest użycie operacji modulo.
Zasady gry Raindrops są następujące — jeśli dana liczba:

- ma 3 jako czynnik, dodaj 'Pling' do wyniku.
- ma 5 jako czynnik, dodaj 'Plang' do wyniku.
- ma 7 jako czynnik, dodaj 'Plong' do wyniku.
- nie ma żadnego z czynników 3, 5 ani 7, wynikiem powinny być cyfry tej liczby.

# --instructions--

Napisz funkcję, która zwraca odpowiedni ciąg znaków, przykłady:

- 28 ma 7 jako czynnik, ale nie 3 ani 5, więc wynikiem będzie `"Plong"`.
- 30 ma zarówno 3, jak i 5 jako czynniki, ale nie 7, więc wynikiem będzie `"PlingPlang"`.
- 34 nie ma czynnika 3, 5 ani 7, więc wynikiem będzie `"34"`.

Przykład wywołania funkcji:
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

Dźwięk dla 1 to "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

Dźwięk dla 3 to "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

Dźwięk dla 5 to "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

Dźwięk dla 7 to "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

Dźwięk dla 6 to "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

Dźwięk dla 8 to "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

Dźwięk dla 9 to "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

Dźwięk dla 10 to "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

Dźwięk dla 14 to "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

Dźwięk dla 15 to "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

Dźwięk dla 21 to "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

Dźwięk dla 25 to "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

Dźwięk dla 27 to "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

Dźwięk dla 35 to "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

Dźwięk dla 49 to "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

Dźwięk dla 52 to "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

Dźwięk dla 105 to "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

Dźwięk dla 3125 to "Plang"

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
