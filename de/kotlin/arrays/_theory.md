Ein **Array** speichert eine feste Anzahl von Werten desselben Typs unter einem einzigen Variablennamen.
Du erstellst eines mit `arrayOf`, liest ein Element mit eckigen Klammern und einem **Index** ab `0` aus und erhältst die Anzahl der Elemente mit `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
Das letzte Element befindet sich am Index `size - 1`.

---

`arrayOf(1, 2, 3)` erstellt ein `Array<Int>`, bei dem jedes Element ein geboxtes Objekt ist.
Für primitive Typen bietet Kotlin dedizierte, effizientere Typen wie `IntArray`, `DoubleArray` und `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
Du kannst außerdem ein Array einer bestimmten Größe mit einer **Init**-Lambda erstellen, die jeden Index erhält, oder ein mit Nullen gefülltes `IntArray`:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Jedes Array hat zwei praktische Eigenschaften für die Arbeit mit Indizes:
- `indices` ist der Bereich gültiger Indizes, von `0` bis zum letzten
- `lastIndex` ist der Index des letzten Elements, also `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Auch wenn ein Array mit `val` deklariert wird, können seine **Elemente** ersetzt werden, indem man einem Index einen Wert zuweist:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Um jedes Element zu besuchen, kannst du eine `for`-Schleife oder `forEach` verwenden:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Beachte, dass `n` und `it` schreibgeschützte Kopien der Werte sind und nicht neu zugewiesen werden können. Um Elemente zu ändern, brauchst du also ihren Index.

---

Um zu prüfen, ob ein Array einen Wert enthält, verwendest du `in` oder `contains`, beide geben einen `Boolean` zurück.
`indexOf` gibt den Index des ersten Vorkommens zurück, oder `-1`, wenn der Wert nicht vorhanden ist:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Ein Array direkt auszugeben zeigt nicht seine Elemente, sondern etwas wie `[Ljava.lang.String;@1b6d3586`.
Verwende `joinToString`, um eine lesbare Zeichenkette zu erstellen, optional mit einem eigenen Trennzeichen (der Standard ist `", "`), oder `contentToString`, um die Elemente zwischen eckigen Klammern zu erhalten:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Arrays können **an Ort und Stelle** sortiert oder in eine neue sortierte Sammlung kopiert werden:
- `sort()` und `sortDescending()` ordnen das Array selbst neu an und geben nichts zurück
- `reverse()` kehrt die Reihenfolge des Arrays selbst um
- `sorted()`, `sortedDescending()` und `reversed()` lassen das Array unverändert und geben eine neue `List` zurück
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Numerische Arrays verfügen über Aggregatfunktionen:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` und `min()` werfen eine Ausnahme bei einem leeren Array, verwende `maxOrNull()` und `minOrNull()`, wenn das Array leer sein könnte.

---

Der Hauptunterschied zwischen einem Array und einer `MutableList` ist, dass ein Array eine **feste Größe** hat: Einmal erstellt, kannst du seine Elemente ersetzen, aber nie eines hinzufügen oder entfernen, es gibt keine `add`-Funktion.
Ausdrücke wie `nums + 4` lassen `nums` nicht wachsen, sie bauen ein brandneues Array:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Bevorzuge eine `MutableList`, wenn sich die Anzahl der Elemente im Laufe der Zeit ändert, und ein Array, wenn sie von vornherein bekannt ist oder wenn du die Leistung primitiver Typen brauchst.

---

Arrays unterstützen dieselben Transformationsfunktionen wie Listen. `filter` behält die Elemente, die einer Bedingung entsprechen, und `map` wandelt jedes Element um.
Beide geben eine neue `List` zurück, kein Array:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Da das Ergebnis eine Liste ist, zeigt eine direkte Ausgabe ihre Elemente an.

---

Wenn du beim Durchlaufen sowohl den Index als auch den Wert brauchst, verwende `withIndex()` und destrukturiere jedes Paar, oder `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Arrays und Listen lassen sich leicht ineinander umwandeln:
- `toList()` und `toMutableList()` kopieren ein Array in eine Liste
- `toTypedArray()` kopiert eine Liste in ein `Array<T>`
- `toIntArray()` kopiert eine Liste von `Int` in ein `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Jede Umwandlung erstellt eine **Kopie**, sodass eine Änderung des Ergebnisses das Original nicht beeinflusst.

---

Anders als bei Listen sind zwei Arrays mit denselben Elementen mit `==` **nicht** gleich: Arrays werden per Referenz verglichen, also ist `==` nur `true`, wenn es sich um dasselbe Array-Objekt handelt.
Um die Inhalte zu vergleichen, verwende `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Da Arrays eine feste Größe haben, bedeutet das Herausnehmen eines Teils, ein neues Array zu erstellen:
- `copyOf()` kopiert das gesamte Array, `copyOf(n)` kopiert die ersten `n` Elemente
- `copyOfRange(from, to)` kopiert die Elemente vom Index `from` bis `to` **ausschließlich**
- `sliceArray(range)` kopiert die Elemente an den Indizes des Bereichs, beide Enden eingeschlossen
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
