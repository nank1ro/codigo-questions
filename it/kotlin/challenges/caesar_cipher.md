---
language: kotlin
exerciseType: 1
difficulty: 2
title: Cifrario di Cesare
---

# --description--

Giulio Cesare proteggeva le sue lettere private con uno dei trucchi più antichi della crittografia: sostituiva ogni lettera di un messaggio con la lettera che si trova un numero fisso di posizioni più avanti nell'alfabeto. Con uno spostamento di 3, `a` diventa `d`, `b` diventa `e` e `c` diventa `f`.

L'alfabeto si comporta come un cerchio, quindi le lettere della fine tornano all'inizio: con uno spostamento di 3, `x` diventa `a`, `y` diventa `b` e `z` diventa `c`.

Tutto ciò che non è una lettera, come uno spazio, una virgola, un punto esclamativo o una cifra, attraversa il cifrario senza subire modifiche.

# --instructions--

Scrivi una funzione `caesarCipher` che riceve un messaggio `text` e un numero intero `shift`, e restituisce il messaggio codificato.

Esempi:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Il messaggio è sempre in minuscolo, quindi non dovrai mai occuparti delle lettere maiuscole.
- I caratteri che non sono lettere mantengono la loro posizione e il loro valore.
- Lo spostamento non è mai negativo. Uno spostamento di `0` lascia il messaggio invariato, e così anche uno spostamento di `26`.

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

Uno spostamento di 3 trasforma "hello" in "khoor"

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

La fine dell'alfabeto ricomincia da capo, quindi "xyz" diventa "abc"

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

Uno spostamento di 0 lascia il messaggio invariato

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

Uno spostamento di 26 è un giro completo dell'alfabeto, quindi il messaggio resta invariato

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

Punteggiatura e spazi passano invariati

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Un messaggio vuoto resta vuoto

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

Gli spazi tra singole lettere vengono preservati

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Le cifre non vengono spostate, nemmeno con uno spostamento di 25

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Uno spostamento di 13 codifica una frase intera

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
