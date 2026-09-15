Ein **regulärer Ausdruck** (Regex) ist ein kleines Muster, das eine Form von Text beschreibt: „eine Folge von Ziffern“, „ein Wort, gefolgt von einem Gleichheitszeichen“, „drei Großbuchstaben“. Statt Schleifen über Zeichen zu schreiben, beschreibst du die Form einmal und lässt Swift sie finden.

Swift schreibt einen Regex zwischen `#/` und `/#`:
```swift
let digits = #/\d+/#
```
Innerhalb des Musters bedeutet `\d` „eine beliebige Ziffer“ und `+` bedeutet „eines oder mehr vom vorherigen Element“, also bedeutet `\d+` „eine Folge von einer oder mehreren Ziffern“.

Die einfachste Frage, die du stellen kannst, ist, ob ein Text eine Übereinstimmung enthält. `contains(_:)` nimmt einen Regex und gibt einen `Bool` zurück:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Verwende immer die hier gezeigte Form `#/ ... /#`: Die kürzere Schreibweise `/ ... /` verwirrt den Compiler, wenn das Muster direkt in einem Methodenaufruf steht.

---

Ein paar Kurzschreibweisen decken die meisten Muster ab. Jede davon passt auf genau **ein** Zeichen:
- `\d` ist eine Ziffer
- `\w` ist ein Buchstabe, eine Ziffer oder ein Unterstrich
- `\s` ist ein Leerzeichen, ein Tabulator oder ein Zeilenumbruch
- `.` ist ein beliebiges einzelnes Zeichen

Um mehr als ein Zeichen zu treffen, füge direkt nach dem Muster einen **Quantifizierer** hinzu:
- `+` bedeutet eines oder mehr
- `*` bedeutet null oder mehr
- `?` bedeutet null oder eins

Also ist `\w+` ein Wort, `\s*` ein optionaler Abstand und `\d?` eine optionale Ziffer:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
Ein Zeichen ohne besondere Bedeutung passt einfach auf sich selbst, daher trifft `#/cat/#` auf die drei Buchstaben `cat`.

---

Standardmäßig darf ein Muster an beliebiger Stelle im Text passen. **Anker** binden es stattdessen an eine Position:
- `^` bedeutet „der Anfang des Textes“
- `$` bedeutet „das Ende des Textes“

```swift
print("swift".contains(#/^sw/#))  // true, der Text beginnt mit sw
print("myswift".contains(#/^sw/#)) // false, sw steht nicht am Anfang
print("swift".contains(#/ft$/#))  // true, der Text endet mit ft
```
Anker treffen eine Position, kein Zeichen, daher tragen sie nichts zum Inhalt der Übereinstimmung bei.

---

Wenn keine der Kurzschreibweisen passt, liste die Zeichen, die du akzeptierst, in eckigen Klammern auf. `[abc]` trifft auf ein `a`, ein `b` oder ein `c`, und ein Bindestrich schreibt einen Bereich:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
Eine Zahl in geschweiften Klammern sagt genau, wie oft sich das vorherige Muster wiederholt: `{3}` bedeutet dreimal, `{2,4}` bedeutet zwischen zwei- und viermal:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Ein Muster mit `^` und `$` zu umschließen und mit einer Anzahl zu versehen, ist die übliche Methode, um zu prüfen, dass ein ganzer Text eine bestimmte Form hat.

---

`contains(_:)` sagt nur ja oder nein. Um den gefundenen Text zu erhalten, verwendest du `firstMatch(of:)`. Es gibt eine **optionale Übereinstimmung** zurück: `nil`, wenn nichts gepasst hat, sodass es sich natürlich mit `if let` kombinieren lässt.

