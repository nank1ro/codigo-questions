Un'**enumerazione** (o *enum*) definisce un tipo comune per un gruppo di valori correlati, così puoi lavorare con quei valori in modo type-safe.
In Kotlin la dichiari con le parole chiave `enum class`, elencando le sue **voci** separate da virgole:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
Per convenzione i nomi delle voci sono scritti in maiuscolo. Ogni voce è un valore del tipo enum e vi si accede tramite il nome della classe:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Le classi enum devono essere dichiarate al livello superiore di un file (o all'interno di un'altra classe), mai all'interno di una funzione.

---

Ogni voce di un enum ha due proprietà integrate:

- `name` è il nome della voce come `String`
- `ordinal` è la sua posizione nella dichiarazione, a partire da `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Le voci di un enum si confrontano con `==`:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Un'espressione `when` è il modo naturale per diramarsi su un enum. Quando copre **ogni** voce è *esaustiva* e non necessita di un ramo `else`:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Se dimentichi una voce, il compilatore segnala un errore invece di lasciare che il bug arrivi a runtime.

---

Un enum può avere un **costruttore**, proprio come una classe normale. Ogni voce passa allora i propri argomenti, e i valori vengono memorizzati in proprietà:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Le proprietà del costruttore sono di solito dichiarate con `val`, poiché i dati di una voce non sono pensati per cambiare.

---

Le classi enum possono anche dichiarare **metodi**. L'elenco delle voci deve essere chiuso con un punto e virgola `;` prima di qualsiasi dichiarazione di membro:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
All'interno di un metodo puoi accedere alle proprietà della voce, così come a `name` e `ordinal`.

---

Ogni classe enum espone una proprietà `entries`: una lista di tutte le sue voci nell'ordine di dichiarazione. È comoda per iterare:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Essendo una lista, `entries` supporta anche `size` e l'indicizzazione, ad esempio `Direction.entries[0]` è `NORTH`.

Il codice più vecchio usa invece la funzione `values()`, che restituisce un array; `entries` è la scelta consigliata a partire da Kotlin 1.9.

---

Per passare da una `String` a una voce, usa la funzione `valueOf`. Cerca la voce il cui `name` corrisponde esattamente:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
Il confronto distingue maiuscole e minuscole: `Direction.valueOf("east")` lancia una `IllegalArgumentException` perché nessuna voce ha quel nome.

---

Una classe enum può dichiarare un **metodo astratto** e lasciare che ogni voce fornisca la propria implementazione in un corpo racchiuso tra parentesi graffe:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
Ogni voce si comporta in modo diverso pur condividendo lo stesso tipo e la stessa firma del metodo.

---

Un'**interfaccia** dichiara metodi senza corpo; qualsiasi tipo che la implementa deve fornirli:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Le classi enum possono implementare interfacce. Elenchi l'interfaccia dopo i due punti e contrassegni ogni implementazione con `override`. All'interno del corpo dell'enum, la voce corrente è `this` e le altre voci possono essere referenziate senza il nome della classe:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
