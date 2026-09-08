Manchmal fehlt ein Wert einfach: ein Benutzer ohne zweiten Vornamen, eine Suche ohne Ergebnis, ein Text, der sich nicht in eine Zahl umwandeln lässt.
Kotlin repräsentiert einen fehlenden Wert mit `null`, aber eine normale Variable kann ihn niemals aufnehmen. Jeder Typ ist standardmäßig **non-null**:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Um einen fehlenden Wert zuzulassen, deklarieren Sie einen **Nullable-Typ**, indem Sie ein Fragezeichen `?` an den Typ anhängen.
Ein `String?` enthält entweder einen `String` oder `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` und `String?` sind zwei verschiedene Typen: Ein `String` fehlt nie, ein `String?` kann es.

---

Der Unterschied zwischen `String` und `String?` wird vom **Compiler** geprüft, nicht zur Laufzeit.
Weisen Sie `null` einem Non-Null-Typ zu oder übergeben Sie einen Nullable-Wert, wo ein Non-Null-Wert erwartet wird, entsteht ein Kompilierungsfehler, sodass das Programm gar nicht erst startet:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
So vermeidet Kotlin die in anderen Sprachen verbreiteten Abstürze durch „Nullzeiger“: Ein Wert kann nur dort fehlen, wo Sie ihn ausdrücklich mit `?` deklariert haben.

---

Das `?` funktioniert überall dort, wo ein Typ geschrieben wird: Eine Funktion kann einen Nullable-Parameter entgegennehmen und einen Nullable-Wert zurückgeben.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
Sie können eine Methode nicht direkt auf einem Nullable-Wert aufrufen, weil er `null` sein könnte.
Der **Safe-Call**-Operator `?.` ruft die Methode nur auf, wenn der Wert nicht `null` ist; andernfalls ist der gesamte Ausdruck `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
Das Ergebnis eines Safe-Calls ist immer nullable: `word?.length` ist ein `Int?`, kein `Int`.

---

Sehr oft möchte man von einem Nullable-Wert nur den Wert selbst oder einen Standardwert.
Der **Elvis-Operator** `?:` macht genau das: Er gibt die linke Seite zurück, wenn sie nicht `null` ist, andernfalls den Wert auf seiner rechten Seite:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Da die rechte Seite nur verwendet wird, wenn die linke `null` ist, ist das Ergebnis non-null, wenn der Standardwert es ist.
`?:` lässt sich gut mit `?.` kombinieren, um einen Safe-Call wieder in einen einfachen Wert umzuwandeln:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Safe-Calls können **verkettet** werden: Sobald ein Glied der Kette `null` ist, wird der Rest der Kette übersprungen und der gesamte Ausdruck wird zu `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Eine Kette, die mit `?:` endet, liefert Ihnen in einer Zeile ein non-null Ergebnis:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Safe-Call-Ketten zeigen ihre Stärke bei verschachtelten Objekten, bei denen jede Ebene fehlen kann:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Jedes `?.` schützt den nächsten Schritt, und das letzte `?:` liefert den Standardwert.

---

Der **Not-null-Assertion**-Operator `!!` wandelt einen Nullable-Wert in einen Non-Null-Wert um und sagt dem Compiler damit: „Ich bin sicher, dass dies nicht `null` ist“:
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Wenn Sie sich irren und der Wert `null` ist, stürzt das Programm zur Laufzeit mit einer `NullPointerException` ab – genau dem Fehler, den Kotlin verhindern soll:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Verwenden Sie `!!` nur, wenn der Wert wirklich nicht `null` sein kann; ziehen Sie ansonsten überall `?.`, `?:` und Null-Prüfungen vor.

---

