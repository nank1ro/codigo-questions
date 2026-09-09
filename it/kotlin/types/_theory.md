Ogni valore in Kotlin ha un **tipo**, che dice al compilatore che tipo di dato è e cosa puoi farci.
I tipi di base sono:
- `Int`: un numero intero, come `42` o `-7`
- `Long`: un numero intero che può essere molto più grande di un `Int`
- `Double`: un numero con una parte decimale, come `3.14`
- `Float`: un numero decimale che usa metà della memoria di un `Double`, ma è meno preciso
- `Char`: un singolo carattere tra apici singoli, come `'a'`
- `Boolean`: oppure `true` oppure `false`
- `String`: un pezzo di testo tra virgolette doppie, come `"Hello"`

Come hai visto nelle lezioni sulle variabili, puoi indicare il tipo esplicitamente con due punti dopo il nome:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
Un valore di un tipo non può essere memorizzato in una variabile di un altro tipo: `val age: Int = "36"` è un errore di compilazione.

---

Il più delle volte non scrivi il tipo: Kotlin lo **deduce** dal valore che assegni, seguendo alcune regole sui letterali:
- un numero intero, come `42`, è un `Int`
- un numero con un punto decimale, come `3.14`, è un `Double`
- il testo tra virgolette doppie è una `String`
- un carattere tra apici singoli è un `Char`
- `true` e `false` sono `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Per controllare cosa ha dedotto Kotlin puoi stampare il nome del tipo di qualsiasi valore con `::class.simpleName`:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
Un letterale decimale non viene mai dedotto come `Float`: `val ratio = 0.5` è un `Double`.

---

Un `Int` può contenere numeri interi fino a circa due miliardi, più precisamente fino a `Int.MAX_VALUE`, che è `2147483647`.
Un letterale intero troppo grande per un `Int` viene automaticamente dedotto come un `Long`, e puoi forzare un `Long` per qualsiasi letterale con il suffisso `L`:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
Allo stesso modo il suffisso `f` trasforma un letterale decimale in un `Float`: `val ratio = 0.5f`.
I numeri lunghi sono difficili da leggere, quindi Kotlin ti permette di inserire underscore `_` in qualsiasi punto tra le cifre; vengono ignorati dal compilatore:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin non converte mai da solo tra tipi numerici quando assegni un valore, nemmeno da un tipo più piccolo a uno più grande: memorizzare un `Int` in una variabile `Long` o `Double` è un errore di compilazione.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Ogni tipo numerico ha **funzioni di conversione** che creano un nuovo valore del tipo di cui hai bisogno: `toInt()`, `toLong()`, `toDouble()`, `toFloat()` e, per ottenere testo, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Passare da un decimale a un numero intero **tronca**: `toInt()` semplicemente scarta la parte decimale, quindi `3.99.toInt()` è `3` e `(-3.99).toInt()` è `-3`.

---

I tipi degli operandi decidono come funziona la divisione. Quando entrambi sono `Int`, l'operatore `/` esegue la **divisione tra interi**: il risultato è un `Int` e il resto viene scartato.
Quando almeno un operando è un `Double`, `/` esegue la divisione in virgola mobile e mantiene la parte decimale:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
Quindi per ottenere un risultato decimale da due variabili `Int` devi convertire almeno una di esse **prima** di dividere: `(7 / 2).toDouble()` è `3.0`, perché la divisione tra interi è già avvenuta.

---

Quando una funzione deve restituire un risultato decimale calcolato da numeri interi, converti gli operandi in `Double` prima di dividere e dichiara il tipo di ritorno come `Double`:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Ricorda che `sum()` e `size` di una `List<Int>` sono anch'essi valori `Int`, quindi hanno bisogno della stessa conversione.

---

Ogni `Char` è memorizzato come un numero, il suo **codice**. La proprietà `code` dà l'`Int` nascosto dietro a un carattere, e `toChar()` fa il contrario, trasformando un `Int` nel `Char` con quel codice:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
Le lettere hanno codici consecutivi, quindi aggiungere al codice fa avanzare lungo l'alfabeto.
Nota che il codice di `'7'` è `55`, non `7`: per leggere la cifra che un `Char` rappresenta usa `digitToInt()`, che restituisce `7`.

---

Dato che il codice di un `Char` è un `Int`, puoi fare aritmetica su di esso e riconvertire il risultato in un `Char`. È così che ti muovi lungo l'alfabeto:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin ti permette anche di aggiungere un `Int` direttamente a un `Char`: `'a' + 1` è `'b'`, e la differenza tra due caratteri `'d' - 'a'` è l'`Int` `3`.

---

Il testo digitato da un utente arriva sempre come `String`, anche quando sembra un numero. Per fare calcoli con esso devi **farne il parsing**: `toInt()` trasforma `"42"` nell'`Int` `42`, e `toDouble()` trasforma `"3.5"` nel `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
Non tutto il testo è un numero: `"4x2".toInt()` lancia una `NumberFormatException` e ferma il programma.
Le alternative sicure `toIntOrNull()` e `toDoubleOrNull()` restituiscono `null` invece di lanciare un'eccezione, quindi, come hai imparato nelle lezioni sulla nullabilità, puoi fornire un valore predefinito con `?:`:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` riesce solo quando tutto il testo è un numero intero valido, con un segno opzionale:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
Per il testo decimale usa `toDoubleOrNull()`, che accetta `"3.5"` e restituisce un `Double?` allo stesso modo.

---

Un `Int` ha una dimensione fissa, quindi ha un valore minimo e uno massimo: `Int.MIN_VALUE` è `-2147483648` e `Int.MAX_VALUE` è `2147483647`.
Superare il limite **non** solleva un errore: il valore silenziosamente **riparte dall'altra estremità** dell'intervallo, un comportamento chiamato overflow.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
Quando un risultato può superare i due miliardi, usa un `Long`, il cui limite `Long.MAX_VALUE` è circa nove quintilioni. Ricorda di convertire prima dell'operazione: `Int.MAX_VALUE.toLong() + 1` è `2147483648`.

---

Un `Double` memorizza i decimali in binario, quindi alcuni valori non possono essere rappresentati esattamente e piccoli errori compaiono nelle ultime cifre:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
Per mostrare un numero fisso di decimali, usa `String.format` con una stringa di formato: `"%.2f"` significa "un numero decimale con 2 cifre dopo il punto". Il risultato è una `String`, arrotondata a quel numero di cifre:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` è il tipo al vertice della gerarchia: ogni valore Kotlin è un `Any`, quindi una variabile di tipo `Any` può contenere un `Int`, una `String`, un `Boolean`, o qualsiasi altra cosa.
Per scoprire cosa contiene davvero usi l'operatore `is`, che restituisce `true` quando il valore ha quel tipo:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Una volta superato un controllo, il compilatore esegue uno **smart cast** del valore: dentro l'`if` (o il ramo del `when`) puoi usarlo come quel tipo, senza bisogno di conversioni:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
