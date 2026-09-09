Eine **Erweiterungsfunktion** fügt einem bestehenden Typ eine neue Funktion hinzu, ohne dessen Quellcode anzufassen.
Sie schreiben `fun`, dann den Typ, den Sie erweitern wollen (den **Empfängertyp**), einen Punkt und den Namen der Funktion:
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Innerhalb der Funktion ist `this` der Wert, auf dem die Funktion aufgerufen wird, der **Empfänger**: in `4.squared()` ist es `4`.
Sobald die Erweiterung existiert, rufen Sie sie mit dem Punkt genau so auf wie eine Funktion, die von Anfang an Teil von `Int` gewesen wäre.

---

Erweiterungen funktionieren mit jedem Typ, sogar mit denen, deren Quellcode Sie nicht haben. `String` stammt aus der Standardbibliothek, aber Sie können ihm trotzdem neue Funktionen geben:
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Innerhalb einer Erweiterung können Sie `this.` weglassen, wenn Sie andere Member des Empfängers verwenden: `lowercase()` allein bedeutet `this.lowercase()`, und `length` allein bedeutet `this.length`.

---

Eine Erweiterungsfunktion kann Parameter haben wie jede andere Funktion. Der Empfänger bleibt links vom Punkt und die Parameter stehen zwischen den Klammern:
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
Der Typ vor dem Punkt ist ein ganz normaler Typ, Sie können also genauso `List<Int>`, `Double` oder eine selbst geschriebene Klasse erweitern.

---

Eine Erweiterung ändert die erweiterte Klasse **nicht** und fügt ihr kein neues Member hinzu. Der Compiler schreibt den Aufruf einfach um: `"kotlin".first3()` wird zu einem Aufruf der Funktion, bei dem `"kotlin"` als `this` übergeben wird.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
Deshalb können Sie finale Klassen wie `String` und `Int` erweitern: in ihnen ändert sich nichts, die Erweiterung lebt nur in Ihrem Code.

---

Neben Funktionen können Sie auch eine **Erweiterungseigenschaft** hinzufügen. Sie wird mit `val`, dem Empfängertyp, einem Punkt und dem Namen deklariert, gefolgt von einem `get()`, das den Wert bei jedem Lesen der Eigenschaft berechnet:
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
Eine Erweiterungseigenschaft kann nichts speichern: sie hat kein Hintergrundfeld, daher ist ein Initialisierer wie `val String.label = "text"` ein Compilerfehler. Sie kann ihren Wert nur aus dem Empfänger berechnen.
Erweiterungseigenschaften können nicht innerhalb einer Funktion deklariert werden (lokale Erweiterungseigenschaften sind nicht erlaubt), anders als Erweiterungsfunktionen.

---

Erweiterungseigenschaften werden ohne Klammern gelesen, genau wie das eingebaute `length` eines `String`. Sie sind die natürliche Wahl, wenn der Wert den Empfänger beschreibt, statt etwas mit ihm zu tun:
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Beachten Sie die Klammern um `-3`: ohne sie würde `-3.isNegative` zuerst die Eigenschaft von `3` lesen und dann versuchen, einen `Boolean` zu negieren, was nicht kompiliert.

---

Der Empfängertyp kann **nullable** sein. Eine Erweiterung für `String?` kann auf einer Variable aufgerufen werden, die `null` enthalten kann, und innerhalb der Funktion ist `this` ein `String?`, sodass Sie den `null`-Fall selbst behandeln, meist mit dem Elvis-Operator `?:` aus den Lektionen zur Nullability:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
`name.orDash()` auf einem `null`-Wert aufzurufen ist sicher: es ist kein `?.` nötig, weil die Funktion selbst einen `null`-Empfänger akzeptiert.

---

Innerhalb einer Erweiterung mit nullable Empfänger können Sie auch den sicheren Aufruf `this?.` verwenden, um die Member des Werts nur dann zu erreichen, wenn er nicht `null` ist. Die Standardbibliothek nutzt dieselbe Idee für Funktionen wie `isNullOrEmpty()`:
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

