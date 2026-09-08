Ein **String** ist ein Stück Text. In Swift schreibst du ein String-Literal zwischen doppelten Anführungszeichen, und sein Typ ist `String`:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
Wie bei jedem anderen Wert erzeugt `let` eine Konstante, die nicht geändert werden kann, und `var` erzeugt eine Variable, die es kann.
Swift leitet den Typ `String` aus dem Literal ab, daher ist die Typannotation optional.

---

Die **String-Interpolation** fügt den Wert eines Ausdrucks in ein String-Literal ein. Setze den Ausdruck in `\()`:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
Jeder Typ kann interpoliert werden: Zahlen, Booleans und andere Strings werden automatisch in Text umgewandelt.

---

Zwei Strings können mit dem `+`-Operator verbunden werden, der einen neuen String erzeugt:
```swift
let full = "Hello" + " " + "world" // Hello world
```
Um am Ende einer bestehenden String-Variable Text hinzuzufügen, verwendest du `+=`. Die Variable muss mit `var` deklariert werden, weil sich ihr Wert ändert:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

Die Eigenschaft `count` gibt die Anzahl der Zeichen in einem String zurück, und `isEmpty` ist `true`, wenn der String überhaupt keine Zeichen enthält:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Jedes Zeichen wird gezählt, einschließlich Leerzeichen und Satzzeichen.

---

Ein `String` ist eine Sammlung von `Character`-Werten. Ein `Character` ist ein einzelner Buchstabe, eine Ziffer, ein Symbol oder ein Leerzeichen, und er wird mit denselben doppelten Anführungszeichen wie ein String geschrieben, daher benötigst du eine Typannotation, um einen zu erhalten:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
`isEmpty` zu prüfen ist besser, als `count` mit `0` zu vergleichen: Es liest sich besser und muss nicht jedes Zeichen zählen.

---

Ein **mehrzeiliges String-Literal** beginnt und endet mit drei doppelten Anführungszeichen `"""`, jeweils auf einer eigenen Zeile. Jede Zeile dazwischen wird Teil des Strings, und die Zeilenumbrüche bleiben erhalten:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
Das gibt die beiden Zeilen genau so aus, wie sie geschrieben wurden. Die schließenden `"""` legen außerdem die Einrückung fest: jeglicher Leerraum davor wird am Anfang jeder Zeile entfernt.

---

Da ein String eine Sammlung von Zeichen ist, kannst du mit einer `for`-`in`-Schleife über ihn iterieren. Jede Iteration liefert dir ein `Character`:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
Ein `Character` kann mit `==` mit einem Zeichenliteral verglichen werden, daher ist das Zählen, wie oft ein Zeichen vorkommt, nur eine Schleife mit einem Zähler.

---

Im Gegensatz zu Arrays können Strings nicht mit einer Ganzzahl indiziert werden wie `text[2]`: Manche Zeichen benötigen mehr Speicher als andere, daher verwendet Swift einen eigenen Typ `String.Index`, um auf eine Position zu zeigen.
`startIndex` ist die Position des ersten Zeichens und `endIndex` ist die Position *nach* dem letzten. Um dich von einem Index aus zu bewegen, verwendest du `index(_:offsetBy:)` und indizierst den String dann mit dem Ergebnis:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Sich über das Ende des Strings hinaus zu bewegen führt zur Laufzeit zu einem Absturz, daher muss der Offset innerhalb von `count` bleiben.

---

Die Arbeit mit Indizes ist umständlich, daher bietet Swift Abkürzungen für die häufigsten Fälle:
- `first` und `last` geben das erste und letzte Zeichen als optionales `Character?` zurück (`nil` bei einem leeren String)
- `prefix(n)` gibt die ersten `n` Zeichen zurück und `suffix(n)` die letzten `n`
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` und `suffix` geben eine `Substring` zurück, eine Sicht auf den ursprünglichen Text. Um sie als echten `String` zu speichern, umschließe sie mit `String(...)`. Wenn `n` größer als `count` ist, erhältst du einfach den ganzen String.

---

Drei Methoden beantworten die häufigsten Fragen zum Inhalt eines Strings, und jede gibt einen `Bool` zurück:
- `contains(_:)` ist `true`, wenn der angegebene Text (oder das Zeichen) irgendwo im String vorkommt
- `hasPrefix(_:)` ist `true`, wenn der String mit dem angegebenen Text beginnt
- `hasSuffix(_:)` ist `true`, wenn der String mit dem angegebenen Text endet
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
Alle drei unterscheiden zwischen Groß- und Kleinschreibung: `"Swift".hasPrefix("s")` ist `false`.

---

Da `contains`, `hasPrefix` und `hasSuffix` Booleans zurückgeben, lassen sie sich auf natürliche Weise mit `||` und `&&` kombinieren, um komplexere Prüfungen zu bauen.

---

`uppercased()` und `lowercased()` geben einen **neuen** String zurück, bei dem jeder Buchstabe in Groß- oder Kleinbuchstaben umgewandelt wurde. Der ursprüngliche String wird nicht verändert:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Beide sind Methoden, also vergiss die Klammern nicht.

---

Die Umwandlung in Kleinbuchstaben ist der übliche Weg, um Text unabhängig von der Groß-/Kleinschreibung zu vergleichen: Zwei Strings, die sich nur in der Groß-/Kleinschreibung unterscheiden, werden gleich, sobald beide in Kleinbuchstaben umgewandelt wurden.

---

`split(separator:)` zerlegt einen String überall dort, wo das Trennzeichen vorkommt, in ein Array von Teilen. `joined(separator:)` macht das Gegenteil: Es fügt die Elemente eines Arrays zu einem einzigen String zusammen und setzt dabei das Trennzeichen dazwischen:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Wie `prefix` gibt auch `split` `Substring`-Werte zurück; umschließe einen davon mit `String(...)`, wenn du ihn als `String` speichern musst.

---

Das Aufteilen an Leerzeichen ist der einfachste Weg, einen Satz in Wörter zu zerlegen, und das Zusammenfügen ist der Weg, um Text aus einem Array wiederherzustellen.

---

Das Foundation-Framework fügt viele zusätzliche String-Methoden hinzu. Eine der nützlichsten ist `replacingOccurrences(of:with:)`, die einen neuen String zurückgibt, in dem jedes Vorkommen des ersten Textes durch den zweiten ersetzt wird:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
Denke daran, am Anfang der Datei `import Foundation` zu schreiben, sonst ist die Methode nicht verfügbar. Methodenaufrufe können verkettet werden, sodass `text.lowercased().replacingOccurrences(of: " ", with: "_")` gültig ist.

---

Strings können mit denselben Operatoren wie Zahlen verglichen werden. `==` prüft, ob zwei Strings genau dieselben Zeichen haben, während `<` und `>` sie Zeichen für Zeichen in alphabetischer Reihenfolge vergleichen:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
Der Vergleich unterscheidet zwischen Groß- und Kleinschreibung, und jeder Großbuchstabe kommt **vor** jedem Kleinbuchstaben, daher ist `"B" < "a"` gleich `true`.

---

Ein `Character` ist kein `String`, daher kann er nicht direkt mit `+` an einen String angehängt werden. Wandle ihn zuerst mit `String(...)` um:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Kombiniert mit einer `for`-`in`-Schleife lässt sich damit ein String Zeichen für Zeichen neu aufbauen, zum Beispiel indem jedes neue Zeichen vor die bisher gesammelten gesetzt wird.
