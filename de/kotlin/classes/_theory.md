Eine **Klasse** ist ein Bauplan für die Erstellung von Objekten. In Kotlin deklariert man eine Klasse mit dem Schlüsselwort `class`, gefolgt vom Klassennamen.

Eine Klasse kann **Eigenschaften** (Daten) und **Methoden** (Verhalten) enthalten. Um eine Eigenschaft direkt im Konstruktor zu deklarieren, stellt man ihr `val` oder `var` voran:

```kotlin
class Dog(val name: String)
```

Dies erstellt eine `Dog`-Klasse mit einer `name`-Eigenschaft. Eine Instanz erstellt man, indem man die Klasse wie eine Funktion aufruft:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Klassen können mehrere Eigenschaften in ihrem **primären Konstruktor** haben. Jede Eigenschaft wird mit `val` (schreibgeschützt) oder `var` (veränderlich) direkt in der Konstruktorparameterliste deklariert:

```kotlin
class Person(val name: String, var age: Int)
```

Das Schlüsselwort `val` macht `name` nach der Erstellung schreibgeschützt, während `var` `age` veränderlich macht — man kann es später ändern:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // erlaubt, weil age var ist
```

---

Der **`init`-Block** wird unmittelbar nach dem primären Konstruktor ausgeführt. Er wird verwendet, um Validierungs- oder Einrichtungslogik durchzuführen, wenn ein Objekt erstellt wird:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "Radius must be positive" }
    }
}
```

Man kann im `init`-Block auch zusätzliche Eigenschaften initialisieren:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Klassen können **Methoden** enthalten — Funktionen, die zur Klasse gehören und auf ihren Eigenschaften arbeiten:

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

Methoden werden mit Punktnotation auf einer Instanz aufgerufen:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

Eine **`data class`** ist eine spezielle Klasse zum Speichern von Daten. Kotlin generiert automatisch `equals()`, `hashCode()`, `toString()` und `copy()` für uns:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)            // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

Die Funktion `copy()` erstellt eine neue Instanz mit einigen geänderten Eigenschaften:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
