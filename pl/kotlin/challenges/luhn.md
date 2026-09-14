---
language: kotlin
exerciseType: 1
difficulty: 2
title: Suma kontrolna Luhna
---

# --description--

Algorytm Luhna to prosta suma kontrolna służąca do sprawdzania poprawności numerów identyfikacyjnych, takich jak numery kart kredytowych.

Przed sprawdzeniem numeru usuń wszystkie spacje z ciągu znaków. Ciąg znaków jest poprawny tylko wtedy, gdy to, co zostało, jest dłuższe niż jeden znak, a oryginalny ciąg znaków zawiera wyłącznie cyfry i spacje.

Aby wykonać sprawdzenie, zacznij od skrajnie prawej cyfry i przesuwaj się w lewo, podwajając co drugą cyfrę. Gdy podwojenie da liczbę większą niż 9, odejmij od niej 9. Następnie zsumuj wszystkie cyfry: numer jest poprawny tylko wtedy, gdy suma jest podzielna przez 10.

Na przykład `"059"` daje `0`, potem podwojone `5` to `10`, które staje się `1`, a następnie `9`. Ich suma wynosi `10`, czyli liczbę podzielną przez 10, więc numer jest poprawny.

# --instructions--

Napisz funkcję `isValid`, która przyjmuje ciąg znaków i zwraca `true`, gdy numer jest poprawny, a `false` w przeciwnym razie.

- `"4539 3195 0343 6467"` przechodzi sumę kontrolną, więc wynik to `true`.
- `"8273 1232 7352 0569"` nie przechodzi sumy kontrolnej, więc wynik to `false`.
- `"0"` ma długość tylko jednego znaku, więc wynik to `false`.
- `"055-444-285"` zawiera znak, który nie jest cyfrą ani spacją, więc wynik to `false`.

Przykład wywołania funkcji:
```kotlin
println(isValid("095 245 88"))
// prints true
```

# --seed--

```kotlin
fun isValid(value: String): Boolean {
    
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

Pojedyncza cyfra nie jest poprawna.

```kotlin
    tryCatch(isValid("0") == false)
```

Pojedyncza cyfra ze spacją na początku nie jest poprawna.

```kotlin
    tryCatch(isValid(" 0") == false)
```

Numer `"059"` jest poprawny.

```kotlin
    tryCatch(isValid("059") == true)
```

Numer `"59"` jest poprawny.

```kotlin
    tryCatch(isValid("59") == true)
```

Numer `"055 444 285"` jest poprawny.

```kotlin
    tryCatch(isValid("055 444 285") == true)
```

Numer `"055 444 286"` nie jest poprawny.

```kotlin
    tryCatch(isValid("055 444 286") == false)
```

Numer `"8273 1232 7352 0569"` nie jest poprawny.

```kotlin
    tryCatch(isValid("8273 1232 7352 0569") == false)
```

Numer `"4539 3195 0343 6467"` jest poprawny.

```kotlin
    tryCatch(isValid("4539 3195 0343 6467") == true)
```

Numer `"1 2345 6789 1234 5678 9012"` nie jest poprawny.

```kotlin
    tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

Numer `"095 245 88"` jest poprawny.

```kotlin
    tryCatch(isValid("095 245 88") == true)
```

Litera powoduje, że numer jest niepoprawny.

```kotlin
    tryCatch(isValid("055a 444 285") == false)
```

Myślniki powodują, że numer jest niepoprawny.

```kotlin
    tryCatch(isValid("055-444-285") == false)
```

Znak interpunkcyjny powoduje, że numer jest niepoprawny.

```kotlin
    tryCatch(isValid(":9") == false)
```

Symbole powodują, że numer jest niepoprawny.

```kotlin
    tryCatch(isValid("055# 444\$ 285") == false)
```

Pusty ciąg znaków nie jest poprawny.

```kotlin
    tryCatch(isValid("") == false)
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
fun isValid(value: String): Boolean {
    var sum = 0
    var count = 0
    for (i in value.length - 1 downTo 0) {
        val character = value[i]
        if (character == ' ') {
            continue
        }
        if (character < '0' || character > '9') {
            return false
        }
        var digit = character - '0'
        if (count % 2 == 1) {
            digit *= 2
            if (digit > 9) {
                digit -= 9
            }
        }
        sum += digit
        count++
    }
    return count > 1 && sum % 10 == 0
}
```
