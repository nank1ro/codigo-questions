Eine `Map` speichert **Schlüssel-Wert-Paare**: Jeder Wert wird über seinen Schlüssel abgerufen statt über einen Index.
Schlüssel sind innerhalb einer Map eindeutig, während sich Werte wiederholen können.

Mit `mapOf` erstellen Sie eine schreibgeschützte Map, indem Sie jeden Schlüssel mit seinem Wert über die Infix-Funktion `to` verknüpfen:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
Hier sind `"Italy"` und `"France"` die Schlüssel und `"Rome"` und `"Paris"` ihre Werte.

---

Um einen Wert zu lesen, indizieren Sie die Map mit ihrem Schlüssel, entweder mit eckigen Klammern oder mit der Funktion `get`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Wenn der Schlüssel nicht vorhanden ist, ist das Ergebnis `null`, weshalb der Typ von `ages["Alice"]` `Int?` ist, nicht `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

Wenn ein Schlüssel möglicherweise fehlt, können Sie mit `getOrDefault` den Wert wählen, der anstelle von `null` verwendet werden soll:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
Das erste Argument ist der Schlüssel, das zweite der Standardwert, der zurückgegeben wird, wenn der Schlüssel nicht gefunden wird.

---

Eine mit `mapOf` erstellte Map ist schreibgeschützt. Um Einträge hinzuzufügen oder zu ändern, verwenden Sie `mutableMapOf`, das eine `MutableMap` zurückgibt:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
Die Zuweisung mit `map[key] = value` fügt das Paar hinzu, wenn der Schlüssel neu ist, und ersetzt den Wert, wenn der Schlüssel bereits existiert. Sie können auch `ages.put("Bob", 25)` aufrufen, was dasselbe bewirkt.

---

`remove(key)` löscht einen Eintrag aus einer `MutableMap`. Wenn der Schlüssel nicht vorhanden ist, passiert nichts.
Die Eigenschaft `size` gibt an, wie viele Einträge die Map enthält:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Um zu prüfen, ob ein Schlüssel existiert, verwenden Sie `containsKey` oder den Operator `in`; um zu prüfen, ob ein Wert existiert, verwenden Sie `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

Die Eigenschaft `keys` gibt alle Schlüssel einer Map als `Set` zurück, und `values` gibt alle Werte als Sammlung zurück:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Beide behalten die Reihenfolge bei, in der die Einträge eingefügt wurden.

---

Sie können mit `for` über eine Map iterieren und dabei jeden Eintrag in seinen Schlüssel und Wert destrukturieren:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
Die Klammern `(name, age)` teilen jeden Eintrag in zwei Variablen auf. Die Einträge werden in der Reihenfolge besucht, in der sie eingefügt wurden.
