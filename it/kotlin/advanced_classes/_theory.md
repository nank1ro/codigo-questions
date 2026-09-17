Una `data class` è una classe il cui compito è **contenere dati**. Dalle proprietà che dichiari nel costruttore primario il compilatore genera per te quattro membri:

- `toString()`, un testo leggibile nella forma `ClassName(prop=value, ...)`
- `equals()` e `hashCode()`, così due istanze con gli stessi dati risultano uguali
- `copy()`, che costruisce una nuova istanza riutilizzando i valori attuali

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` dà il meglio di sé con gli **argomenti con nome**: indichi solo le proprietà che vuoi cambiare, e ogni altro valore viene riportato.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

L'originale non viene mai modificato: `copy()` restituisce un oggetto del tutto nuovo.

---

Per ogni proprietà del costruttore primario una data class genera anche una funzione `componentN()`: `component1()` per la prima proprietà, `component2()` per la seconda, e così via.

Queste funzioni alimentano le **dichiarazioni di destrutturazione**, con cui scomponi un oggetto in più variabili in una sola riga:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

L'ordine delle variabili segue l'ordine delle proprietà, non i loro nomi. Usa `_` per saltare quella che non ti serve:

```kotlin
val (_, onlyY) = point
```

---

L'`equals()` generato rende `==` un confronto **strutturale**: due istanze sono uguali quando ogni proprietà del costruttore primario è uguale. L'operatore `===` è diverso, chiede se entrambi i nomi puntano **allo stesso identico oggetto** in memoria.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, stessi dati
println(a === b) // false, due oggetti diversi
println(a === a) // true
```

Poiché `hashCode()` viene generato insieme a `equals()`, le istanze di una data class si comportano correttamente anche dentro un `Set` o come chiavi di una `Map`: i duplicati collassano.

```kotlin
println(setOf(a, b).size) // 1
```

Una classe normale non genera nulla di tutto questo, quindi per essa `==` ricade sull'identità.

---

I membri generati considerano solo le proprietà dichiarate nel **costruttore primario**. Una proprietà dichiarata nel **corpo** della classe è una proprietà normale: non fa parte di `toString()`, `equals()`, `hashCode()` o `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

È facile dimenticarsene, quindi metti nel costruttore primario tutto ciò che identifica l'oggetto, e tieni nel corpo lo stato derivato o temporaneo.

---

Una classe `sealed` descrive un insieme **chiuso** di alternative: sono ammesse solo le sottoclassi scritte nello stesso package e modulo, così il compilatore le conosce tutte.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

Il vantaggio è il **`when` esaustivo**: quando ramifichi su un tipo sealed e copri ogni sottoclasse, puoi omettere il ramo `else`. Se più avanti aggiungi una nuova sottoclasse, il compilatore segnala ogni `when` che hai dimenticato di aggiornare, invece di prendere silenziosamente l'`else`.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Dopo `is Circle` il valore viene sottoposto a smart cast, quindi `shape.radius` è disponibile dentro quel ramo senza alcun cast manuale.

---

A volte serve esattamente **una** istanza di qualcosa: un logger, un registro, una configurazione dell'applicazione. Sostituire `class` con `object` dichiara quel singleton al posto tuo:

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

L'istanza viene creata la prima volta che la usi, e adoperi direttamente il nome: non c'è nessuna chiamata `Registry()` e nessun costruttore. Un `object` può contenere proprietà, metodi, blocchi `init`, e può implementare interfacce o estendere una classe.

---

Un `companion object` è il singleton che appartiene a una classe. Oltre alle costanti, il suo compito naturale è contenere **funzioni factory**: funzioni che controllano o trasformano l'input prima di costruire un'istanza, e che possono restituire `null` quando l'input non ha senso.

Marcare il costruttore come `private` obbliga ogni chiamante a passare dalla factory:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

Il companion si chiama sul nome della classe, `Age.of(...)`, e può raggiungere il costruttore privato perché vive dentro la classe.

---

Un'`interface` elenca ciò che un tipo sa fare. I suoi membri sono astratti per impostazione predefinita, ma un'interfaccia può anche fornire un'**implementazione di default**, un corpo che ogni classe che la implementa eredita gratuitamente e può sovrascrivere:

```kotlin
interface Greeter {
    val name: String              // astratto, la classe deve fornirlo
    fun greet(): String = "Hi, $name"  // implementazione di default
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

Un'interfaccia non può conservare stato (non ha backing field), quindi una proprietà astratta deve essere implementata dalla classe, di solito con `override val` nel costruttore. A differenza di una classe, un tipo può implementare tutte le interfacce che vuole.

---

Una classe `abstract` sta tra un'interfaccia e una classe normale: non può essere istanziata, e mescola membri **astratti**, che non hanno corpo e devono essere sovrascritti, con membri concreti che le sottoclassi ereditano così come sono.

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

A differenza di un'interfaccia, una classe astratta ha un costruttore e può conservare stato nelle proprietà, ed è per questo che la sottoclasse passa `name` verso l'alto con `: Vehicle(name)`. Una classe può estendere una sola classe, quindi scegli una classe astratta quando le sottoclassi condividono dati, e un'interfaccia quando condividono solo comportamento. I membri astratti sono sovrascrivibili senza aggiungere `open`.

---

Una classe dichiarata dentro un'altra classe è **nested** per impostazione predefinita. Non sa nulla dell'istanza esterna e la costruisci a partire dal nome della classe esterna:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Aggiungi la parola chiave `inner` e la situazione cambia: una classe `inner` porta con sé un riferimento all'istanza esterna, quindi può leggerne le proprietà, e la costruisci **a partire da un'istanza**:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

Dentro una classe `inner`, `this` è l'oggetto interno; usa `this@Counter` quando ti serve esplicitamente quello esterno.

---

I pezzi di questo argomento di solito si combinano: una `enum class` le cui costanti portano proprietà proprie modella un insieme fisso di etichette, mentre una `data class` porta il contenuto che le accompagna.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
