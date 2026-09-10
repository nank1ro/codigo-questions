Eine **Methode höherer Ordnung** ist eine Methode, die eine Funktion als Argument nimmt. Kotlin-Collections bieten viele davon, und die Funktion, die du übergibst, ist meistens ein **Lambda**: eine kleine anonyme Funktion, die zwischen geschweiften Klammern steht.
`map` ist die häufigste: Sie ruft das Lambda für jedes Element auf und gibt eine **neue Liste** mit den Ergebnissen zurück, während das Original unverändert bleibt:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
Wenn das Lambda einen einzigen Parameter hat, musst du ihn nicht deklarieren: Kotlin nennt ihn `it`. Das Lambda wird nach dem Methodennamen geschrieben, außerhalb der runden Klammern, die weggelassen werden können, wenn das Lambda das einzige Argument ist. Das ist die **Trailing-Lambda**-Syntax, und sie wird in jeder Übung dieses Themas verwendet.

---

`filter` nimmt ein Lambda, das einen `Boolean` zurückgibt, ein sogenanntes **Prädikat**, und gibt eine neue Liste nur mit den Elementen zurück, für die das Prädikat `true` ist:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
Statt `it` kannst du dem Parameter einen Namen geben, gefolgt von einem Pfeil `->`. Ein benannter Parameter macht längere Lambdas lesbarer, und er ist nötig, wenn ein Lambda in einem anderen verschachtelt ist, weil das innere `it` das äußere Element verdeckt:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` führt das Lambda einmal für jedes Element aus und gibt nichts zurück. Es ist die Alternative höherer Ordnung zur `for`-Schleife und wird für Seiteneffekte wie das Ausgeben verwendet:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` gibt dir zusätzlich die Position jedes Elements. Sein Lambda hat **zwei** Parameter, also müssen sie benannt werden: `it` existiert nur für Lambdas mit genau einem Parameter.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, dann 1: b
}
```

---

`reduce` fasst alle Elemente zu einem einzigen Wert zusammen. Sein Lambda nimmt zwei Parameter: den **Akkumulator** (das bisherige Ergebnis) und das nächste Element. Es startet mit dem ersten Element als Akkumulator und führt das Lambda für jedes weitere Element aus:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` wirft bei einer leeren Liste eine Exception, weil es kein erstes Element gibt, mit dem es starten könnte. `fold` löst das: Du übergibst den **Startwert** des Akkumulators als Argument, und das Lambda läuft für jedes Element, auch für das erste:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
Mit `fold` kann der Akkumulator sogar einen anderen Typ als die Elemente haben, etwa um aus einer Zahlenliste einen `String` aufzubauen.

---

Manche Methoden höherer Ordnung beantworten eine Frage über die Collection, statt eine neue aufzubauen. Sie alle nehmen ein Prädikat:
- `any` gibt `true` zurück, wenn **mindestens ein** Element es erfüllt
- `all` gibt `true` zurück, wenn **jedes** Element es erfüllt
- `none` gibt `true` zurück, wenn **kein** Element es erfüllt
- `count` gibt zurück, **wie viele** Elemente es erfüllen
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
Bei einer leeren Liste gibt `any` `false` zurück, während `all` und `none` `true` zurückgeben: Es gibt kein Element, das die Regel bricht.

---

Aggregationsmethoden verwandeln eine ganze Collection in einen einzigen Wert:
- `sum()` addiert eine Liste von Zahlen, während `sumOf` den Wert addiert, den das Lambda für jedes Element berechnet
- `maxByOrNull` und `minByOrNull` geben das **Element** zurück, für das das Lambda den größten oder kleinsten Wert liefert, oder `null` bei einer leeren Liste
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Beachte den Unterschied zu `maxOf { it.length }`, das den größten **Wert** (`6`) zurückgibt statt des Elements, das ihn erzeugt hat.

---

`sortedBy` gibt eine neue Liste zurück, sortiert nach dem Wert, den das Lambda für jedes Element berechnet, vom kleinsten aufwärts. `sortedByDescending` sortiert vom größten abwärts. Wenn die Elemente selbst verglichen werden sollen, brauchen `sorted()` und `sortedDescending()` kein Lambda:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
Die Sortierung ist **stabil**: Elemente mit demselben Schlüssel behalten ihre ursprüngliche relative Reihenfolge. Die ursprüngliche Liste wird nie verändert.

---

