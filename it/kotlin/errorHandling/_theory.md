Un'**eccezione** è il modo in cui Kotlin segnala che un'istruzione non può essere eseguita. Trasformare `"abc"` in un numero, dividere un intero per zero o leggere oltre la fine di una lista generano tutti un'eccezione.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Questo programma stampa `before` e poi si ferma. `toInt()` non riesce a leggere `"abc"`, quindi **lancia** una `NumberFormatException`; nessuna parte del programma se ne occupa, quindi Kotlin termina il programma con un report di errore e `after` non viene mai stampato.

Puoi anche lanciare un'eccezione tu stesso con la parola chiave `throw`:
```kotlin
throw Exception("something went wrong")
```

Un'eccezione che nessuno gestisce non è un avviso: è la fine dell'esecuzione.

---

Per mantenere il programma in vita, metti l'istruzione rischiosa dentro un blocco `try` e descrivi il recupero in un blocco `catch`:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin esegue il blocco `try`; non appena un'istruzione al suo interno lancia un'eccezione, il resto del blocco viene saltato e il controllo passa al blocco `catch`. Il nome tra parentesi tonde — qui `e` — è l'oggetto eccezione, e `Exception` è il tipo che viene catturato.

Una volta che il blocco `catch` è terminato, il programma continua normalmente con la riga dopo l'intero `try`/`catch`.

---

Catturare `Exception` cattura tutto, che è raramente quello che vuoi: un errore di battitura in un altro punto del blocco verrebbe inghiottito anch'esso. Indica invece il **tipo esatto** da cui sai come recuperare.

Ogni errore ha il suo tipo. `"abc".toInt()` lancia una `NumberFormatException`, quindi quello è il tipo da catturare:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Se dentro il blocco viene lanciato un tipo diverso di eccezione, questo `catch` non corrisponde e l'eccezione continua a propagarsi fuori dalla funzione.

---

Un solo `try` può essere seguito da più blocchi `catch`, ognuno dei quali gestisce un tipo diverso:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin prova i blocchi **dall'alto verso il basso** ed esegue il primo il cui tipo corrisponde. Uno solo dei blocchi viene mai eseguito.

L'ordine conta quindi. `NumberFormatException` e `IndexOutOfBoundsException` sono entrambi tipi di `Exception`, quindi un `catch (e: Exception)` scritto per primo corrisponderebbe a ogni errore e i blocchi sottostanti non verrebbero mai eseguiti. Scrivi prima il tipo più specifico e per ultimo quello più generale.

---

Un blocco `finally` può essere aggiunto alla fine. Viene eseguito **qualunque cosa accada**: dopo un `try` riuscito, dopo che un `catch` ha recuperato, e persino quando l'eccezione non viene affatto catturata.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
Questo lo rende il posto giusto per le operazioni di pulizia che non devono essere saltate, come chiudere un file. Un `try` ha bisogno almeno di un `catch` o di un `finally`, ma può avere entrambi.

---

In Kotlin `try` non è solo un'istruzione: è un'**espressione** che produce un valore. Il valore è l'ultima espressione del blocco che è stato eseguito — il blocco `try` quando nulla è fallito, il blocco `catch` quando è fallito.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
Questa è la forma idiomatica in Kotlin. Invece di dichiarare una `var`, assegnarla in due punti e sperare che ogni percorso la imposti, ottieni un'unica `val` che contiene sempre un valore utilizzabile.

Nota che un blocco `finally` non cambia mai il valore: viene eseguito solo per i suoi effetti collaterali.

---

Poiché `try` è un'espressione, può essere usato ovunque ci si aspetti un valore — anche come intero corpo di una funzione scritta con `=`:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Entrambi i blocchi devono produrre un valore dello stesso tipo, qui `Int`. Scrivi il valore di riserva come ultima espressione del blocco `catch`; non c'è nessun `return` dentro nessuno dei due blocchi.

---

Lanciare e catturare non è gratis, e per le conversioni più comuni Kotlin offre una variante più economica che semplicemente restituisce `null` invece di lanciare: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
Combinato con l'operatore Elvis `?:`, che fornisce un sostituto quando il valore alla sua sinistra è `null`, l'intero `try`/`catch` si riduce a una riga:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Usa `try`/`catch` quando l'errore è genuinamente eccezionale; usa `toIntOrNull()` quando un input sbagliato è previsto.

---

Le tue funzioni possono rifiutare un input sbagliato allo stesso modo in cui lo fa la libreria standard, con `throw`. La libreria fornisce già un tipo per il caso più comune: `IllegalArgumentException` significa "il valore che mi hai passato non è accettabile".

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` termina immediatamente la funzione — il `return` sotto non viene mai raggiunto. È il chiamante a decidere cosa farne:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Lanciare è meglio che restituire silenziosamente un valore inventato: una risposta sbagliata viaggia lontano, un'eccezione si ferma al primo chiamante pronto a gestirla.

---

Ogni eccezione porta con sé il testo con cui è stata creata. Dentro un blocco `catch` la leggi attraverso la proprietà `message` dell'oggetto eccezione:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` è nullable, perché un'eccezione può essere creata senza alcun testo; `e.message ?: "unknown"` fornisce un sostituto sicuro quando ti serve una semplice `String`.

Preferisci stampare `e.message` piuttosto che l'oggetto eccezione stesso: il testo dell'oggetto include anche il nome della classe, che è rumore per chi legge l'output.

---

Scrivere `if (...) throw IllegalArgumentException(...)` su ogni argomento diventa rumoroso, quindi Kotlin offre due scorciatoie che si leggono come frasi:

```kotlin
require(n >= 0) { "n must not be negative" }   // lancia IllegalArgumentException
check(started) { "not started" }               // lancia IllegalStateException
```
Entrambe prendono una condizione e un blocco che produce il messaggio, ed entrambe lanciano **quando la condizione è falsa**. L'unica differenza è il tipo di eccezione, e quella differenza è un messaggio per chi legge:

* `require` protegge gli **argomenti** passati dal chiamante, e fallisce con `IllegalArgumentException`.
* `check` protegge lo **stato** dell'oggetto o del programma, e fallisce con `IllegalStateException`.

Il blocco viene valutato solo quando il controllo fallisce, quindi costruire il messaggio non costa nulla nel percorso felice.

---

Quando nessuno dei tipi incorporati descrive bene il tuo errore, dichiarane uno tuo. Un'eccezione è una classe ordinaria che estende `Exception` e passa il suo testo al genitore:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
Quella singola riga è un tipo di eccezione completo. Viene lanciata e catturata come qualsiasi altra, e `e.message` restituisce il testo con cui è stata costruita:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
Il vantaggio è la precisione: un chiamante può catturare solo `InsufficientFundsException` e lasciare che ogni altro errore continui la sua corsa.

---

`runCatching` esegue un blocco e non lascia mai fuggire un'eccezione. Restituisce invece un `Result`, un oggetto che contiene **o** il valore prodotto dal blocco **o** l'eccezione che ha lanciato:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
Il valore si legge in seguito, e scegli tu cosa deve diventare un fallimento:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` trasforma un fallimento in `null`, mentre `getOrElse { ... }` esegue il blocco per costruire un sostituto. Nulla viene lanciato nel punto della chiamata, quindi il fallimento può essere portato con sé e gestito più avanti.
