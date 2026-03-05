`Set`s sind ein Datentyp, mit dem Sie eine Sammlung verschiedener Informationsteile als Sequenz unter einem einzelnen Variablennamen speichern können.
Der Hauptunterschied zu `List`s besteht darin, dass ein `Set` nur ein Element pro Wert ermöglicht.

Wie `List`s speichert ein `Set` mehrere Werte eines oder mehrerer Typen und verwendet **Indizes**, um diese Werte zu unterscheiden.
Sie können Elemente einer Menge mit einem Ausdruck der folgenden Form zuweisen:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` steht für den Typ der Elemente in der Menge, zum Beispiel `Int`, `String`, `Any`...

---

Ein `Set` ist eine Sammlung von __eindeutigen__ Elementen ohne eine bestimmte Reihenfolge.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

Bei __[1]__ versuchen wir, ein Set mit der Zahl __1__ zu erstellen, die zweimal vorhanden ist. Aber wie Sie sehen können, muss jedes Element eindeutig sein und die zweite __1__ wird automatisch verworfen.

---

Es gibt zwei Arten von `Set`s in Kotlin:

- `Set` kann nach der Erstellung nicht geändert werden.
- `MutableSet` kann nach der Erstellung geändert werden, d. h. Sie können seine Elemente hinzufügen, entfernen oder aktualisieren.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ wirft einen Fehler, weil `Set`s _schreibgeschützt_ sind.

Um ein veränderbares Set zu erstellen, verwenden Sie das Schlüsselwort `mutableSetOf`
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

Die häufigste `Set`-Aktivität ist das Testen auf Zugehörigkeit mit `in` oder `contains()`

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

Wie Sie oben sehen können, geben `in` und `contains` einen `Bool` zurück, der angibt, ob sich das übergebene Element in der Menge befindet

---

Die Reihenfolge der Elemente in einer `Set` ist nicht wichtig.
Wenn Sie tatsächlich versuchen, zwei `Set`s mit dem gleichen Element, aber in unterschiedlicher Reihenfolge zu vergleichen, erhalten Sie, dass sie gleich sind.

---

Mit `Set`s können Sie mehrere Operationen durchführen, z. B. Überprüfung von Vereinigung, Schnittmenge, Differenz und Teilmenge.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

Um eine `Set` in eine `List` zu konvertieren, können wir die Funktion `toList()` verwenden
