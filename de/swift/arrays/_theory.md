Arrays sind ein Datentyp, mit dem Sie eine Sammlung verschiedener Informationen als Sequenz unter einem einzelnen Variablennamen speichern können.
Ein Array speichert mehrere Werte eines oder mehrerer Typen und verwendet **Indizes**, um diese Werte zu unterscheiden.
Sie können Elemente einem Array mit einem Ausdruck der folgenden Form zuweisen:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` steht für den Typ der Elemente im Array, zum Beispiel kann es `Int`, `String`, `Any` sein...

---

Sie können auf ein einzelnes Element des Arrays über seinen Index zugreifen.
Ein Index ist wie eine Adresse, die die Position des Elements im Array kennzeichnet.
Der Index steht direkt nach dem Array-Namen in Klammern, etwa so:
```swift
arrayName[index]
```

Array-Indizes beginnen mit `0`, **nicht** mit `1`! Sie greifen auf das erste Element eines Arrays so zu: `arrayName[0]`.
Das zweite Element in einem Array befindet sich bei Index 1: `arrayName[1]`.

---

Ein Array-Index verhält sich wie jeder andere Variablenname.
Er kann verwendet werden, um Werte zu lesen und auch zuzuweisen.
Sie haben gesehen, wie man einen Array-Index so zugreift:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Gibt den Wert "Jeremiah" aus
print(names[0])
```
So funktioniert eine Zuweisung:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Neue Wert "Jordan" zuweisen
names[0] = "Jordan"
// Gibt den Wert "Jordan" aus
print(names[0])
```

---

Genau wie Strings haben Arrays eine **Länge** `count`.
Die Länge eines Arrays ist die Anzahl der Elemente, die es enthält

---

Ein Array muss keine feste Länge haben.
Sie können jederzeit Elemente am Ende eines Arrays hinzufügen!
Um ein Element zu einem Array hinzuzufügen, verwenden wir die `append`-Funktion:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Gibt ["a", "b", "c"] aus
```

---

Manchmal möchten Sie nur auf einen Teil eines Arrays zugreifen.
Betrachten Sie den folgenden Code:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// gibt [2, 3] aus
```
Zunächst erstellen wir ein Array namens `numbers`.
Dann nehmen wir einen Unterabschnitt des Arrays und speichern ihn im slice-Array.
Dies tun wir, indem wir die Indizes definieren, die wir einschließen möchten, nach dem Namen des Arrays: `numbers[1...2]`.
In Swift können wir den letzten Index mit `...` einschließen, aber wir können auch den letzten Index mit `..<` ausschließen

---

In Swift können wir ein Array nach Belieben aufteilen!
```swift
// Nimmt die ersten zwei Elemente
listName[..<2]
// Nimmt das vierte bis letzte Element
listName[3...]
```
Wenn Ihr Array-Slice das allererste oder letzte Element in einem Array enthält, muss der Index für dieses Element nicht angegeben werden

---

Array-Elemente können von jedem Typ sein, wenn wir den Typ `Any` angeben:
```swift
var arrayName: [Any] = ["one", 2, true]
```
In der Tat haben wir oben in der Reihenfolge einen String, eine ganze Zahl und einen Boolean.
Wir können aber auch Arrays mit Arrays haben!

---

Manchmal müssen Sie nach einem Element in einem Array suchen.
In Swift können wir die Methode `firstIndex()` verwenden:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// gibt 1 aus
```
Der obige Code gibt den ersten Index aus, der den String `"Zac"` enthält, in diesem Fall `1`.
Wir können auch Elemente an einem bestimmten Index in ein Array einfügen, indem wir die Methode `insert()` verwenden:
```swift
names.insert("Ali", at: 1)
// gibt ["Trevor", "Ali", "Zac", "Glenn"] aus
```
Der obige Code fügt `"Ali"` bei Index `1` ein, wodurch alles nach diesem Index um 1 nach unten verschoben wird

---

In Swift können wir auf sehr einfache Weise mit den Schlüsselwörtern `for..in` durch ein Array iterieren:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// gibt 1, 2, 3 aus
```
Ein Variablenname folgt dem Schlüsselwort `for`, ihm wird der Wert jedes Array-Elements nacheinander zugewiesen.

---

**Tuples** sind wie Arrays, aber Sie können die Elemente benennen und diese Namen verwenden, um auf sie zu verweisen
Um ein Tuple zu erstellen, verwenden wir die runden Klammern `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
