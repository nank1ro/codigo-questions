---
language: kotlin
exerciseType: 1
difficulty: 1
title: Gocce di pioggia
---

# --description--

Il tuo compito e' quello di convertiire un numero in una stringa che contiene suoni di gocce di pioggia corrispondenti a determinati fattori potenziali.
Un fattore e' un numero che si divide uniformemente in un altro numero, senza lasciare alcun resto.
Il modo piu' semplice per verificare se un numero e' un fattore di un altro e' utilizzare l'operazione modulo.
Le regole delle gocce di pioggia sono che se un dato numero:

- ha 3 come fattore, aggiungi 'Pling' al risultato.
- ha 5 come fattore, aggiungi 'Plang' al risultato.
- ha 7 come fattore, aggiungi 'Plong' al risultato.
- non ha 3, 5 o 7 come fattore, il risultato dovrebbe essere costituito dalle cifre del numero.

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

- 28 ha 7 come fattore, ma non 3 o 5, quindi il risultato e' `"Plong"`.
- 30 ha sia 3 che 5 come fattori, ma non 7, quindi il risultato e' `"PlingPlang"`.
- 34 non e' fattorizzato da 3, 5, o 7, quindi il risultato e' `"34"`.

Esempio di chiamata:
```kotlin
println(converti(28))
// stampa "Plong"
```

# --seed--

```kotlin
fun converti(): String {
    
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

Il suono per 1 è "1"

```kotlin
    tryCatch(converti(1) == "1")
```

Il suono per 3 è "Pling"

```kotlin
    tryCatch(converti(3) == "Pling")
```

Il suono per 5 è "Plang"

```kotlin
    tryCatch(converti(5) == "Plang")
```

Il suono per 7 è "Plong"

```kotlin
    tryCatch(converti(7) == "Plong")
```

Il suono per 6 è "Pling"

```kotlin
    tryCatch(converti(6) == "Pling")
```

Il suono per 8 è "8"

```kotlin
    tryCatch(converti(8) == "8")
```

Il suono per 9 è "Pling"

```kotlin
    tryCatch(converti(9) == "Pling")
```

Il suono per 10 è "Plang"

```kotlin
    tryCatch(converti(10) == "Plang")
```

Il suono per 14 è "Plong"

```kotlin
    tryCatch(converti(14) == "Plong")
```

Il suono per 15 è "PlingPlang"

```kotlin
    tryCatch(converti(15) == "PlingPlang")
```

Il suono per 21 è "PlingPlong"

```kotlin
    tryCatch(converti(21) == "PlingPlong")
```

Il suono per 25 è "Plang"

```kotlin
    tryCatch(converti(25) == "Plang")
```

Il suono per 27 è "Pling"

```kotlin
    tryCatch(converti(27) == "Pling")
```

Il suono per 35 è "PlangPlong"

```kotlin
    tryCatch(converti(35) == "PlangPlong")
```

Il suono per 49 è "Plong"

```kotlin
    tryCatch(converti(49) == "Plong")
```

Il suono per 52 è "52"

```kotlin
    tryCatch(converti(52) == "52")
```

Il suono per 105 è "PlingPlangPlong"

```kotlin
    tryCatch(converti(105) == "PlingPlangPlong")
```

Il suono per 3125 è "Plang"

```kotlin
    tryCatch(converti(3125) == "Plang")
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
fun converti(num: Int): String {
    var result = ""
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
