Listen sind ein Datentyp, mit dem Sie eine Sammlung verschiedener Informationsteile als Sequenz unter einem einzelnen Variablennamen speichern können.
Eine Liste speichert mehrere Werte eines oder mehrerer Typen und verwendet **Indizes**, um diese Werte zu unterscheiden.
Sie können Elemente einer Liste mit einem Ausdruck der folgenden Form zuweisen:
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` steht für den Typ der Elemente in der Liste, z. B. `Int`, `String`, `Any`...

---

Eine Liste ist eine Sammlung von Elementen mit einer bestimmten Reihenfolge. Es gibt zwei Arten von Listen in Kotlin:

- `List` kann nach der Erstellung nicht geändert werden.
- `MutableList` kann nach der Erstellung geändert werden, d. h. Sie können Elemente hinzufügen, entfernen oder aktualisieren.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ wirft einen Fehler auf, da `List`s _schreibgeschützt_ sind.

Um eine veränderbare Liste zu erstellen, verwenden Sie das Schlüsselwort `mutableListOf`
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

Sie können auf ein einzelnes Element der Liste über seinen Index zugreifen.
Ein Index ist wie eine Adresse, die den Ort des Elements in der Liste identifiziert.
Der Index erscheint direkt nach dem Listennamen, in Klammern, wie folgt:
```kotlin
listName[index]
```

Listenindizes beginnen mit `0`, **nicht** `1`! Sie greifen auf das erste Element einer Liste wie folgt zu: `listName[0]` oder `listName.get(0)` oder sogar `listName.first()`.
Das zweite Element in einer Liste befindet sich bei Index __1__: `listName[1]`.

---

Der Index ist eigentlich ein Offset vom ersten Element. Zum Beispiel, wenn Sie `list[2]` sagen, fragen Sie nicht nach dem zweiten Element der Liste, sondern nach dem Element, das 2 Positionen vom ersten Element entfernt ist. Daher ist `list[0]` das erste Element (null Offset), `list[1]` ist das zweite Element (Offset von 1), `list[2]` ist das dritte Element (Offset von 2) usw.

Ein Listenindex kann verwendet werden, um auf Werte zuzugreifen und diese zuzuweisen.
Sie haben gesehen, wie Sie wie folgt auf einen Listenindex zugreifen:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
So funktioniert eine Zuweisung:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

Wie Strings haben auch Listen eine **Länge**, die mit dem `size` Getter abgerufen wird.
Die Länge einer Liste ist die Anzahl der Elemente, die sie enthält

---

Eine weitere nützliche Listenoperation ist die Methode `contains`, um herauszufinden, ob ein bestimmtes Element in der Liste enthalten ist.
Wenn Sie beispielsweise eine Liste mit Namen haben, können Sie die Methode `contains` verwenden, um herauszufinden, ob ein bestimmter Name in der Liste vorhanden ist.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

Eine veränderbare Liste muss keine feste Länge haben.
Sie können jederzeit Elemente am Ende einer Liste hinzufügen!
Um ein Element zu einer veränderbaren Liste hinzuzufügen, verwenden wir die Funktion `add` oder die Abkürzung `+=`:
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

Wie wir im vorherigen Beispiel gesehen haben, können wir Elemente einzeln mit der Funktion `add` hinzufügen.
Aber wenn wir alle Elemente einer anderen Liste auf einmal hinzufügen müssen, können wir einfach die Funktion `addAll` oder die Abkürzung `+=` verwenden:
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e") 
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

Manchmal möchten Sie nur auf einen Teil einer Liste zugreifen.
Betrachten Sie den folgenden Code:
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__: Zuerst erstellen wir eine _schreibgeschützte_ Liste namens `numbers`.
__[2]__: Dann nehmen wir einen Unterabschnitt der Liste mit der Funktion `slice` und speichern ihn in der Slice-Liste.
Wir tun dies, indem wir die Indizes, die wir einfügen möchten, in der Funktion `slide` definieren.

In Kotlin können wir den letzten Index mit `..` einbeziehen, aber wir können den letzten Index auch mit `until` ausschließen

---

Listenelemente können jeden Typ haben, wenn wir den Typ `Any` angeben:
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
Tatsächlich haben wir oben der Reihe nach einen `String`, einen `Integer` und einen `Boolean`.
Aber wir können auch Listen mit Listen haben!

---

Manchmal müssen Sie ein Element in einer Liste suchen.
In Kotlin können wir die Methode `indexOfFirst` verwenden:
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

Die Methode `indexOfFirst` nimmt eine __Prädikat__-Funktion, die für jedes Element in der Liste ausgewertet wird, bis sie wahr ist, und gibt den _Index_ des Elements zurück.
Der obige Code druckt den ersten Index, der den String `"Zac"` enthält, `1` in diesem Fall.

Wir können auch Elemente an einem bestimmten Index in eine veränderbare Liste einfügen, indem wir die Methode `add(index, element)` verwenden:
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
Der obige Code fügt `"Ali"` bei Index `1` ein, was alles nach diesem Index um 1 verschiebt

---

In Kotlin können wir auf sehr einfache Weise durch eine Liste schleifen, indem wir die Schlüsselwörter `for..in` verwenden:
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3 
```
Ein Variablenname folgt dem Schlüsselwort `for`, dem der Wert jedes Listenelements nacheinander zugewiesen wird.
