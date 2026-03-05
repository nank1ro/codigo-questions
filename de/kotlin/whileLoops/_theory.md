> Computer sind ideal für sich wiederholende Aufgaben.

Die grundlegendste Form der Wiederholung verwendet das `while`-Schlüsselwort.
Dies wiederholt einen Block, solange der steuernde _boolesche Ausdruck_ wahr ist:

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
Der boolesche Ausdruck wird einmal am Anfang der Schleife und vor jeder weiteren Iteration durch den Block bewertet.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Hier haben wir eine Variable `x` erstellt und ihr den Anfangswert __3__ zugewiesen.

Dann haben wir die `while`-Anweisung verwendet, die den Code-Block ausführt, bis die Bedingung `x > 0` `true` ist.

Innerhalb des Code-Blocks sollten wir **nicht** vergessen, die Zeile `x--` hinzuzufügen.
Sie dekrementiert den `x`-Wert, sonst ist unsere Schleife unendlich.

---

Lassen Sie uns diesen Code-Ausschnitt analysieren.
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__: Wir initialisieren die `counter`-Variable auf __0__.
- __[2]__: Der bedingte Ausdruck für den _while_ sagt: "Wiederholen Sie die Anweisungen im Body, solange der Zähler kleiner als _100_ ist".
- __[3]__: Der `+=`-Operator addiert _10_ zu `counter` und weist das Ergebnis in einer einzigen Operation zu.

Die Ausgabe des obigen Codes ist _10_, _20_, _30_, _40_, _50_, _60_, _70_, _80_, _90_, _100_

---

Es gibt eine zweite Möglichkeit, _while_ in Verbindung mit dem `do`-Schlüsselwort zu verwenden.
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
Wie Sie sehen, ist die `do-while`-Schleife der `while`-Schleife sehr ähnlich, mit einem wichtigen Unterschied:
> Der Body der Schleife wird einmal ausgeführt, bevor die Bedingung bewertet wird.

Mit anderen Worten, der Body der `do-while`-Schleife wird immer mindestens einmal ausgeführt, auch wenn der bedingte Ausdruck anfangs `false` ergibt.

Im Gegensatz dazu wird der Body einer `while`-Schleife nie ausgeführt, wenn die Bedingung beim ersten Mal `false` ergibt.

---

Die _while_-Schleife unterstützt drei strukturelle Sprungausdrücke:
- `break` beendet die nächste einschließende Schleife.
- `continue` geht zum nächsten Schritt der nächsten einschließenden Schleife.
- `return` gibt standardmäßig von der nächsten einschließenden Funktion oder anonymen Funktion zurück (_wir werden dies später sehen, wenn wir über Funktionen sprechen_).

Hier ist ein Beispiel für die Verwendung von `continue` in einer _while_-Schleife:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

Wie Sie sehen können, überspringen wir bei __[1]__, wenn `i` gleich _2_ ist, und _continue_ zum nächsten Schritt. Tatsächlich wird die Zahl 2 niemals gedruckt.

---

Hier ist ein Beispiel für die Verwendung von `break` in einer _while_-Schleife:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

Wie Sie sehen können, beenden wir bei __[1]__, wenn `i` gleich _2_ ist, die Schleife. Tatsächlich werden die Zahlen 2 und 3 niemals gedruckt.
