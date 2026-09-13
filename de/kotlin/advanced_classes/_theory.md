Eine `data class` ist eine Klasse, deren Aufgabe es ist, **Daten zu halten**. Aus den Eigenschaften, die du im Primärkonstruktor deklarierst, generiert der Compiler vier Member für dich:

- `toString()`, ein lesbarer `ClassName(prop=value, ...)`-Text
- `equals()` und `hashCode()`, sodass zwei Instanzen mit denselben Daten als gleich gelten
- `copy()`, das eine neue Instanz erstellt, die die aktuellen Werte wiederverwendet

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` zeigt seine volle Stärke mit **benannten Argumenten**: Du benennst nur die Eigenschaften, die du ändern möchtest, und alle anderen Werte werden übernommen.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

Das Original wird nie verändert: `copy()` gibt ein komplett neues Objekt zurück.

---

Für jede Eigenschaft im Primärkonstruktor generiert eine data class auch eine `componentN()`-Funktion: `component1()` für die erste Eigenschaft, `component2()` für die zweite und so weiter.

Diese Funktionen ermöglichen **Destructuring-Deklarationen**, bei denen du ein Objekt in einer Zeile in mehrere Variablen entpackst:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

Die Reihenfolge der Variablen folgt der Reihenfolge der Eigenschaften, nicht ihren Namen. Mit `_` überspringst du eine, die du nicht brauchst:

```kotlin
val (_, onlyY) = point
```

---

Das generierte `equals()` macht `==` zu einem **strukturellen** Vergleich: Zwei Instanzen sind gleich, wenn jede Eigenschaft des Primärkonstruktors gleich ist. Der Operator `===` ist anders: Er fragt, ob beide Namen auf **dasselbe Objekt** im Speicher zeigen.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, same data
println(a === b) // false, two different objects
println(a === a) // true
```

Da `hashCode()` zusammen mit `equals()` generiert wird, verhalten sich data-class-Instanzen auch in einem `Set` oder als `Map`-Schlüssel korrekt: Duplikate verschmelzen.

```kotlin
println(setOf(a, b).size) // 1
```

Eine normale Klasse generiert nichts davon, daher fällt `==` bei ihr auf Identität zurück.

---

Die generierten Member beachten nur die Eigenschaften, die im **Primärkonstruktor** deklariert sind. Eine im **Klassenkörper** deklarierte Eigenschaft ist eine normale Eigenschaft: Sie ist nicht Teil von `toString()`, `equals()`, `hashCode()` oder `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

Das ist leicht zu vergessen: Lege also alles, was das Objekt identifiziert, in den Primärkonstruktor und behalte abgeleiteten oder temporären Zustand im Körper.

---

Eine `sealed`-Klasse beschreibt eine **geschlossene** Menge von Alternativen: Nur die Unterklassen, die im selben Paket und Modul geschrieben sind, sind erlaubt, daher kennt der Compiler jede einzelne davon.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

Der Gewinn ist das **erschöpfende `when`**: Wenn du über einen sealed-Typ verzweigst und jede Unterklasse abdeckst, kannst du den `else`-Zweig weglassen. Fügst du später eine neue Unterklasse hinzu, meldet der Compiler jedes `when`, das du vergessen hast zu aktualisieren, statt stumm den `else`-Zweig zu nehmen.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Nach `is Circle` ist der Wert smart cast, sodass `shape.radius` innerhalb dieses Zweigs ohne manuellen Cast verfügbar ist.
