Jeder Wert in Swift hat einen **Typ**, der dem Compiler mitteilt, um welche Art von Daten es sich handelt und was du damit machen kannst.
Die grundlegenden Typen sind:
- `Int`: eine Ganzzahl, wie `42` oder `-7`
- `Double`: eine Zahl mit Dezimalteil, wie `3.14`
- `String`: ein Stück Text, wie `"Hello"`
- `Character`: ein einzelnes Zeichen, wie `"a"`
- `Bool`: entweder `true` oder `false`

Du kannst den Typ einer Konstante oder Variable mit einer **Typannotation** angeben: einem Doppelpunkt und dem Typnamen nach dem Namen:
```swift
let age: Int = 36
let name: String = "Ada"
```
Ein Wert eines Typs kann nicht in einer Konstante eines anderen Typs gespeichert werden: `let age: Int = "36"` ist ein Compilerfehler.

---

Meistens schreibst du die Typannotation nicht: Swift **leitet** den Typ aus dem Wert ab, den du zuweist, und folgt dabei einigen Literalregeln:
- eine Zahl ohne Dezimalpunkt, wie `42`, ist ein `Int`
- eine Zahl mit Dezimalpunkt, wie `3.14`, ist ein `Double`
- Text zwischen doppelten Anführungszeichen ist ein `String`
- `true` und `false` sind `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift hat auch `Float`, eine Dezimalzahl, die halb so viel Speicher wie ein `Double` verwendet, aber weniger präzise ist, daher wird ein Dezimalliteral nie als `Float` abgeleitet: du musst es mit einer Annotation anfordern.
Ebenso wird `"a"` als `String` abgeleitet, daher braucht ein `Character` immer eine Annotation.

---

Die Funktion `type(of:)` gibt den Typ eines Werts zurück, was praktisch ist, um zu prüfen, was Swift abgeleitet hat:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
Wenn du einen anderen Typ als den abgeleiteten möchtest, füge eine Annotation hinzu. Ein Ganzzahl-Literal kann in einer `Double`- oder `Float`-Konstante gespeichert werden, und ein Ein-Zeichen-Literal in einer `Character`-Konstante:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift wandelt Zahlentypen nie von selbst um: das Addieren eines `Int` zu einem `Double` ist ein Compilerfehler, obwohl beide Zahlen sind.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
Um sie zu kombinieren, erzeugst du einen neuen Wert des benötigten Typs, indem du den Wert an den Initialisierer des Typs übergibst:
```swift
let total = Double(apples) * price // 4.5
```
Dasselbe funktioniert umgekehrt: `Int(4.5)` erzeugt einen `Int` und behält nur den Ganzzahlanteil der Zahl.

---

`Int(x)` rundet nicht: es **schneidet ab**, verwirft einfach den Dezimalteil, daher ist `Int(3.99)` gleich `3` und `Int(-3.99)` gleich `-3`.
Um auf die nächste Ganzzahl zu runden, rufe zuerst `rounded()` auf dem `Double` auf und wandle dann um:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
Halbe Werte wie `2.5` werden von Null weg gerundet: `2.5` wird zu `3.0` und `-2.5` wird zu `-3.0`.

---

Der Typ der Operanden entscheidet, wie die Division funktioniert. Wenn beide `Int` sind, führt der Operator `/` eine **Ganzzahldivision** durch: das Ergebnis ist ein `Int` und der Rest wird verworfen.
Wenn mindestens ein Operand ein `Double` ist, führt `/` eine Fließkommadivision durch und behält den Dezimalteil:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
Um also aus zwei `Int`-Werten ein Dezimalergebnis zu erhalten, musst du mindestens einen davon **vor** der Division in `Double` umwandeln: `Double(7 / 2)` ist `3.0`, weil die Ganzzahldivision bereits stattgefunden hat.

---

Wenn eine Funktion ein Dezimalergebnis aus Ganzzahlen zurückgeben muss, wandle die Operanden vor der Division in `Double` um und deklariere den Rückgabetyp als `Double`:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Denke daran, dass `count` eines Arrays ebenfalls ein `Int` ist, daher braucht es dieselbe Umwandlung.

---

Zahlen und Strings werden mit derselben Initialisierer-Syntax umgewandelt. `String(42)` macht aus einer Zahl den Text `"42"`, genau wie ihre Interpolation mit `"\(42)"`.
Die entgegengesetzte Richtung kann fehlschlagen, weil nicht jeder Text eine Zahl ist, daher gibt `Int("42")` ein **optionales** `Int?` zurück: hier enthält es `42`, aber `Int("hello")` ist `nil`.
Wie du in den Optional-Übungen gelernt hast, kannst du mit `??` einen Fallback angeben oder es mit `if let` entpacken:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` gelingt nur, wenn der gesamte Text eine gültige Ganzzahl ist, mit optionalem Vorzeichen:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
Für Dezimaltext verwende `Double(text)`, das auf dieselbe Weise ein `Double?` zurückgibt: `Double("3.5")` ist `Optional(3.5)`.