Der gefundene Text ist in der Eigenschaft `0` der Übereinstimmung gespeichert, geschrieben als `m.0`:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` stoppt bei der ersten Übereinstimmung, selbst wenn der Text mehr enthält.

---

`m.0` ist kein `String`, sondern ein `Substring`: ein Blick in den ursprünglichen Text, keine Kopie. Es wird genau wie ein String ausgegeben, aber wo ein `String` verlangt wird, musst du es umwandeln:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Zahleninitialisierer nehmen ein `Substring` direkt an, daher funktioniert `Int(m.0)` ohne den Umweg.

---

`matches(of:)` gibt **jede** Übereinstimmung statt nur der ersten zurück, als Array. Das Array ist nie `nil`: Wenn nichts passt, ist es einfach leer, sodass du es direkt durchlaufen oder umwandeln kannst:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Jedes Element ist eine Übereinstimmung, daher ist `$0.0` in einem `map` der gefundene Text:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Weil `Int(_:)` ein `Substring` akzeptiert, ist das Umwandeln von gefundenem Text in Zahlen ein einziger Schritt. `compactMap` ist hier praktisch: Es verwirft die Werte, die `nil` zurückgeben:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Verwende `map`, wenn sich jedes Element umwandeln lässt, und `compactMap`, wenn einige fehlschlagen können.

---

Runde Klammern um einen Teil des Musters erzeugen eine **Erfassungsgruppe**: Die gesamte Übereinstimmung bleibt `m.0`, und der Teil innerhalb der Klammern wird zu `m.1`:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
So behältst du den interessanten Teil und wirfst den umgebenden Text weg. Ohne Klammern gibt es überhaupt kein `m.1`, und der Code kompiliert nicht.

---

Ein Muster kann mehrere Gruppen enthalten. Sie werden von links nach rechts nach ihrer öffnenden Klammer nummeriert, daher ist die zweite `m.2`, die dritte `m.3` und so weiter:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` bleibt immer die gesamte Übereinstimmung, ganz gleich wie viele Gruppen es gibt.

---

Klammern zu zählen wird schnell fehleranfällig, sobald ein Muster wächst. Gib einer Gruppe stattdessen einen **Namen**, indem du `?<name>` direkt nach ihrer öffnenden Klammer schreibst, und lies sie als Eigenschaft der Übereinstimmung:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
Benannte Gruppen werden weiterhin nummeriert, daher funktioniert `m.1` weiterhin, aber `m.key` sagt aus, was sie enthält, und übersteht eine Änderung am Muster.

---

`replacing(_:with:)` tauscht jede Übereinstimmung gegen einen festen Text und gibt einen neuen `String` zurück, ohne den ursprünglichen zu verändern:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Beachte, dass `\d+` eine ganze Folge von Ziffern durch ein einzelnes `#` ersetzt, während `\d` eine Ziffer nach der anderen ersetzen würde. Das Muster entscheidet, wie viel verschwindet.

---

`split(separator:)` akzeptiert ebenfalls einen Regex, wodurch ein einziger Aufruf Trenner behandeln kann, die nicht immer gleich geschrieben werden:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
Das Muster `[,;]\s*` bedeutet „ein Komma oder ein Semikolon, gefolgt von einer beliebigen Menge an Abstand“, daher wird jeder Trenner als Ganzes verbraucht und es entsteht kein leeres Feld. Das Ergebnis ist ein Array von `Substring`.

---

Einen ganzen Text mit `^` und `$` zu prüfen funktioniert, aber `wholeMatch(of:)` sagt es direkt: Es gibt nur dann eine Übereinstimmung zurück, wenn das Muster den Text vom ersten bis zum letzten Zeichen abdeckt, und sonst `nil`:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Verwende `firstMatch(of:)`, um etwas in einem Text zu finden, und `wholeMatch(of:)`, um zu prüfen, dass ein Text genau eine Form hat.

---

Ein `#/ ... /#`-Literal steht beim Kompilieren fest. Wenn das Muster erst zur Laufzeit bekannt wird, zum Beispiel weil ein Nutzer es eingegeben hat, baust du es mit `Regex(_:)`:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
Dieser Initialiser **wirft**: Ein ungültiges Muster wie `"["` wird erst entdeckt, während das Programm läuft, daher benötigt der Aufruf `try`, und der Fehler muss entweder mit `do`/`catch` (oder `try?`) behandelt oder durch das Markieren der umgebenden Funktion mit `throws` weitergereicht werden, wie es diese Übung tut. Ein so gebauter Regex hat keine zur Compilezeit bekannten nummerierten Eigenschaften, aber `contains`, `matches(of:)` und `replacing` funktionieren genau wie vorher.
