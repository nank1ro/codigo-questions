**Scope-Funktionen** führen einen Codeblock *im Kontext eines Objekts* aus. Sie fügen der Sprache keine neuen Funktionen hinzu: Sie machen Code, der mit einem Objekt arbeitet, nur kürzer und leichter lesbar. Kotlin hat fünf davon: `let`, `run`, `with`, `apply` und `also`.

Sie unterscheiden sich nur in **zwei** Punkten: wie das Objekt innerhalb des Blocks referenziert wird und was der Aufruf zurückgibt. Wir beginnen mit `let`: Innerhalb seines Blocks heißt das Objekt `it`, und der Aufruf gibt das **Ergebnis des letzten Ausdrucks** des Blocks zurück.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Ohne `let` bräuchten Sie eine temporäre Variable; mit `let` steht das Objekt unter dem kurzen Namen `it` zur Verfügung, solange der Block andauert.

---

Da `let` den Wert seines letzten Ausdrucks zurückgibt, ist es eine praktische Möglichkeit, einen **Wert in etwas anderes umzuwandeln**, ohne eine Zwischenvariable zu benennen:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Innerhalb des Blocks können Sie `it` so oft verwenden, wie Sie brauchen:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` wird nach einem sicheren Aufruf richtig nützlich. `?.let { ... }` führt den Block **nur** aus, wenn der Wert nicht `null` ist, und innerhalb des Blocks ist `it` ein Nicht-null-Wert, sodass keine zusätzliche Prüfung nötig ist:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
Wenn der Wert `null` ist, ist der ganze Ausdruck `null` und der Block wird nie ausgeführt; daher ist der Elvis-Operator `?:` der natürliche Partner, um einen Ersatz zu liefern:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Innerhalb eines `let`-Blocks müssen Sie das Objekt nicht `it` nennen: Sie können dem Lambda-Parameter einen Namen geben, was den Code lesbar hält, wenn Blöcke verschachtelt sind oder wenn `it` nichts Aussagekräftiges sagen würde.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
Dieselbe Benennung funktioniert bei jeder Scope-Funktion, die `it` verwendet, also bei `let` und `also`.

---

`apply` geht auf beiden Achsen gleichzeitig weiter: Innerhalb seines Blocks ist das Objekt der Empfänger `this` (sodass seine Member **ohne jedes Präfix** verwendet werden können), und der Aufruf gibt **das Objekt selbst** zurück, nicht das Ergebnis des Blocks.

Diese Kombination macht `apply` zum Werkzeug, um ein Objekt genau dort zu **konfigurieren**, wo Sie es erstellen:
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
`host` und `port` innerhalb des Blocks sind `this.host` und `this.port`; da `apply` den konfigurierten `Server` zurückgibt, kann er direkt zugewiesen werden.

---

`apply` ist nicht auf Objekte beschränkt, die Sie gerade erstellt haben: Es funktioniert auf jedem Objekt, und da es das Objekt zurückgibt, können Sie den ganzen Ausdruck überall dort verwenden, wo das Objekt erwartet wird.
```kotlin
val box = Box()
box.apply { label = "tools" }        // verändert box und gibt es zurück
println(listOf(Box().apply { label = "nails" }).size) // 1
```
Der Block ist ein normaler Codeblock, daher kann er so viele Anweisungen enthalten, wie Sie brauchen.

---

`also` ist das Spiegelbild von `apply`: Das Objekt wird als `it` referenziert, und der Aufruf gibt **das Objekt selbst** zurück. Da das Ergebnis des Blocks weggeworfen wird, ist `also` für **Nebeneffekte** wie Logging oder Prüfen gedacht, und es kann mitten in einer Kette eingefügt werden, ohne zu ändern, was die Kette erzeugt:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Lesen Sie es als *„und mache auch noch dies damit*“: der Wert fließt unangetastet zum nächsten Schritt weiter.

---

Wenn der Block das Objekt als **Argument** von etwas anderem braucht, liest sich `also` besser als `apply`: `it` kann direkt weitergegeben werden, während `this` ausgeschrieben werden müsste.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
Der Wert des Ausdrucks ist immer noch `"ada"`: `also` sieht nur zu, wie er vorbeizieht.

---

`run` ist `let` mit der anderen Art, das Objekt zu benennen: Innerhalb des Blocks ist das Objekt `this`, sodass seine Member kein Präfix brauchen, und der Aufruf gibt das **Ergebnis des letzten Ausdrucks** zurück.

Es passt, wenn Sie mehrere Member desselben Objekts lesen, um einen Wert zu berechnen:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Vergleichen Sie es mit `apply`, das `this` auf genau dieselbe Weise verwendet, aber das Objekt statt des Ergebnisses des Blocks zurückgibt.

---

`with` macht dieselbe Arbeit wie `run`, ist aber **keine** Erweiterung: Das Objekt wird als erstes Argument übergeben, statt der Empfänger eines Punkt-Aufrufs zu sein.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Innerhalb des Blocks ist das Objekt `this` und der Aufruf gibt den letzten Ausdruck zurück, genau wie `run`. Bevorzugen Sie `with`, wenn Sie bereits ein Nicht-null-Objekt haben und mehrere Aufrufe darauf bündeln wollen; bevorzugen Sie `run`, wenn das Objekt aus einer Kette kommt oder einen sicheren Aufruf brauchen könnte (`obj?.run { ... }`).

---

Alle fünf Scope-Funktionen sind jetzt auf dem Tisch, und jede ist nur ein Punkt auf den beiden Achsen:
- `let` - das Objekt ist `it`, gibt das Ergebnis des Blocks zurück
- `run` - das Objekt ist `this`, gibt das Ergebnis des Blocks zurück
- `with` - das Objekt ist `this` (als Argument übergeben), gibt das Ergebnis des Blocks zurück
- `apply` - das Objekt ist `this`, gibt das Objekt zurück
- `also` - das Objekt ist `it`, gibt das Objekt zurück

Wählen Sie die Zeile, die Sie brauchen: `it` liest sich besser, wenn Sie das Objekt an etwas anderes weitergeben, `this` liest sich besser, wenn Sie viele seiner Member anfassen; geben Sie das Ergebnis des Blocks zurück, wenn Sie einen neuen Wert wollen, und das Objekt, wenn Sie weiter damit arbeiten wollen.