---

Ein **Typalias** gibt einem bestehenden Typ einen neuen Namen, mit dem Schlüsselwort `typealias`:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` und `Int` sind derselbe Typ, daher lassen sie sich frei mischen. Ein Alias fügt keine Sicherheit hinzu: Er macht den Code nur besser lesbar, wenn ein einfacher Typ eine bestimmte Bedeutung in deinem Programm hat.

---

Ein `Int` verwendet 64 Bits, daher kann er nur Zahlen in einem festen Bereich darstellen. Der größte und der kleinste Wert sind als `Int.max` und `Int.min` verfügbar:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Das Überschreiten dieser Grenzen wird **Überlauf** genannt. Anders als in vielen anderen Sprachen läuft Swift nicht stillschweigend am anderen Ende des Bereichs weiter: eine überlaufende Operation ist ein **Laufzeitfehler**, der das Programm stoppt.

---

`Int.max` und `Int.min` sind als Startwerte nützlich, wenn du nach einem Extremwert suchst: jede tatsächliche Zahl ist kleiner als `Int.max`, daher ist es ein sicherer Anfangswert für "das bisher kleinste":
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

Wie du in den Strings-Übungen gesehen hast, gibt dir das Iterieren über einen `String` jeweils ein `Character`. Ein `Character` ist kein `String`, daher wandelst du ihn mit `String(c)` um, um ihn als Text zu verwenden.
Wenn das Zeichen eine Ziffer ist, gibt dir die Eigenschaft `wholeNumberValue` ihren Zahlenwert als `Int?`: sie ist `nil` für Zeichen, die keine Ziffern sind.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Da `Int(text)` und `Double(text)` bei einem Fehler `nil` zurückgeben, verrät dir der Vergleich des Ergebnisses mit `nil`, ob ein Text eine Zahl dieser Art ist:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Beachte die letzte Zeile: jeder von `Int` akzeptierte Text wird auch von `Double` akzeptiert, daher prüfe zuerst auf `Int`, wenn du sie unterscheiden willst.

---

Manchmal musst du Werte verschiedener Typen zusammen speichern. Der spezielle Typ `Any` kann einen Wert **eines beliebigen** Typs enthalten, daher kann ein als `[Any]` deklariertes Array Zahlen, Strings und Booleans mischen:
```swift
let items: [Any] = [1, "two", true]
```
Jedes Element erinnert sich noch an seinen echten Typ, den `type(of:)` offenlegt. Um mit dem Wert als seinem echten Typ zu arbeiten, verwendest du einen **bedingten Cast** mit `as?`, der ein Optional zurückgibt: er enthält den Wert, wenn der Typ passt, und sonst `nil`:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` ist eine letzte Option: ein Array eines einzelnen konkreten Typs ist sicherer und einfacher zu verwenden, daher ziehe es wann immer möglich vor.

---

Bedingte Casts lassen sich natürlich mit `else if` verketten, um mehrere mögliche Typen zu behandeln, und wandeln jeden in den Typ um, den du für das Ergebnis brauchst:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
Ein in `Any` gespeicherter `Int` bleibt ein `Int`: `as? Double` darauf gibt `nil` zurück, weil `as?` den Typ prüft, es wandelt keine Zahlen um.
