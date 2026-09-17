Eine **Exception** ist die Art von Kotlin zu melden, dass eine Anweisung nicht ausgeführt werden kann. Die Umwandlung von `"abc"` in eine Zahl, die Division einer ganzen Zahl durch null oder das Lesen hinter das Ende einer Liste lösen jeweils eine aus.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Dieses Programm gibt `before` aus und stoppt dann. `toInt()` kann `"abc"` nicht lesen, also **löst** es eine `NumberFormatException` aus; nichts im Programm kümmert sich darum, also beendet Kotlin das Programm mit einer Fehlermeldung und `after` wird nie ausgegeben.

Sie können auch selbst eine Exception mit dem Schlüsselwort `throw` auslösen:
```kotlin
throw Exception("something went wrong")
```

Eine Exception, die niemand behandelt, ist keine Warnung: Sie ist das Ende des Programmlaufs.

---

Um das Programm am Laufen zu halten, setzen Sie die riskante Anweisung in einen `try`-Block und beschreiben Sie die Wiederherstellung in einem `catch`-Block:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin führt den `try`-Block aus; sobald eine Anweisung darin eine Exception auslöst, wird der Rest des Blocks übersprungen und die Kontrolle springt zum `catch`-Block. Der Name in den Klammern — hier `e` — ist das Exception-Objekt, und `Exception` ist der Typ, der abgefangen wird.

Sobald der `catch`-Block fertig ist, fährt das Programm normal mit der Zeile nach dem gesamten `try`/`catch` fort.

---

Wenn Sie `Exception` abfangen, fangen Sie alles ab — was selten das ist, was Sie wollen: Auch ein Tippfehler an anderer Stelle im Block würde verschluckt. Geben Sie stattdessen den **genauen Typ** an, von dem Sie wissen, wie Sie sich davon erholen können.

Jeder Fehler hat seinen eigenen Typ. `"abc".toInt()` löst eine `NumberFormatException` aus, also ist das der Typ, der abgefangen werden muss:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Wird innerhalb des Blocks eine andere Art von Exception ausgelöst, passt dieses `catch` nicht, und die Exception reist weiter aus der Funktion hinaus.

---

Auf ein `try` können mehrere `catch`-Blöcke folgen, von denen jeder einen anderen Typ behandelt:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin probiert die Blöcke **von oben nach unten** durch und führt den ersten aus, dessen Typ passt. Es läuft immer nur ein Block.

Deshalb ist die Reihenfolge wichtig. `NumberFormatException` und `IndexOutOfBoundsException` sind beides Arten von `Exception`, sodass ein zuerst geschriebenes `catch (e: Exception)` auf jeden Fehler passen würde und die Blöcke darunter nie ausgeführt würden. Schreiben Sie den spezifischsten Typ zuerst und den allgemeinsten zuletzt.

---

Ein `finally`-Block kann am Ende ergänzt werden. Er wird **unabhängig davon ausgeführt, was passiert**: nach einem erfolgreichen `try`, nachdem ein `catch` die Exception behandelt hat, und sogar dann, wenn die Exception gar nicht abgefangen wird.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
Das macht ihn zum Ort für Aufräumarbeiten, die nicht übersprungen werden dürfen, etwa das Schließen einer Datei. Ein `try` braucht mindestens ein `catch` oder ein `finally`, darf aber auch beides haben.

---

In Kotlin ist `try` nicht nur eine Anweisung: Es ist ein **Ausdruck**, der einen Wert liefert. Der Wert ist der letzte Ausdruck des Blocks, der ausgeführt wurde — der `try`-Block, wenn nichts fehlgeschlagen ist, der `catch`-Block, wenn doch.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
Das ist die idiomatische Form in Kotlin. Statt eine `var` zu deklarieren, sie an zwei Stellen zuzuweisen und zu hoffen, dass jeder Pfad sie setzt, erhalten Sie ein einziges `val`, das immer einen brauchbaren Wert enthält.

Beachten Sie, dass ein `finally`-Block den Wert nie ändert: Er läuft nur wegen seiner Nebenwirkungen.

---

Da `try` ein Ausdruck ist, kann es überall dort verwendet werden, wo ein Wert erwartet wird — auch als gesamter Funktionskörper einer mit `=` geschriebenen Funktion:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Beide Blöcke müssen einen Wert desselben Typs liefern, hier `Int`. Schreiben Sie den Ersatzwert als letzten Ausdruck in den `catch`-Block; in keinem der beiden Blöcke steht ein `return`.

---

Auslösen und Abfangen ist nicht kostenlos, und für die gängigen Umwandlungen bietet Kotlin eine günstigere Variante, die einfach `null` zurückgibt, statt eine Exception auszulösen: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
In Kombination mit dem Elvis-Operator `?:`, der einen Ersatz liefert, wenn der Wert auf seiner linken Seite `null` ist, schrumpft das gesamte `try`/`catch` auf eine Zeile:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Greifen Sie zu `try`/`catch`, wenn ein Fehler wirklich außergewöhnlich ist; greifen Sie zu `toIntOrNull()`, wenn Sie mit schlechter Eingabe rechnen.

