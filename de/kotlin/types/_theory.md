Jeder Wert in Kotlin hat einen **Typ**, der dem Compiler sagt, um welche Art von Daten es sich handelt und was Sie damit tun können.
Die grundlegenden Typen sind:
- `Int`: eine ganze Zahl, wie `42` oder `-7`
- `Long`: eine ganze Zahl, die viel größer als ein `Int` sein kann
- `Double`: eine Zahl mit einem Dezimalteil, wie `3.14`
- `Float`: eine Dezimalzahl, die halb so viel Speicher wie ein `Double` verwendet, aber weniger präzise ist
- `Char`: ein einzelnes Zeichen zwischen einfachen Anführungszeichen, wie `'a'`
- `Boolean`: entweder `true` oder `false`
- `String`: ein Text zwischen doppelten Anführungszeichen, wie `"Hello"`

Wie Sie in den Variablen-Lektionen gesehen haben, können Sie den Typ explizit mit einem Doppelpunkt nach dem Namen angeben:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
Ein Wert eines Typs kann nicht in einer Variable eines anderen Typs gespeichert werden: `val age: Int = "36"` ist ein Kompilierungsfehler.

---

In den meisten Fällen schreiben Sie den Typ nicht: Kotlin **leitet** ihn aus dem Wert ab, den Sie zuweisen, und folgt dabei einigen Regeln für Literale:
- eine ganze Zahl, wie `42`, ist ein `Int`
- eine Zahl mit Dezimalpunkt, wie `3.14`, ist ein `Double`
- Text zwischen doppelten Anführungszeichen ist ein `String`
- ein Zeichen zwischen einfachen Anführungszeichen ist ein `Char`
- `true` und `false` sind `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Um zu prüfen, was Kotlin abgeleitet hat, können Sie den Namen des Typs eines beliebigen Werts mit `::class.simpleName` ausgeben:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
Ein Dezimalliteral wird nie als `Float` abgeleitet: `val ratio = 0.5` ist ein `Double`.

---

Ein `Int` kann ganze Zahlen bis etwa zwei Milliarden aufnehmen, genauer gesagt bis `Int.MAX_VALUE`, das `2147483647` ist.
Ein Ganzzahl-Literal, das zu groß für ein `Int` ist, wird automatisch als `Long` abgeleitet, und Sie können mit dem Suffix `L` für jedes Literal ein `Long` erzwingen:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
Auf dieselbe Weise macht das Suffix `f` aus einem Dezimalliteral ein `Float`: `val ratio = 0.5f`.
Lange Zahlen sind schwer zu lesen, daher können Sie in Kotlin Unterstriche `_` an beliebiger Stelle zwischen den Ziffern setzen; der Compiler ignoriert sie:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin konvertiert beim Zuweisen eines Werts nie von selbst zwischen Zahlentypen, nicht einmal von einem kleineren zu einem größeren Typ: Das Speichern eines `Int` in einer `Long`- oder `Double`-Variable ist ein Kompilierungsfehler.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Jeder Zahlentyp hat **Konvertierungsfunktionen**, die einen neuen Wert des gewünschten Typs erzeugen: `toInt()`, `toLong()`, `toDouble()`, `toFloat()` und, um Text zu erhalten, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Der Übergang von einer Dezimalzahl zu einer ganzen Zahl **schneidet ab**: `toInt()` verwirft einfach den Dezimalteil, sodass `3.99.toInt()` `3` ist und `(-3.99).toInt()` `-3`.

---

Die Typen der Operanden entscheiden, wie die Division funktioniert. Wenn beide `Int` sind, führt der Operator `/` eine **Ganzzahldivision** durch: Das Ergebnis ist ein `Int` und der Rest wird verworfen.
Wenn mindestens ein Operand ein `Double` ist, führt `/` eine Fließkommadivision durch und behält den Dezimalteil:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
Um also aus zwei `Int`-Variablen ein Dezimalergebnis zu erhalten, müssen Sie mindestens eine davon **vor** der Division konvertieren: `(7 / 2).toDouble()` ist `3.0`, weil die Ganzzahldivision bereits stattgefunden hat.

---

Wenn eine Funktion ein Dezimalergebnis aus ganzen Zahlen berechnen muss, konvertieren Sie die Operanden vor der Division in `Double` und deklarieren Sie den Rückgabetyp als `Double`:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Denken Sie daran, dass `sum()` und `size` einer `List<Int>` ebenfalls `Int`-Werte sind, sodass sie dieselbe Konvertierung brauchen.

---

Jedes `Char` wird als Zahl gespeichert, sein **Code**. Die Eigenschaft `code` liefert das `Int` hinter einem Zeichen, und `toChar()` macht das Gegenteil und verwandelt ein `Int` in das `Char` mit diesem Code:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
Buchstaben haben aufeinanderfolgende Codes, daher bewegt Sie das Addieren zum Code entlang des Alphabets.
Beachten Sie, dass der Code von `'7'` `55` ist, nicht `7`: Um die Ziffer zu lesen, die ein `Char` darstellt, verwenden Sie `digitToInt()`, das `7` zurückgibt.

---

Da der Code eines `Char` ein `Int` ist, können Sie damit rechnen und das Ergebnis zurück in ein `Char` konvertieren. So bewegen Sie sich entlang des Alphabets:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin erlaubt es auch, ein `Int` direkt zu einem `Char` zu addieren: `'a' + 1` ist `'b'`, und die Differenz zwischen zwei Zeichen `'d' - 'a'` ist das `Int` `3`.

---

Von einem Benutzer eingegebener Text kommt immer als `String` an, selbst wenn er wie eine Zahl aussieht. Um damit zu rechnen, müssen Sie ihn **parsen**: `toInt()` macht aus `"42"` das `Int` `42`, und `toDouble()` macht aus `"3.5"` das `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
Nicht jeder Text ist eine Zahl: `"4x2".toInt()` löst eine `NumberFormatException` aus und stoppt das Programm.
Die sicheren Alternativen `toIntOrNull()` und `toDoubleOrNull()` geben `null` zurück, statt eine Ausnahme auszulösen, sodass Sie, wie Sie in den Nullability-Lektionen gelernt haben, mit `?:` einen Standardwert angeben können:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` gelingt nur, wenn der gesamte Text eine gültige ganze Zahl mit optionalem Vorzeichen ist:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
Für Dezimaltext gibt es `toDoubleOrNull()`, das auf dieselbe Weise `"3.5"` akzeptiert und ein `Double?` zurückgibt.

---

Ein `Int` hat eine feste Größe, daher hat es einen kleinsten und einen größten Wert: `Int.MIN_VALUE` ist `-2147483648` und `Int.MAX_VALUE` ist `2147483647`.
Das Überschreiten der Grenze löst **keinen** Fehler aus: Der Wert springt still zum anderen Ende des Bereichs, ein Verhalten, das Overflow genannt wird.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
Wenn ein Ergebnis zwei Milliarden überschreiten kann, verwenden Sie ein `Long`, dessen Grenze `Long.MAX_VALUE` etwa neun Trillionen beträgt. Denken Sie daran, vor der Operation zu konvertieren: `Int.MAX_VALUE.toLong() + 1` ist `2147483648`.

---

Ein `Double` speichert Dezimalzahlen im Binärsystem, daher können manche Werte nicht exakt dargestellt werden und kleine Fehler erscheinen in den letzten Ziffern:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
Um eine feste Anzahl von Dezimalstellen anzuzeigen, verwenden Sie `String.format` mit einem Formatstring: `"%.2f"` bedeutet "eine Dezimalzahl mit 2 Ziffern nach dem Punkt". Das Ergebnis ist ein `String`, auf so viele Ziffern gerundet:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` ist der Typ an der Spitze der Hierarchie: Jeder Kotlin-Wert ist ein `Any`, daher kann eine Variable vom Typ `Any` ein `Int`, ein `String`, ein `Boolean` oder alles andere enthalten.
Um herauszufinden, was sie tatsächlich enthält, verwenden Sie den Operator `is`, der `true` zurückgibt, wenn der Wert diesen Typ hat:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Sobald eine Prüfung bestanden ist, führt der Compiler einen **Smart Cast** des Werts durch: Innerhalb des `if` (oder des `when`-Zweigs) können Sie ihn als diesen Typ verwenden, ganz ohne Konvertierung:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
