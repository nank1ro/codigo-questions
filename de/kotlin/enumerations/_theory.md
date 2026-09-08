Eine **Enumeration** (oder *Enum*) definiert einen gemeinsamen Typ für eine Gruppe verwandter Werte, damit du mit diesen Werten auf typsichere Weise arbeiten kannst.
In Kotlin deklarierst du eine mit den Schlüsselwörtern `enum class` und listest ihre **Einträge** durch Kommas getrennt auf:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
Konventionsgemäß werden die Namen der Einträge in Großbuchstaben geschrieben. Jeder Eintrag ist ein Wert des Enum-Typs und wird über den Klassennamen aufgerufen:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Enum-Klassen müssen auf oberster Ebene einer Datei (oder innerhalb einer anderen Klasse) deklariert werden, niemals innerhalb einer Funktion.

---

Jeder Enum-Eintrag hat zwei eingebaute Eigenschaften:

- `name` ist der Name des Eintrags als `String`
- `ordinal` ist seine Position in der Deklaration, beginnend bei `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Enum-Einträge werden mit `==` verglichen:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Ein `when`-Ausdruck ist der natürliche Weg, um über ein Enum zu verzweigen. Wenn er **jeden** Eintrag abdeckt, ist er *erschöpfend* und benötigt keinen `else`-Zweig:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Wenn du einen Eintrag vergisst, meldet der Compiler einen Fehler, anstatt den Bug zur Laufzeit auftreten zu lassen.

---

Eine Enum-Klasse kann einen **Konstruktor** haben, genau wie eine gewöhnliche Klasse. Jeder Eintrag übergibt dann seine eigenen Argumente, und die Werte werden in Eigenschaften gespeichert:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Konstruktor-Eigenschaften werden meist mit `val` deklariert, da sich die Daten eines Eintrags nicht ändern sollen.

---

Enum-Klassen können auch **Methoden** deklarieren. Die Liste der Einträge muss vor allen Member-Deklarationen mit einem Semikolon `;` abgeschlossen werden:
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
Innerhalb einer Methode kannst du auf die Eigenschaften des Eintrags sowie auf `name` und `ordinal` zugreifen.

---

Jede Enum-Klasse stellt eine `entries`-Eigenschaft bereit: eine Liste all ihrer Einträge in Deklarationsreihenfolge. Das ist praktisch zum Iterieren:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Da `entries` eine Liste ist, unterstützt sie auch `size` und Indizierung, z. B. ist `Direction.entries[0]` gleich `NORTH`.

Älterer Code verwendet stattdessen die Funktion `values()`, die ein Array zurückgibt; `entries` ist seit Kotlin 1.9 die empfohlene Wahl.

---

Um von einem `String` zurück zu einem Eintrag zu gelangen, verwende die Funktion `valueOf`. Sie sucht den Eintrag, dessen `name` exakt übereinstimmt:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
Der Abgleich unterscheidet zwischen Groß- und Kleinschreibung: `Direction.valueOf("east")` wirft eine `IllegalArgumentException`, weil kein Eintrag diesen Namen hat.

---

Eine Enum-Klasse kann eine **abstrakte Methode** deklarieren und jeden Eintrag seine eigene Implementierung in einem in geschweiften Klammern eingeschlossenen Rumpf bereitstellen lassen:
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
Jeder Eintrag verhält sich anders, während er dennoch denselben Typ und dieselbe Methodensignatur teilt.

---

Eine **Schnittstelle** (Interface) deklariert Methoden ohne Rumpf; jeder Typ, der sie implementiert, muss sie bereitstellen:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Enum-Klassen können Schnittstellen implementieren. Du listest die Schnittstelle nach einem Doppelpunkt auf und markierst jede Implementierung mit `override`. Innerhalb des Enum-Rumpfs ist der aktuelle Eintrag `this`, und andere Einträge können ohne den Klassennamen referenziert werden:
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
