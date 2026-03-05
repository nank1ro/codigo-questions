**Wörterbücher** sind ähnlich wie Arrays und Tupel, aber du greifst auf Werte zu, indem du einen *Schlüssel* anstelle eines Index suchst
Ein Schlüssel kann eine beliebige Zeichenkette oder Zahl sein.
Wörterbücher werden in eckigen Klammern eingeschlossen, wie folgt:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
Dies ist ein Wörterbuch namens `dictionaryName` mit drei *Schlüssel-Wert-Paaren*.
Der Schlüssel `key1` verweist auf den Wert `1`, `key2` auf `2` usw.

---

Der Zugriff auf Wörterbuch-Werte nach Schlüssel ist genauso wie der Zugriff auf Array-Werte nach Index:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Wie Arrays sind Wörterbücher _veränderbar_.
Das bedeutet, dass sie nach ihrer Erstellung geändert werden können (wenn sie nicht als konstant deklariert sind).
Ein Vorteil davon ist, dass wir neue _Schlüssel-Wert-Paare_ zum Wörterbuch hinzufügen können, nachdem es erstellt wurde, wie folgt:
```swift
dictName[newKeyName] = newValue
```

---

Die Länge `count` eines Wörterbuchs ist die Anzahl der _Schlüssel-Wert-Paare_, die es hat.
Jedes Paar zählt nur einmal, auch wenn der Wert ein Array ist. (Das ist richtig: Du kannst auch Arrays in Wörterbüchern ablegen!)

---

Da Wörterbücher veränderbar sind, können sie auf vielfältige Weise geändert werden. Elemente können mit der Methode `removeValue(forKey:)` aus einem Wörterbuch entfernt werden:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
entfernt den Schlüssel `keyName` und seinen zugehörigen Wert aus dem Wörterbuch.

---

Was ist, wenn wir alle Schlüssel des Wörterbuchs auflisten möchten?
Nun, da ist die Eigenschaft `keys`.

---

Was ist, wenn wir alle Werte des Wörterbuchs auflisten möchten?
Nun, da ist die Eigenschaft `values`.

---

Wie bei Arrays können wir mit den Schlüsselwörtern `for..in` zwischen Wörterbuchelementen schleifen.
Um sowohl den Schlüssel als auch den Wert in der Schleife zu erhalten, müssen wir keine Eigenschaft angeben:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

Wir können auch die Eigenschaft `isEmpty`, die wir mit Arrays verwendet haben, verwenden, um zu bestimmen, ob ein Wörterbuch leer ist

---

Um Werte zu einem Wörterbuch hinzuzufügen oder zu ändern, können wir auch die Methode `updateValue(_:forKey:)` verwenden

---

Früher haben wir gesehen, wie man ein _Schlüssel-Wert-Paar_ aus dem Wörterbuch mit der Methode `removeValue()` entfernt.
Wir können ein Element auch durch Zuweisung des Wertes `nil` zum Schlüssel entfernen
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
