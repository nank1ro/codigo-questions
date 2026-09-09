Una **funzione di estensione** aggiunge una nuova funzione a un tipo esistente senza toccarne il codice sorgente.
Si scrive `fun`, poi il tipo che si vuole estendere (il **tipo ricevente**), un punto e il nome della funzione:
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Dentro la funzione, `this` è il valore su cui la funzione viene chiamata, detto **ricevente**: in `4.squared()` è `4`.
Una volta che l'estensione esiste, la si chiama con il punto esattamente come una funzione che facesse parte di `Int` fin dall'inizio.

---

Le estensioni funzionano su qualsiasi tipo, anche su quelli di cui non hai il codice sorgente. `String` viene dalla libreria standard, ma puoi comunque darle nuove funzioni:
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Dentro un'estensione puoi omettere `this.` quando usi altri membri del ricevente: `lowercase()` da solo significa `this.lowercase()`, e `length` da solo significa `this.length`.

---

Una funzione di estensione può avere parametri come qualsiasi altra funzione. Il ricevente resta a sinistra del punto e i parametri vanno fra le parentesi:
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
Il tipo davanti al punto è un tipo normale, quindi puoi estendere `List<Int>`, `Double` o una classe che hai scritto tu allo stesso modo.

---

Un'estensione **non** modifica la classe che estende e non le inserisce un nuovo membro. Il compilatore riscrive semplicemente la chiamata: `"kotlin".first3()` diventa una chiamata alla funzione con `"kotlin"` passato come `this`.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
Ecco perché puoi estendere classi final come `String` e `Int`: al loro interno non cambia nulla, l'estensione vive solo nel tuo codice.

---

Oltre alle funzioni, puoi aggiungere una **proprietà di estensione**. Si dichiara con `val`, il tipo ricevente, un punto e il nome, seguiti da un `get()` che calcola il valore ogni volta che la proprietà viene letta:
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
Una proprietà di estensione non può memorizzare nulla: non ha un campo di appoggio, quindi un inizializzatore come `val String.label = "text"` è un errore di compilazione. Può solo calcolare il suo valore dal ricevente.
Le proprietà di estensione non possono essere dichiarate dentro una funzione (le proprietà di estensione locali non sono ammesse), a differenza delle funzioni di estensione.

---

Le proprietà di estensione si leggono senza parentesi, esattamente come il `length` predefinito di una `String`. Sono la scelta naturale quando il valore descrive il ricevente invece di farci qualcosa:
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Nota le parentesi attorno a `-3`: senza di esse `-3.isNegative` leggerebbe prima la proprietà di `3` e poi proverebbe a negare un `Boolean`, cosa che non compila.

---

Il tipo ricevente può essere **nullable**. Un'estensione su `String?` può essere chiamata su una variabile che potrebbe contenere `null`, e dentro la funzione `this` è una `String?`, quindi il caso `null` lo gestisci tu, di solito con l'operatore Elvis `?:` che hai visto nelle lezioni sulla nullabilità:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
Chiamare `name.orDash()` su un valore `null` è sicuro: non serve `?.`, perché è la funzione stessa ad accettare un ricevente `null`.

---

Dentro un'estensione con ricevente nullable puoi anche usare la chiamata sicura `this?.` per raggiungere i membri del valore solo quando non è `null`. La libreria standard usa la stessa idea per funzioni come `isNullOrEmpty()`:
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

Quando una classe ha già un membro con lo stesso nome e gli stessi parametri di un'estensione, **vince sempre il membro**: l'estensione non viene mai chiamata, e il compilatore ti avvisa che è oscurata.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
Un'estensione non può sovrascrivere o sostituire un comportamento esistente; può solo aggiungere nuove funzioni e proprietà. Per essere scelta, un'estensione ha bisogno di un nome o di una lista di parametri che la classe non abbia già.

---

Un'estensione può lavorare su una famiglia di tipi tutta insieme grazie a un **parametro di tipo**: un segnaposto per un tipo, dichiarato fra parentesi angolari subito dopo `fun`, che Kotlin riempie a ogni chiamata. Questo rende l'estensione **generica**:
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
Con `listOf(1, 2, 3)` il segnaposto `T` è `Int`, con `listOf("a", "b")` è `String`, così la stessa funzione restituisce ogni volta il tipo giusto.

---

Il parametro di tipo può essere usato ovunque nella firma: come tipo di ritorno, come `T?` nullable, o dentro un altro tipo. Un'estensione generica che potrebbe non trovare nulla restituisce `T?`, come il `firstOrNull()` predefinito:
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Dentro la funzione puoi usare `size`, `isEmpty()` e l'indicizzazione esattamente come su qualsiasi lista, perché il ricevente è una `List<T>`.

---

Puoi anche estendere il **companion object** di una classe, purché la classe ne dichiari uno, anche vuoto. Il tipo ricevente si scrive `ClassName.Companion`, e l'estensione si chiama poi sul nome della classe, come una funzione factory:
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
La classe e l'estensione sono entrambe dichiarazioni di primo livello, quindi vanno scritte fuori da `main`.

---

Un'estensione su companion può avere parametri, il che ne fa un posto comodo per costruttori alternativi che convertono da un'altra unità o da un altro formato:
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

Dove dichiari un'estensione decide dove può essere usata, il suo **scope**:
- al primo livello di un file, è disponibile in tutto il file e nel resto del package
- dentro una funzione, è un'estensione locale, usabile solo in quella funzione
- dentro una classe, è un'**estensione membro**, usabile solo dentro quella classe

Un'estensione membro può leggere le proprietà della classe in cui vive, quindi combina due riceventi: l'istanza della classe e il valore su cui viene chiamata:
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Dentro `greet`, `greeting` viene dal `Greeter` e `this` è la `String` su cui la funzione viene chiamata. Fuori dalla classe, `"Ada".greet()` è un errore di compilazione.

---

Una funzione di estensione con esattamente **un** parametro può essere marcata `infix`. Una funzione infix può essere chiamata senza il punto e senza le parentesi, con il ricevente a sinistra e l'argomento a destra, cosa che si legge quasi come una frase:
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin la usa anche per alcune funzioni predefinite: `1 to "one"` costruisce una `Pair`, e `1 until 5` costruisce un intervallo.

---

Per poter essere marcata `infix`, una funzione deve essere un membro o un'estensione, deve avere esattamente un parametro, e quel parametro non può avere un valore predefinito. Qualsiasi altra cosa è un errore di compilazione:
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Le chiamate infix hanno una precedenza fra l'aritmetica e il confronto: `1 add 2 * 3` è `1 add 6`, mentre `1 add 2 == 3` confronta il risultato con `3`.