`take(n)` gibt eine neue Liste mit den ersten `n` Elementen zurück, und `drop(n)` gibt eine neue Liste **ohne** die ersten `n` Elemente zurück. Keine der beiden nimmt ein Lambda, aber sie werden oft an eine Methode angehängt, die eines nimmt:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` und `dropWhile` sind die Versionen mit einem Prädikat: Sie nehmen oder verwerfen Elemente vom Anfang an, **solange** das Prädikat `true` ist, und stoppen beim ersten Element, das es nicht erfüllt:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` teilt eine Collection in eine `Map` auf: Das Lambda berechnet den **Schlüssel** jedes Elements, und jedem Schlüssel wird die Liste der Elemente zugeordnet, die ihn erzeugt haben, in ihrer ursprünglichen Reihenfolge:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
Das Ergebnis hat den Typ `Map<K, List<T>>`, wobei `K` der vom Lambda zurückgegebene Typ ist und `T` der Typ der Elemente. Die Schlüssel erscheinen in der Reihenfolge, in der sie zuerst auftreten.

---

Wenn das Lambda für jedes Element eine **Liste** zurückgibt, erzeugt `map` eine Liste von Listen. `flatMap` macht dasselbe, fügt danach aber all diese Listen zu einer einzigen flachen Liste zusammen:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
Die Reihenfolge bleibt erhalten: Zuerst kommen alle Werte, die das erste Element erzeugt hat, dann die des zweiten und so weiter. Wenn du bereits eine Liste von Listen hast, fügt `flatten()` sie ohne Lambda zusammen.

---

`zip` paart die Elemente zweier Listen Position für Position. Ohne Lambda gibt es eine Liste von `Pair`-Werten zurück, deren Hälften mit `.first` und `.second` gelesen werden; mit einem Lambda werden ihm die beiden Elemente jeder Position übergeben und die Ergebnisse in einer Liste gesammelt:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
Das Ergebnis ist so lang wie die **kürzere** der beiden Listen: Überzählige Elemente der längeren werden ignoriert.

---

Die Form des Lambdas muss zu dem passen, was die Methode erwartet:
- Methoden, die mit einem Element auf einmal arbeiten (`map`, `filter`, `sortedBy`, `groupBy`...), nehmen ein Lambda mit **einem Parameter**, in dem `it` verfügbar ist
- `reduce`, `fold`, `forEachIndexed` und `zip` mit einem Lambda übergeben **zwei** Werte, also müssen die Parameter mit `a, b ->` explizit benannt werden
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: ein Parameter, it ist verfügbar
numbers.reduce { acc, n -> acc + n }    // ok: zwei Parameter, benannt
numbers.reduce { it + 1 }               // Fehler: it existiert bei zwei Parametern nicht
```
Die Parameter zu benennen ist immer erlaubt, auch bei einem einzigen: `numbers.map { n -> n * 2 }`.

---

Methoden höherer Ordnung können **verkettet** werden: Jede gibt eine neue Collection zurück, mit der die nächste arbeitet, sodass sich eine ganze Berechnung wie eine Pipeline von links nach rechts liest:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Auch Maps haben Methoden höherer Ordnung. `mapValues` behält die Schlüssel und ersetzt jeden Wert durch das Ergebnis des Lambdas, das den **Eintrag** mit `.key` und `.value` erhält:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

In einer Kette ändert sich der Typ von `it` bei jedem Schritt: Nach `filter` auf einer `List<String>` hast du weiterhin Strings, aber nach `map { it.length }` hast du eine `List<Int>`, also sieht das nächste Lambda Zahlen.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Jeder Schritt gibt eine **neue** Liste zurück und rührt die vorherige nie an, also lässt sich eine Kette in benannte Zwischenwerte aufteilen, ohne das Ergebnis zu ändern.

---

Ein Lambda kann einen weiteren Aufruf höherer Ordnung enthalten. Innerhalb des inneren Lambdas bezieht sich `it` auf das **innere** Element und verdeckt das äußere, also benenne den äußeren Parameter explizit, damit beide erreichbar bleiben:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` erzeugt ein `Pair`. Hier arbeitet das äußere Lambda mit einem Map-Eintrag, während das innere mit den Paaren aus der Liste dieses Eintrags arbeitet.

---

Eine `Map` kann wie eine Liste von Einträgen verarbeitet werden: `filter` und `map` arbeiten direkt auf der Map und erhalten jeden Eintrag mit `.key` und `.value`. `filter` auf einer Map gibt eine Map zurück, während `map` eine Liste zurückgibt. Sortiermethoden wie `sortedBy` sind auf einer Map nicht definiert: Geh zuerst über `scores.entries`, das eine Collection der Einträge ist:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` ist die Menge aller Einträge; `scores.keys` und `scores.values` geben nur jeweils eine Seite.