Wenn Sie einen Wert mit `if` auf `null` prüfen, merkt sich der Compiler das: Innerhalb des Zweigs, in dem der Wert als non-null bekannt ist, wird er per **Smart-Cast** zum Non-Null-Typ, und Sie können ihn direkt verwenden, ohne `?.` oder `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
Dasselbe geschieht nach einem frühen Absprung:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Smart-Casts funktionieren bei `val`-Variablen und Funktionsparametern, deren Wert sich zwischen der Prüfung und der Verwendung nicht ändern kann.

---

`let` führt einen Codeblock mit dem Wert aus, auf dem er aufgerufen wird; dieser ist innerhalb des Blocks als `it` verfügbar.
Kombiniert mit einem Safe-Call führt `?.let` den Block **nur** aus, wenn der Wert nicht `null` ist, und innerhalb des Blocks ist `it` non-null:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
Er ist eine kompakte Alternative zu `if (x != null) { ... }`, wenn Sie den Wert nur innerhalb des Blocks benötigen.

---

`let` gibt auch den Wert des letzten Ausdrucks in seinem Block **zurück**, sodass `?.let` einen Nullable-Wert umwandeln kann und `?:` den Standardwert einsetzt, wenn er `null` ist:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Wenn `price` `null` ist, wird der `let`-Block übersprungen, der Ausdruck ist `null` und der Elvis-Operator gibt `"free"` zurück.

---

Auch Sammlungen können nullable Elemente enthalten: Eine `List<Int?>` kann `null`-Einträge enthalten, während eine `List<Int>` dies nie tut.
`filterNotNull()` gibt eine neue Liste ohne die `null`-Einträge zurück, und ihr Elementtyp wird non-null, sodass Sie die Elemente frei verwenden können:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Viele Standardfunktionen geben `null` zurück, statt zu scheitern. `toIntOrNull()` wandelt eine Zeichenkette in ein `Int` um oder gibt `null` zurück, wenn der Text keine ganze Zahl ist:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` wandelt jedes Element wie `map` um, verwirft aber die Ergebnisse, die `null` sind:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

Manchmal kann einer Eigenschaft beim Erstellen des Objekts noch kein Wert zugewiesen werden, aber Sie wissen, dass sie gesetzt wird, bevor sie verwendet wird.
Statt sie nullable zu machen, markieren Sie sie mit `lateinit`: Der Typ bleibt non-null und beim Lesen ist kein `?.` nötig:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` hat einige Regeln: Es funktioniert nur bei `var`-Eigenschaften, nur mit Non-Null-Typen und nicht mit primitiven Typen wie `Int` oder `Boolean`.
Liest man eine `lateinit`-Eigenschaft, bevor ihr ein Wert zugewiesen wurde, wird eine `UninitializedPropertyAccessException` ausgelöst; Sie können zuvor mit `::player.isInitialized` prüfen, ob sie initialisiert ist.

---

Wenn ein `null` bedeutet, dass der Aufrufer einen Fehler gemacht hat, brechen Sie früh mit `requireNotNull` ab.
Es gibt den Wert als non-null zurück, wenn er vorhanden ist, und wirft eine `IllegalArgumentException`, wenn er `null` ist, mit einer optionalen Meldung:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
Nach dem Aufruf führt der Compiler auch einen Smart-Cast von `name` selbst zu `String` durch, sodass `name.length` ab dieser Zeile erlaubt ist.
Anders als bei `!!` trägt der Fehler eine klare Meldung und sagt aus, dass das *Argument* falsch war.

---

Eine Erweiterungsfunktion kann für einen **Nullable-Empfänger** deklariert werden, sodass sie sogar auf einem `null`-Wert aufgerufen werden kann. Innerhalb der Funktion ist `this` nullable und muss geprüft werden:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Beachten Sie, dass beim Aufruf kein `?.` nötig ist: Die Funktion selbst behandelt den `null`-Fall.
Die Standardbibliothek verwendet diesen Trick in `isNullOrEmpty()` und `orEmpty()`, die gefahrlos für jedes `String?` aufgerufen werden können.

---

Die rechte Seite von `?:` kann ein beliebiger Ausdruck sein, auch `return`. So lässt sich kompakt aus einer Funktion aussteigen, sobald ein Wert fehlt:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Alle Werkzeuge, die Sie kennengelernt haben, lassen sich gut kombinieren: Nullable-Parameter und Rückgabetypen beschreiben, *wo* ein Wert fehlen kann, und `?.`, `?:`, `let`, Smart-Casts und `toIntOrNull` behandeln ihn, ohne dass das Programm jemals abstürzt.