---

Ihre eigenen Funktionen können schlechte Eingaben genauso zurückweisen wie die Standardbibliothek, mit `throw`. Die Bibliothek stellt für den häufigsten Fall bereits einen Typ bereit: `IllegalArgumentException` bedeutet „der Wert, den Sie mir übergeben haben, ist nicht akzeptabel“.

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` beendet die Funktion sofort — das `return` darunter wird nie erreicht. Der Aufrufer entscheidet, was er damit macht:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Auszulösen ist besser, als stillschweigend einen erdachten Wert zurückzugeben: Eine falsche Antwort reist weit, eine Exception stoppt beim ersten Aufrufer, der bereit ist, sie zu behandeln.

---

Jede Exception trägt den Text, mit dem sie erzeugt wurde. Innerhalb eines `catch`-Blocks lesen Sie ihn über die Eigenschaft `message` des Exception-Objekts:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` ist nullable, weil eine Exception auch ohne jeden Text erzeugt werden kann; `e.message ?: "unknown"` liefert einen sicheren Ersatz, wenn Sie einen reinen `String` brauchen.

Geben Sie lieber `e.message` aus als das Exception-Objekt selbst: Der eigene Text des Objekts enthält auch den Klassennamen, und das ist Rauschen für die Person, die die Ausgabe liest.

---

Bei jedem Argument `if (...) throw IllegalArgumentException(...)` zu schreiben wird unübersichtlich, daher bietet Kotlin zwei Kurzformen, die sich wie einfache Sätze lesen:

```kotlin
require(n >= 0) { "n must not be negative" }   // löst IllegalArgumentException aus
check(started) { "not started" }               // löst IllegalStateException aus
```
Beide nehmen eine Bedingung und einen Block entgegen, der die Meldung erzeugt, und beide lösen **aus, wenn die Bedingung falsch ist**. Der einzige Unterschied ist der Exception-Typ, und dieser Unterschied ist eine Botschaft an den Leser:

* `require` bewacht die **Argumente**, die der Aufrufer übergeben hat, und schlägt mit `IllegalArgumentException` fehl.
* `check` bewacht den **Zustand** des Objekts oder Programms und schlägt mit `IllegalStateException` fehl.

Der Block wird nur ausgewertet, wenn die Prüfung fehlschlägt, daher kostet das Erzeugen der Meldung im Erfolgsfall nichts.

---

Wenn keiner der eingebauten Typen Ihren Fehler gut beschreibt, deklarieren Sie Ihren eigenen. Eine Exception ist eine ganz normale Klasse, die `Exception` erweitert und ihren Text an die Oberklasse weiterreicht:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
Diese eine Zeile ist ein vollständiger Exception-Typ. Er wird wie jeder andere ausgelöst und abgefangen, und `e.message` gibt den Text zurück, mit dem er erzeugt wurde:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
Der Gewinn ist Präzision: Ein Aufrufer kann gezielt `InsufficientFundsException` abfangen und jeden anderen Fehler weiterreisen lassen.

---

`runCatching` führt einen Block aus und lässt nie eine Exception entwischen. Stattdessen gibt es ein `Result` zurück, ein Objekt, das **entweder** den Wert enthält, den der Block erzeugt hat, **oder** die Exception, die er ausgelöst hat:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
Der Wert wird danach ausgelesen, und Sie entscheiden, was aus einem Fehler werden soll:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` macht aus einem Fehler `null`, während `getOrElse { ... }` den Block ausführt, um einen Ersatz zu bauen. An der Aufrufstelle wird nichts ausgelöst, daher kann der Fehler herumgereicht und später behandelt werden.

---

Ein `Result` lässt sich auch untersuchen, ohne es auszupacken. `onFailure` führt seinen Block nur aus, wenn das Ergebnis eine Exception enthält, `onSuccess` nur, wenn es einen Wert enthält, und **beide geben dasselbe `Result` zurück**, sodass sich die Aufrufe verketten lassen:

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
Innerhalb des Blocks ist die Exception (oder der Wert) als `it` verfügbar, daher ist `it.message` der Text des Fehlers.

Das ist die Form „melden und weitermachen“: das Problem dort berichten, wo es auftritt, dann weitermachen — ohne ein frühes `return` und ohne eine `var`, die an zwei Stellen gesetzt wird.

---

Wo das `try` steht, entscheidet, wie viel Arbeit ein einziger schlechter Wert vernichtet. Umschließen Sie die **gesamte Schleife**, bricht der erste Fehler den Rest des Stapels ab; umschließen Sie den **Schleifenkörper**, geht nur dieses eine Element verloren:

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // diesen Wert überspringen
    }
}
println(total) // 8
```
Das lässt sich natürlich mit einer validierenden Funktion kombinieren, die auslöst: Die Funktion formuliert eine Regel und weist alles zurück, das sie verletzt, und die Schleife entscheidet, dass eine Zurückweisung nur ein Element kostet.
