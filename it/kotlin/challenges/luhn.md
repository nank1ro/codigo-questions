---
language: kotlin
exerciseType: 1
difficulty: 2
title: Checksum di Luhn
---

# --description--

L'algoritmo di Luhn è un semplice checksum usato per validare numeri identificativi, come i numeri delle carte di credito.

Prima di controllare un numero, rimuovi ogni spazio dalla stringa. La stringa è valida solo se ciò che resta è più lungo di un carattere e la stringa originale non contiene altro che cifre e spazi.

Per eseguire il controllo, parti dalla cifra più a destra e procedi verso sinistra, raddoppiando una cifra su due. Quando il raddoppio produce un numero maggiore di 9, sottrai 9. Poi somma tutte le cifre: il numero è valido solo se la somma è divisibile per 10.

Ad esempio, `"059"` dà `0`, poi `5` raddoppiato è `10` che diventa `1`, poi `9`. La loro somma è `10`, che è divisibile per 10, quindi il numero è valido.

# --instructions--

Scrivi una funzione `isValid` che riceve una stringa e restituisce `true` quando il numero è valido, `false` altrimenti.

- `"4539 3195 0343 6467"` passa il checksum, quindi il risultato è `true`.
- `"8273 1232 7352 0569"` non passa il checksum, quindi il risultato è `false`.
- `"0"` è lungo solo un carattere, quindi il risultato è `false`.
- `"055-444-285"` contiene un carattere che non è una cifra né uno spazio, quindi il risultato è `false`.

Esempio di chiamata di funzione:
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

Una singola cifra non è valida.

```kotlin
    tryCatch(isValid("0") == false)
```

Una singola cifra preceduta da uno spazio non è valida.

```kotlin
    tryCatch(isValid(" 0") == false)
```

Il numero `"059"` è valido.

```kotlin
    tryCatch(isValid("059") == true)
```

Il numero `"59"` è valido.

```kotlin
    tryCatch(isValid("59") == true)
```

Il numero `"055 444 285"` è valido.

```kotlin
    tryCatch(isValid("055 444 285") == true)
```

Il numero `"055 444 286"` non è valido.

```kotlin
    tryCatch(isValid("055 444 286") == false)
```

Il numero `"8273 1232 7352 0569"` non è valido.

```kotlin
    tryCatch(isValid("8273 1232 7352 0569") == false)
```

Il numero `"4539 3195 0343 6467"` è valido.

```kotlin
    tryCatch(isValid("4539 3195 0343 6467") == true)
```

Il numero `"1 2345 6789 1234 5678 9012"` non è valido.

```kotlin
    tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

Il numero `"095 245 88"` è valido.

```kotlin
    tryCatch(isValid("095 245 88") == true)
```

Una lettera rende il numero non valido.

```kotlin
    tryCatch(isValid("055a 444 285") == false)
```

I trattini rendono il numero non valido.

```kotlin
    tryCatch(isValid("055-444-285") == false)
```

Un carattere di punteggiatura rende il numero non valido.

```kotlin
    tryCatch(isValid(":9") == false)
```

I simboli rendono il numero non valido.

```kotlin
    tryCatch(isValid("055# 444\$ 285") == false)
```

Una stringa vuota non è valida.

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
