In Swift ist ein Fehler ein **Wert**, kein Absturz. Jeder Typ kann einer sein, indem er das `Error`-Protokoll implementiert, und eine Enumeration ist die übliche Wahl, weil ihre Fälle genau benennen, was schiefgehen kann:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
Eine Funktion, die fehlschlagen kann, wird mit `throws` markiert und meldet den Fehlschlag mit `throw`:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Der Aufruf einer solchen Funktion braucht `try`, und der Aufruf muss in einem `do`-Block stehen, auf den ein `catch`-Block folgt, der sagt, was bei einem Fehlschlag zu tun ist:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
Wenn `throw` läuft, wird der Rest des `do`-Blocks übersprungen und `catch` übernimmt. Nichts stürzt ab: Das Programm läuft nach dem `catch` weiter.

---

Eine werfende Funktion kann trotzdem einen Wert zurückgeben. Das Schlüsselwort `throws` steht zwischen der Parameterliste und dem Rückgabepfeil:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
Liest man ihn laut vor: *square nimmt ein `Int`, kann werfen und gibt ein `Int` zurück*.

An der Aufrufstelle existiert der Wert nur, wenn nichts geworfen wurde, deshalb steht die Zuweisung im `do`-Block:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
Das `try` ist keine optionale Verzierung: Der Compiler lehnt den Aufruf ohne es ab, sodass ein Leser immer sieht, welche Zeilen fehlschlagen können.

---

Ein bloßer `catch` behandelt jeden Fehler auf dieselbe Weise. Meist willst du auf einen bestimmten Fehlschlag reagieren, deshalb kann ein `catch` ein **Muster** tragen: den Fall, den er zu behandeln bereit ist.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift probiert die `catch`-Klauseln von oben nach unten durch und führt die erste aus, deren Muster passt.

Das letzte `catch` hat absichtlich kein Muster. Ein `catch` mit Muster deckt nur den Fall ab, den es nennt, und Swift besteht darauf, dass jeder Fehler irgendwo behandelt wird, deshalb braucht ein `do`-Block, der Muster auflistet, ein letztes musterloses `catch`, das den Rest auffängt.

---

Die Reihenfolge zählt. Swift vergleicht den geworfenen Wert mit jedem `catch`-Muster in der Reihenfolge, in der sie geschrieben sind, und stoppt beim ersten Treffer, deshalb würde ein musterloses `catch` an erster Stelle alles darunter verschlucken. Halte die speziellen Fälle oben und das alles abfangende `catch` unten.

Ein Fehler, auf den keines der Muster passt, wird nicht ignoriert: Er landet im letzten musterlosen `catch`.

---

Ein Fehlerfall kann Daten tragen. Gib dem Fall **assoziierte Werte** und das `throw` füllt sie aus, sodass der Handler nicht nur *was* fehlgeschlagen ist erfährt, sondern *um wie viel*:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
Das passende `catch` bindet diese Werte mit `let`:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
Den Namen nach `let` wählst du selbst; er ist eine neue Konstante, die nur innerhalb dieses `catch`-Blocks verfügbar ist. So trägt ein Fehler eine nützliche Nachricht, ohne dass du Zahlen an der Stelle, an der der Fehlschlag passiert, in Strings einfügen musst.

---