Wenn eine Klasse bereits ein Member mit demselben Namen und denselben Parametern wie eine Erweiterung hat, **gewinnt immer das Member**: die Erweiterung wird nie aufgerufen, und der Compiler warnt Sie, dass sie verdeckt wird.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
Eine Erweiterung kann bestehendes Verhalten nicht überschreiben oder ersetzen; sie kann nur neue Funktionen und Eigenschaften hinzufügen. Um gewählt zu werden, braucht eine Erweiterung einen Namen oder eine Parameterliste, die die Klasse noch nicht hat.

---

Eine Erweiterung kann dank eines **Typparameters** auf einer ganzen Familie von Typen arbeiten: ein Platzhalter für einen Typ, direkt nach `fun` in spitzen Klammern deklariert, den Kotlin bei jedem Aufruf ausfüllt. Das macht die Erweiterung **generisch**:
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
Bei `listOf(1, 2, 3)` ist der Platzhalter `T` gleich `Int`, bei `listOf("a", "b")` ist er `String`, sodass dieselbe Funktion jedes Mal den richtigen Typ zurückgibt.

---

Der Typparameter kann überall in der Signatur verwendet werden: als Rückgabetyp, als nullable `T?` oder innerhalb eines anderen Typs. Eine generische Erweiterung, die möglicherweise nichts findet, gibt `T?` zurück, wie das eingebaute `firstOrNull()`:
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Innerhalb der Funktion können Sie `size`, `isEmpty()` und die Indizierung genau wie bei jeder Liste verwenden, denn der Empfänger ist eine `List<T>`.

---

Sie können auch das **Companion Object** einer Klasse erweitern, solange die Klasse eines deklariert, selbst ein leeres. Der Empfängertyp wird als `ClassName.Companion` geschrieben, und die Erweiterung wird dann auf dem Klassennamen aufgerufen, wie eine Factory-Funktion:
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
Die Klasse und die Erweiterung sind beide Deklarationen auf oberster Ebene, sie müssen also außerhalb von `main` geschrieben werden.

---

Eine Companion-Erweiterung kann Parameter haben, was sie zu einem praktischen Ort für alternative Konstruktoren macht, die aus einer anderen Einheit oder einem anderen Format umrechnen:
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

Wo Sie eine Erweiterung deklarieren, entscheidet darüber, wo sie verwendet werden kann, ihr **Gültigkeitsbereich**:
- auf oberster Ebene einer Datei ist sie in der ganzen Datei und im restlichen Package verfügbar
- innerhalb einer Funktion ist sie eine lokale Erweiterung, nur in dieser Funktion verwendbar
- innerhalb einer Klasse ist sie eine **Member-Erweiterung**, nur innerhalb dieser Klasse verwendbar

Eine Member-Erweiterung kann die Eigenschaften der Klasse lesen, in der sie lebt, sie kombiniert also zwei Empfänger: die Instanz der Klasse und den Wert, auf dem sie aufgerufen wird:
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Innerhalb von `greet` kommt `greeting` vom `Greeter` und `this` ist der `String`, auf dem die Funktion aufgerufen wird. Außerhalb der Klasse ist `"Ada".greet()` ein Compilerfehler.

---

Eine Erweiterungsfunktion mit genau **einem** Parameter kann als `infix` markiert werden. Eine Infix-Funktion kann ohne Punkt und Klammern aufgerufen werden, mit dem Empfänger links und dem Argument rechts, was sich fast wie ein Satz liest:
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin nutzt das auch für einige eingebaute Funktionen: `1 to "one"` baut ein `Pair`, und `1 until 5` baut einen Bereich.

---

Um als `infix` markiert werden zu können, muss eine Funktion ein Member oder eine Erweiterung sein, genau einen Parameter haben, und dieser Parameter darf keinen Standardwert haben. Alles andere ist ein Compilerfehler:
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Infix-Aufrufe liegen in der Priorität zwischen Arithmetik und Vergleich: `1 add 2 * 3` ist `1 add 6`, während `1 add 2 == 3` das Ergebnis mit `3` vergleicht.
