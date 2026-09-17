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
println(a == b)  // true, dieselben Daten
println(a === b) // false, zwei verschiedene Objekte
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

---

Manchmal brauchst du genau **eine** Instanz von etwas: einen Logger, eine Registrierung, eine Anwendungskonfiguration. Ersetzt du `class` durch `object`, deklariert das dieses Singleton für dich:

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

Die Instanz wird erstellt, sobald du sie zum ersten Mal berührst, und du verwendest den Namen selbst: Es gibt keinen `Registry()`-Aufruf und keinen Konstruktor. Ein `object` kann Eigenschaften, Methoden und `init`-Blöcke enthalten, und es kann Interfaces implementieren oder eine Klasse erweitern.

---

Ein `companion object` ist das Singleton, das zu einer Klasse gehört. Neben Konstanten besteht seine natürliche Aufgabe darin, **Fabrikfunktionen** zu beherbergen: Funktionen, die die Eingabe prüfen oder umwandeln, bevor sie eine Instanz erstellen, und die `null` zurückgeben können, wenn die Eingabe keinen Sinn ergibt.

Markiert man den Konstruktor als `private`, wird jeder Aufrufer durch die Fabrik gezwungen:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

Der Companion wird über den Klassennamen aufgerufen, `Age.of(...)`, und er kann auf den privaten Konstruktor zugreifen, weil er innerhalb der Klasse lebt.

---

Ein `interface` listet auf, was ein Typ kann. Seine Member sind standardmäßig abstrakt, aber ein Interface kann auch eine **Standardimplementierung** mitliefern: einen Körper, den jede implementierende Klasse gratis erbt und überschreiben darf:

```kotlin
interface Greeter {
    val name: String              // abstract, die Klasse muss es bereitstellen
    fun greet(): String = "Hi, $name"  // Standardimplementierung
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

Ein Interface kann keinen Zustand speichern (es hat keine Backing-Fields), daher muss eine abstrakte Eigenschaft von der Klasse implementiert werden, üblicherweise mit `override val` im Konstruktor. Anders als eine Klasse kann ein Typ so viele Interfaces implementieren, wie er will.

---

Eine `abstract`-Klasse liegt zwischen einem Interface und einer normalen Klasse: Sie kann nicht instanziiert werden und mischt **abstrakte** Member, die keinen Körper haben und überschrieben werden müssen, mit konkreten, die Unterklassen unverändert erben.

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

Anders als ein Interface hat eine abstrakte Klasse einen Konstruktor und kann Zustand in Eigenschaften speichern — deshalb übergibt die Unterklasse `name` mit `: Vehicle(name)` nach oben. Eine Klasse kann nur eine andere Klasse erweitern: Greife also zu einer abstrakten Klasse, wenn die Unterklassen Daten teilen, und zu einem Interface, wenn sie nur Verhalten teilen. Abstrakte Member sind überschreibbar, ohne `open` hinzuzufügen.

---

Eine Klasse, die innerhalb einer anderen Klasse deklariert ist, ist standardmäßig **verschachtelt**. Sie weiß nichts über die äußere Instanz, und du erstellst sie über den Namen der äußeren Klasse:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Fügst du das Schlüsselwort `inner` hinzu, ändert sich die Lage: Eine `inner`-Klasse trägt eine Referenz auf die äußere Instanz, kann also die äußeren Eigenschaften lesen, und du erstellst sie **aus einer Instanz**:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

Innerhalb einer `inner`-Klasse ist `this` das innere Objekt; verwende `this@Counter`, wenn du das äußere explizit brauchst.

---

Die Bausteine dieses Themas werden üblicherweise kombiniert: Eine `enum class`, deren Einträge eigene Eigenschaften tragen, modelliert eine feste Menge von Tags, während eine `data class` die Nutzdaten trägt, die dazugehören.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
