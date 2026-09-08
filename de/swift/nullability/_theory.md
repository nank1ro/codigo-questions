Manchmal fehlt ein Wert einfach: ein Benutzer ohne zweiten Vornamen, eine Suche, die nichts findet, ein Text, der sich nicht in eine Zahl umwandeln lässt.
Swift stellt einen fehlenden Wert mit `nil` dar, aber eine normale Variable kann ihn niemals enthalten:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
Um einen fehlenden Wert zuzulassen, deklarierst du einen **optionalen** Typ, indem du ein Fragezeichen `?` nach dem Typ hinzufügst.
Ein `Int?` enthält entweder einen `Int` oder `nil`:
```swift
var age: Int? = 30
age = nil // erlaubt
```
Eine optionale Variable, die ohne Wert deklariert wird, startet als `nil`.

---

Du kannst ein Optional mit `nil` mithilfe von `==` und `!=` vergleichen, und du kannst es auch direkt mit einem einfachen Wert des zugrunde liegenden Typs vergleichen:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Denke daran, dass `Int?` und `Int` zwei unterschiedliche Typen sind: ein `Int?` kann leer sein, ein `Int` niemals.

---

Ein Optional ist wie eine Box: Bevor du den Wert darin verwenden kannst, musst du sie öffnen, was Swift **Entpacken** nennt.
Der schnellste Weg ist das **erzwungene Entpacken** mit einem Ausrufezeichen `!`:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
Das `!` teilt Swift mit: "Ich bin sicher, dass hier ein Wert vorhanden ist". Wenn du dich irrst und das Optional `nil` ist, stoppt das Programm sofort mit einem Laufzeitabsturz:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
Deshalb gilt erzwungenes Entpacken als gefährlich: verwende es nur, wenn du sicher bist, dass der Wert existiert.

---

Erzwungenes Entpacken ist nur sicher, wenn du bereits geprüft hast, dass das Optional nicht `nil` ist:
```swift
if score != nil {
    print(score! * 2)
}
```

---

Erst auf `nil` prüfen und dann erzwungen entpacken ist umständlich. Swift bietet **optionale Bindung** mit `if let`, die das Optional in einem einzigen Schritt entpackt und den Wert in einer neuen Konstante speichert:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value ist ein Int, kein Int?
} else {
    print("No score")
}
```
Der Rumpf des `if` wird nur ausgeführt, wenn das Optional einen Wert enthält; darin ist `value` ein einfacher `Int` und benötigt kein `!`.

---

Wenn ein fehlender Wert bedeutet "hier aufhören", ist `guard let` klarer als `if let`.
Es entpackt das Optional und führt, falls das fehlschlägt, den `else`-Block aus, der den aktuellen Gültigkeitsbereich verlassen muss (mit `return`, `break`, `continue` oder `throw`):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // name ist ab hier ein String
}
```
Anders als bei `if let` bleibt die entpackte Konstante für den Rest der Funktion verfügbar, sodass der Hauptpfad nicht in einem `if` verschachtelt ist.

---

Eine typische Verwendung von `guard let` besteht darin, die Eingabe einer Funktion am Anfang zu validieren und einen Ersatzwert zurückzugeben, wenn sie fehlt:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Sehr oft möchtest du von einem Optional nur seinen Wert oder einen Standardwert.
Der **Nil-Koaleszenzoperator** `??` macht genau das: Er entpackt das Optional, wenn es einen Wert hat, andernfalls gibt er den Wert rechts davon zurück:
```swift
let score: Int? = nil
let points = score ?? 0 // points ist ein Int gleich 0
```
Der Standardwert muss denselben Typ wie der enthaltene Wert haben.
Du kannst mehrere `??` verketten: der erste Wert, der nicht `nil` ist, gewinnt.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` ist der kürzeste Weg, ein Optional in einen einfachen Wert umzuwandeln, wenn ein sinnvoller Standardwert existiert:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

Beim Verketten von `??` wertet Swift von links nach rechts aus und stoppt beim ersten Wert, der nicht `nil` ist; der letzte Standardwert wird nur verwendet, wenn jedes Optional davor `nil` ist.

---

Auf eine Eigenschaft zuzugreifen oder eine Methode auf einem Optional aufzurufen würde erfordern, es zuerst zu entpacken.
**Optional Chaining** mit `?.` erledigt das für dich: Wenn das Optional `nil` ist, wird der gesamte Ausdruck zu `nil`, andernfalls geht der Zugriff durch:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? mit "SWIFT"
```
Das Ergebnis ist immer ein Optional, auch wenn die Eigenschaft selbst keines ist.
Ketten können so lang sein, wie du brauchst, und sie lassen sich gut mit `??` kombinieren:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

Optional Chaining zeigt seine Stärke, wenn Daten auf mehreren Ebenen fehlen können: ein Objekt kann `nil` sein, und eine seiner Eigenschaften kann es auch sein.
Eine einzige `?.`-Kette behandelt beide Fälle ohne jedes `if`.

---

Ein einzelnes `if let` oder `guard let` kann mehrere Optionals gleichzeitig entpacken: trenne die Bindungen mit Kommas.
Der Rumpf läuft nur, wenn jedes Optional einen Wert hat:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
Du kannst nach den Bindungen auch eine boolesche Bedingung anhängen, wie `if let n = number, n > 0`.

---

Mehrere Optionals in einem `if let` zu binden hält den Code flach: ein einziger `else`-Zweig deckt jeden fehlenden Wert ab.

---

Viele Operationen können fehlschlagen, und Swift meldet den Fehlschlag, indem es ein Optional zurückgibt.
Text in eine Zahl umzuwandeln ist das klassische Beispiel: `Int("42")` gibt ein `Int?` zurück, das `42` enthält, während `Int("abc")` `nil` zurückgibt.
`Int("3.5")` ist ebenfalls `nil`, weil der Text keine ganze Zahl ist; verwende `Double("3.5")` für Dezimalzahlen.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
Weitere Beispiele sind `array.first` (`nil` bei einem leeren Array) und `dictionary[key]` (`nil`, wenn der Schlüssel fehlt).

---

Weil eine Umwandlung fehlschlagen kann, ist ihr Ergebnis immer ein Optional und muss vor der Verwendung entpackt werden, selbst wenn du sicher bist, dass der Text eine gültige Zahl ist.

---

Fehlschlagbare Umwandlungen passen natürlich zu `guard let`: umwandeln, abbrechen, wenn das Ergebnis `nil` ist, dann mit dem einfachen Wert weiterarbeiten.

---

Manchmal möchtest du den Wert innerhalb eines Optionals transformieren und das Ergebnis optional halten, ohne von Hand zu entpacken und wieder zu verpacken.
Optionals haben eine `map`-Methode: sie wendet die Closure auf den Wert an, falls einer vorhanden ist, und gibt andernfalls `nil` zurück.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? mit 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Kombiniert mit einer fehlschlagbaren Umwandlung ergibt sich eine kompakte Pipeline: `Int(text).map { $0 + 1 }`.
