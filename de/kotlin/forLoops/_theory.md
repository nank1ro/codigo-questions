> Das `for`-Schlüsselwort führt einen Codeblock für jeden Wert in einer Sequenz aus.

Die `for`-Schleife iteriert durch alles, das einen Iterator bereitstellt.

Die Syntax von `for` ist folgende:
```kotlin
for (item in collection) print(item)
```

Der Text von `for` kann auch ein Block sein
```kotlin
for (item in collection) {
    print(item)
}
```

Jedes Mal durch die Schleife erhält `item` das nächste Element in den Werten.

Hier ist eine `for`-Schleife, die eine Aktion eine feste Anzahl von Malen wiederholt:

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

Die Ausgabe zeigt den Index `i`, der jeden Wert im Bereich von _1_ bis _3_ erhält.

---

Ein _range_ ist ein Werteintervall, das durch ein Paar von Endpunkten definiert wird.
Es gibt zwei grundlegende Möglichkeiten, Bereiche zu definieren:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ Mit der `..`-Syntax werden beide Grenzen in den resultierenden Bereich einbezogen.
- __[2]__ `until` schließt das Ende aus. Die Ausgabe zeigt, dass _3_ nicht Teil des Bereichs ist.

---

Sie können über einen Bereich in umgekehrter Reihenfolge iterieren.

Sie werden wahrscheinlich erwarten, dass `3..1` funktioniert, aber leider hat das Kotlin-Team beschlossen, diese Funktionalität auf andere Weise zu importieren.

Wenn Sie diesen Code-Schnipsel tatsächlich ausführen:
```kotlin
for (i in 3..1) println(i)
```

Sie werden sehen, dass nichts gedruckt wird.
Um es funktionsfähig zu machen, müssen wir das `downTo`-Schlüsselwort verwenden:

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo` erzeugt einen abnehmenden Bereich.

---

Der Standard _step_ eines Bereichs ist __1__, aber Sie können explizit einen anderen Wert einstellen.

Sie können den __step__ Ihrer `for`-Schleife mit dem `step`-Schlüsselwort definieren.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

Wie Sie sehen, wird der Code-Block mit einem Schritt von _2_ statt _1_ ausgeführt und ändert unsere Ausgabe vollständig.

---

Sie können auch einen Bereich von _Zeichen_ erzeugen.
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

Sie können über einen __String__ iterieren.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

Im obigen Beispiel haben wir jeden Buchstaben + 1 gedruckt, also wird `'a'` zu `'b'`, `'b'` wird zu `'c'` und so weiter.

Dies ist möglich, da Zeichen als Zahlen gespeichert werden, die ihren [ASCII-Codes](https://en.wikipedia.org/wiki/ASCII) entsprechen.

Das Addieren einer Ganzzahl zu einem Zeichen erzeugt also ein neues Zeichen, das dem neuen Codewert entspricht.

---

Falls Sie einfach einen Code-Block `n`-mal wiederholen müssen, können Sie die `repeat(times: Int)`-Funktion verwenden.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

Sie können sogar auf den Index zugreifen mit
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

In Kotlin können wir auch `for-in` für iterierbare Sammlungen verwenden und die gegebene Schließung auf jedem Element aufrufen:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10) 
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

In Kotlin haben wir auch die `forEach`-Schleife.
Sie ruft die gegebene Schließung auf jedem Element in der Sequenz in der gleichen Reihenfolge wie eine `for-in`-Schleife auf:

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9) 
numbers.forEach {
    println(it)
}
```

Die Verwendung der `forEach`-Methode unterscheidet sich auf zwei wichtige Weise von einer `for-in`-Schleife:
1. Die Anweisung `break` oder `continue` kann nicht verwendet werden, um den aktuellen Aufruf der Body-Closure zu beenden oder nachfolgende Aufrufe zu überspringen. (_Eigentlich ist es mit Anmerkungen möglich, aber es ist ein etwas komplexeres Thema, das wir jetzt nicht sehen werden._)
2. Die Verwendung der `return`-Anweisung in der Body-Closure beendet nur die Schließung und nicht den äußeren Bereich, und es werden keine nachfolgenden Aufrufe übersprungen.
