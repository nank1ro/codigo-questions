Variablen sind Container zum Speichern von Datenwerten.
Jede Variable in Kotlin ist ein Objekt.
Um eine Variable zu erstellen, müssen wir ihr einen __Namen__ geben, wobei zu beachten ist, dass sie keine Leerzeichen enthalten darf.
Eine Variable wird in dem Moment erstellt, in dem Sie ihr zum ersten Mal einen Wert zuweisen.
In Kotlin deklarieren Sie Konstanten mit dem Schlüsselwort `val` (Kurzform für _value_) und Variablen mit dem Schlüsselwort `var` (Kurzform für _variable_).
Der Wert einer Konstante kann nach dem Setzen nicht mehr geändert werden, während eine Variable zu einem späteren Zeitpunkt auf einen anderen Wert gesetzt werden kann.
Ein Beispiel für die Erstellung einer Variablen mit dem Namen `x` ist:
```kotlin
var x = 1
```
Auf diese Weise haben wir der Variablen `x` den Wert `1` zugewiesen.
Wenn wir die Variable `x` drucken, erhalten wir die Nummer `1` zurück:
```kotlin
println(x) // prints 1
```

---

Variablen werden so genannt, weil sich der Wert, den sie speichern, ändern kann.
Wir können `x` aktualisieren, indem wir `=` verwenden und ihm einen neuen Wert geben.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

Wir können auch Variablen die Werte anderer Variablen zuweisen. Hier können wir der Variablen `y` den Wert von `x` zuweisen.
```kotlin
var x = 5
var y = x
println(y) // prints 5
```

---

Wenn wir eine Variable aktualisieren, vergisst sie ihren vorherigen Wert. Hier können wir die Variable `x` zweimal anzeigen und sehen, wie sich ihr Wert aktualisiert.
```kotlin
var x = 5
println(x) // prints 5
x = 10
println(x) // prints 10
```

---

In Kotlin können Stringvariablen nur mit doppelten Anführungszeichen deklariert werden:
```kotlin
val x = "May"
```

---

Wenn wir einen Variablennamen mit mehreren Wörtern möchten, verwenden wir **camelCase**.
Dies ist die Praxis, Sätze so zu schreiben, dass jedes Wort in der Mitte des Satzes mit einem Großbuchstaben beginnt.
