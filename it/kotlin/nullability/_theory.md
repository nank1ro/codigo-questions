A volte un valore semplicemente manca: un utente senza secondo nome, una ricerca che non trova nulla, un testo che non può essere convertito in un numero.
Kotlin rappresenta un valore mancante con `null`, ma una variabile normale non può mai contenerlo. Ogni tipo è **non-null** per default:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Per consentire un valore mancante dichiari un tipo **nullable** aggiungendo un punto interrogativo `?` dopo il tipo.
Una `String?` contiene oppure una `String` oppure `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` e `String?` sono due tipi diversi: una `String` non manca mai, una `String?` può mancare.

---

La differenza tra `String` e `String?` è verificata dal **compilatore**, non a runtime.
Assegnare `null` a un tipo non-null, o passare un valore nullable dove se ne aspetta uno non-null, è un errore di compilazione, quindi il programma non parte nemmeno:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
È così che Kotlin evita i crash da "null pointer" comuni in altri linguaggi: un valore può mancare solo dove l'hai dichiarato esplicitamente con `?`.

---

Il `?` funziona ovunque sia scritto un tipo: una funzione può accettare un parametro nullable e può restituire un valore nullable.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
Non puoi chiamare un metodo direttamente su un valore nullable, perché potrebbe essere `null`.
L'operatore **safe call** `?.` chiama il metodo solo quando il valore non è `null`; altrimenti l'intera espressione è `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
Il risultato di una safe call è sempre nullable: `word?.length` è un `Int?`, non un `Int`.

---

Molto spesso tutto ciò che vuoi da un valore nullable è il valore stesso oppure un valore predefinito.
L'**operatore Elvis** `?:` fa esattamente questo: restituisce il lato sinistro quando non è `null`, altrimenti il valore alla sua destra:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Dato che il lato destro viene usato solo quando il sinistro è `null`, il risultato è non-null quando lo è il valore predefinito.
`?:` si combina bene con `?.` per trasformare una safe call di nuovo in un valore normale:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Le safe call possono essere **concatenate**: appena un anello è `null` il resto della catena viene saltato e l'intera espressione diventa `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Una catena che termina con `?:` ti dà un risultato non-null in una sola riga:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Le catene di safe call danno il meglio di sé con oggetti annidati, dove qualsiasi livello può mancare:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Ogni `?.` protegge il passaggio successivo, e il `?:` finale fornisce il valore predefinito.

---

L'operatore **not-null assertion** `!!` converte un valore nullable in uno non-null, dicendo al compilatore "sono sicuro che questo non è `null`":
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Se ti sbagli e il valore è `null`, il programma lancia una `NullPointerException` a runtime, proprio l'errore che Kotlin è stato progettato per prevenire:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Usa `!!` solo quando il valore non può davvero essere `null`; preferisci `?.`, `?:` e le verifiche per `null` in tutti gli altri casi.

---

Quando verifichi se un valore è `null` con `if`, il compilatore se lo ricorda: nel ramo in cui il valore è noto come non-null, viene applicato uno **smart cast** al tipo non-null e puoi usarlo direttamente, senza `?.` o `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
Lo stesso accade dopo un'uscita anticipata:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Gli smart cast funzionano sulle variabili `val` e sui parametri delle funzioni, il cui valore non può cambiare tra la verifica e l'uso.

---

`let` esegue un blocco di codice con il valore su cui è chiamato, disponibile dentro il blocco come `it`.
Combinato con una safe call, `?.let` esegue il blocco **solo** quando il valore non è `null`, e dentro il blocco `it` è non-null:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
È un'alternativa compatta a `if (x != null) { ... }` quando ti serve solo il valore dentro il blocco.

---

`let` **restituisce** anche il valore dell'ultima espressione nel suo blocco, così `?.let` può trasformare un valore nullable e `?:` può inserire il valore predefinito quando è `null`:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Quando `price` è `null` il blocco `let` viene saltato, l'espressione è `null` e l'operatore Elvis restituisce `"free"`.

---

Anche le collezioni possono contenere elementi nullable: una `List<Int?>` può contenere elementi `null`, mentre una `List<Int>` mai.
`filterNotNull()` restituisce una nuova lista senza gli elementi `null`, e il tipo dei suoi elementi diventa non-null, così puoi usare gli elementi liberamente:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Molte funzioni della libreria standard restituiscono `null` invece di fallire. `toIntOrNull()` converte una stringa in un `Int`, oppure restituisce `null` quando il testo non è un numero intero:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` trasforma ogni elemento come `map`, ma scarta i risultati che sono `null`:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

A volte una proprietà non può ricevere un valore quando l'oggetto viene creato, ma sai che verrà impostata prima di essere usata.
Invece di renderla nullable, marchiala con `lateinit`: il tipo resta non-null e non serve alcun `?.` quando la leggi:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` ha alcune regole: funziona solo su proprietà `var`, solo con tipi non-null, e non con i tipi primitivi come `Int` o `Boolean`.
Leggere una proprietà `lateinit` prima di assegnarla lancia una `UninitializedPropertyAccessException`; puoi verificarla prima con `::player.isInitialized`.

---

Quando un `null` significa che chi chiama ha commesso un errore, fallisci presto con `requireNotNull`.
Restituisce il valore come non-null quando è presente, e lancia una `IllegalArgumentException` quando è `null`, con un messaggio opzionale:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
Dopo la chiamata il compilatore applica anche uno smart cast a `name` stesso come `String`, quindi `name.length` è consentito da quella riga in poi.
A differenza di `!!`, l'errore porta con sé un messaggio chiaro e indica che è stato sbagliato l'*argomento*.

---

Una funzione di estensione può essere dichiarata su un **ricevente nullable**, quindi può essere chiamata anche su un valore `null`. Al suo interno, `this` è nullable e deve essere verificato:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Nota che non serve alcun `?.` nel punto di chiamata: è la funzione stessa a gestire il caso `null`.
La libreria standard usa questo trucco in `isNullOrEmpty()` e `orEmpty()`, che si possono chiamare senza problemi su qualsiasi `String?`.

---

Il lato destro di `?:` può essere qualsiasi espressione, incluso `return`. Questo offre un modo compatto per uscire da una funzione appena un valore manca:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Tutti gli strumenti che hai visto si combinano bene: parametri nullable e tipi di ritorno descrivono *dove* un valore può mancare, e `?.`, `?:`, `let`, gli smart cast e `toIntOrNull` lo gestiscono senza mai andare in crash.