Eine Enumeration enthält meist alle Arten, wie eine einzelne Aufgabe fehlschlagen kann, einen Fall pro Grund:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Für jeden Fall ein eigenes `catch` zu schreiben wird repetitiv. Stattdessen fängst du den ganzen Typ auf einmal ab und machst ein `switch` über den Wert:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` bedeutet *fange alles, was ein `FormError` ist, und nenne es `error`*. Innerhalb des Blocks hat `error` den Enumerationstyp, daher sieht `switch` die Fälle und prüft, dass du alle abgedeckt hast. Das letzte musterlose `catch` ist trotzdem nötig, weil auch ein anderer Fehlertyp diesen `do`-Block erreichen könnte.

---

Ein Validator liest sich am besten, wenn die Zurückweisungen zuerst kommen und die eigentliche Arbeit unausgerückt unten steht. `guard` ist genau dafür gebaut: Er sieht die Bedingung vor, die gelten muss, und sein `else`-Block läuft, wenn sie nicht gilt.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
Der `else`-Block eines `guard` muss den aktuellen Gültigkeitsbereich verlassen, und `throw` ist eine der Möglichkeiten dafür, neben `return`, `break` und `continue`. Mehrere gestapelte `guard`s am Anfang einer Funktion lesen sich wie eine Liste der Regeln, die die Eingabe erfüllen muss.

---

Manchmal interessiert dich nicht *warum* etwas fehlgeschlagen ist, sondern nur, dass es passiert ist. `try?` macht aus einem werfenden Aufruf ein **Optional**: den Wert bei Erfolg, `nil` beim Werfen.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
Kein `do`, kein `catch`: Der Fehlschlag wird in das Optional hineingefaltet, dessen Entpacken du schon kennst. Der Preis dafür ist, dass der Fehlerwert weggeworfen wird, greife also nur zu `try?`, wenn es wirklich nichts zu melden gibt.

---

Weil `try?` ein Optional erzeugt, vollendet der Nil-Coalescing-Operator `??` die Arbeit, indem er einen Fallback liefert:
```swift
let port = (try? readPort(text)) ?? 8080
```
Die Klammern sind wichtig. Andernfalls würde `try?` versuchen, den ganzen Ausdruck inklusive `??` abzudecken, und der Compiler verlangt, dass du explizit sagst, wo der werfende Aufruf endet.

Lies die Zeile als einen Satz: *nimm den Port, den wir lesen konnten, sonst 8080*. Zwei Zeilen `do`/`catch` schrumpfen zu einer, wenn die Erholung wirklich nur ein Standardwert ist.

---

Es gibt eine dritte Form: `try!`. Sie sagt dem Compiler *dieser Aufruf kann nicht fehlschlagen*, also kein `do`, kein `catch` und kein Optional. Schlägt er dennoch fehl, stoppt das Programm sofort.
```swift
let pattern = try! Regex("[0-9]+")
```
Das ist die Form, in der `try!` vertretbar ist: Das Argument ist ein Literal, das du selbst in deinem eigenen Quellcode geschrieben hast, und wenn es falsch ist, ist das Programm kaputt und sollte schon beim ersten Testlauf stoppen.

Alles, was zur Laufzeit ankommt — eine Zeile, die ein Benutzer eintippt, eine Datei, eine Netzwerkantwort — kann auf Arten falsch sein, die du beim Schreiben des Codes nicht sehen kannst, und `try!` darauf macht aus einem behebbaren Fehlschlag einen Absturz vor den Augen des Benutzers. Verwende dort `do`/`catch` oder `try?`.

---

Wenn eine Funktion wirft, wird alles nach dem `throw` übersprungen — auch die Zeile, die die Datei schließen oder die Sperre freigeben sollte. `defer` löst das: Es registriert jetzt einen Block und führt ihn aus, wenn der aktuelle Gültigkeitsbereich endet, ganz gleich, wie er endet.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
Der Aufruf gibt `open` aus, dann `close`, und erst danach reist der Fehler zum Aufrufer weiter. Hätte die Funktion normal zurückgegeben, wäre `close` trotzdem ausgegeben worden — das ist der Punkt. Setze das Aufräumen direkt neben das Einrichten und sorge dich nicht mehr darum, welchen Ausgang der Code nimmt.

---

Ein Gültigkeitsbereich kann mehr als ein `defer` registrieren. Sie laufen in **umgekehrter** Reihenfolge: Das zuletzt registrierte läuft als erstes.

Das ist keine willkürliche Regel. Aufräumen macht normalerweise ein Einrichten rückgängig, das der Reihe nach geschah — öffne die Datei, dann sperre sie — und Rückgängigmachen muss andersherum laufen: entsperren, dann schließen. Die umgekehrte Reihenfolge macht jedes `defer` zum Spiegelbild der Zeile über ihm.

---

Eine Funktion, die eine Closure entgegennimmt, hat ein Problem: Sie kann nicht wissen, ob die ihr übergebene Closure wirft. Die Funktion mit `throws` zu markieren würde jeden Aufrufer zwingen, `try` zu schreiben, sogar die, die eine harmlose Closure übergeben. `rethrows` sagt *ich werfe nur, wenn die Closure, die du mir gegeben hast, wirft*:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Im Körper schreibst du trotzdem `try`, denn der Aufruf kann wirklich fehlschlagen. An der Aufrufstelle schaut der Compiler auf die Closure, die du übergeben hast:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // kein try nötig
```
Die Standardbibliothek nutzt das überall — `map`, `filter` und `sorted(by:)` sind alle `rethrows` — weshalb du nie `try` vor ein gewöhnliches `map` schreibst.

---

Ein `do`-Block ist nicht auf einen Fehlertyp beschränkt. Jeder Schritt kann auf seine eigene Weise fehlschlagen, und jeder Fehlschlag bekommt sein eigenes `catch`:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
Das erste `try`, das wirft, beendet den Block, daher laufen die späteren Schritte nie — der Wert existierte schlicht nie. Das macht diese Form lesbar: Der Happy Path bleibt oben in einer geraden Linie, und jede Art, wie er schiefgehen kann, ist darunter aufgelistet.
