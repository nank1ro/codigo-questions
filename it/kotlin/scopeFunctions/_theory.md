Le **scope functions** eseguono un blocco di codice *nel contesto di un oggetto*. Non aggiungono nuove funzionalità al linguaggio: rendono semplicemente più corto e leggibile il codice che lavora su un solo oggetto. Kotlin ne ha cinque: `let`, `run`, `with`, `apply` e `also`.

Differiscono solo su **due** punti: come viene referenziato l'oggetto dentro il blocco, e cosa restituisce la chiamata. Iniziamo con `let`: dentro il suo blocco l'oggetto si chiama `it`, e la chiamata restituisce il **risultato dell'ultima espressione** del blocco.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Senza `let` ti servirebbe una variabile temporanea; con esso l'oggetto è disponibile con il breve nome `it` finché dura il blocco.

---

Poiché `let` restituisce il valore della sua ultima espressione, è un modo pratico per **trasformare un valore in qualcos'altro** senza dover dare un nome a una variabile intermedia:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Dentro il blocco puoi usare `it` tutte le volte che ti serve:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` diventa davvero utile dopo una safe call. `?.let { ... }` esegue il blocco **solo** quando il valore non è `null`, e dentro il blocco `it` è un valore non-null, quindi non serve alcun controllo extra:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
Quando il valore è `null` l'intera espressione è `null` e il blocco non viene mai eseguito, quindi l'operatore Elvis `?:` è il partner naturale per fornire un valore di riserva:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Dentro un blocco `let` non sei costretto a chiamare l'oggetto `it`: puoi dare un nome al parametro della lambda, cosa che mantiene il codice leggibile quando i blocchi sono annidati o quando `it` non direbbe nulla di utile.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
La stessa nomenclatura funziona per ogni scope function che usa `it`, quindi per `let` e `also`.

---

`apply` avanza su entrambi gli assi contemporaneamente: dentro il suo blocco l'oggetto è il ricevente `this` (quindi i suoi membri si possono usare **senza alcun prefisso**), e la chiamata restituisce **l'oggetto stesso**, non il risultato del blocco.

Quella combinazione rende `apply` lo strumento per **configurare** un oggetto proprio nel momento in cui lo crei:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
`host` e `port` dentro il blocco sono `this.host` e `this.port`; poiché `apply` restituisce il `Server` configurato, si può assegnare subito.

---

`apply` non è limitato agli oggetti che hai appena creato: funziona su qualsiasi oggetto, e poiché restituisce l'oggetto puoi usare l'intera espressione ovunque ci si aspetti quell'oggetto.
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
Il blocco è un normale blocco di codice, quindi può contenere quante istruzioni ti servono.

---

`also` è l'immagine speculare di `apply`: l'oggetto viene referenziato come `it`, e la chiamata restituisce **l'oggetto stesso**. Poiché il risultato del blocco viene scartato, `also` è pensato per **effetti collaterali** come il logging o la verifica, e si può inserire in mezzo a una catena senza cambiare ciò che la catena produce:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Leggilo come *"e fai anche questo con esso"*: il valore continua a fluire al passaggio successivo invariato.

---

Quando il blocco ha bisogno dell'oggetto come **argomento** di qualcos'altro, `also` si legge meglio di `apply`: `it` può essere passato direttamente, mentre `this` andrebbe scritto per esteso.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
Il valore dell'espressione resta comunque `"ada"`: `also` si limita a guardarlo passare.

---

`run` è `let` con l'altro modo di riferirsi all'oggetto: dentro il blocco l'oggetto è `this`, quindi i suoi membri non hanno bisogno di prefisso, e la chiamata restituisce il **risultato dell'ultima espressione**.

È adatto quando leggi più membri dello stesso oggetto per calcolare un valore:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Confrontalo con `apply`, che usa `this` esattamente allo stesso modo ma restituisce l'oggetto invece del risultato del blocco.

---

`with` fa lo stesso lavoro di `run`, ma **non** è un'estensione: l'oggetto viene passato come primo argomento invece di essere il ricevente di una chiamata col punto.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Dentro il blocco l'oggetto è `this` e la chiamata restituisce l'ultima espressione, esattamente come `run`. Preferisci `with` quando hai già un oggetto non-null e vuoi raggruppare più chiamate su di esso; preferisci `run` quando l'oggetto esce da una catena o può richiedere una safe call (`obj?.run { ... }`).

---

Tutte e cinque le scope functions sono ora sul tavolo, e ognuna è solo un punto sui due assi:
- `let` - l'oggetto è `it`, restituisce il risultato del blocco
- `run` - l'oggetto è `this`, restituisce il risultato del blocco
- `with` - l'oggetto è `this` (passato come argomento), restituisce il risultato del blocco
- `apply` - l'oggetto è `this`, restituisce l'oggetto
- `also` - l'oggetto è `it`, restituisce l'oggetto

Scegli la riga che ti serve: `it` si legge meglio quando passi l'oggetto a qualcos'altro, `this` si legge meglio quando tocchi molti dei suoi membri; restituisce il risultato del blocco quando vuoi un nuovo valore, restituisce l'oggetto quando vuoi continuare a lavorare con esso.
