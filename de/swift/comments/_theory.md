Ein **Kommentar** ist eine Notiz im Quellcode, geschrieben für die Menschen, die ihn lesen. Der Compiler ignoriert Kommentare vollständig, deshalb ändern sie nie, was das Programm tut.

Der einfachste Kommentar ist der **einzeilige Kommentar**: Er beginnt mit `//` und reicht bis zum Ende der Zeile.
```swift
// Greets the user
print("Hello")
```
Verwende Kommentare, um zu erklären, wozu ein Codeabschnitt dient oder warum er so geschrieben wurde.

---

Ein Kommentar braucht keine eigene Zeile: Er kann auf derselben Zeile hinter dem Code folgen. Das ist ein **nachstehender Kommentar**, und er ist ein guter Platz für eine kurze Notiz zu genau dieser Anweisung:
```swift
let retries = 3 // give up after three attempts
```
Alles von `//` bis zum Ende der Zeile wird ignoriert, während der Code davor wie üblich ausgeführt wird.

---

Da der Compiler Kommentare vollständig entfernt, ändert das Hinzufügen oder Löschen eines Kommentars nie, was ein Programm tut. Es läuft nur der Code, der **nicht** auskommentiert ist.

Das macht `//` zu einer schnellen Möglichkeit, eine Codezeile abzuschalten, ohne sie zu löschen. Das nennt man **Auskommentieren**:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
Die zweite Zeile ist jetzt ein Kommentar, deshalb bleibt `total` `10`. Entfernt man das `//`, lebt die Zeile wieder auf.

Auskommentieren ist praktisch, während du experimentierst, aber denk daran, aufzuräumen: Code, der lange auskommentiert bleibt, verwirrt nur diejenigen, die ihn als Nächstes lesen.

---

Wenn ein Kommentar mehr als eine Zeile braucht, bietet Swift den **mehrzeiligen Kommentar** (auch Blockkommentar genannt) an: Er beginnt mit `/*` und endet mit `*/`, und alles dazwischen wird ignoriert, einschließlich der Zeilenumbrüche.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
Ein Blockkommentar kann auch kurz sein und auf einer Zeile bleiben: `/* like this */`.

---

Anders als `//`, das am Ende der Zeile stoppt, stoppt ein `/*`-Kommentar erst beim `*/`. Vergisst du ihn zu schließen, behandelt den Compiler den gesamten folgenden Code als Teil des Kommentars und meldet einen Fehler:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
Sowohl `//` als auch `/* */` funktionieren als nachstehende Kommentare, aber bei `/*` musst du immer sicherstellen, dass das `*/` vorhanden ist.

---

In vielen Sprachen können Blockkommentare keine anderen Blockkommentare enthalten, in Swift können sie **verschachtelt** werden: Auf jedes `/*` muss sein eigenes `*/` folgen, und der Kommentar endet erst, wenn der äußerste geschlossen wird.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Hier ist `still a comment */` Teil des äußeren Kommentars, deshalb wird nur `done` ausgegeben. Dadurch kannst du einen ganzen Codeblock auskommentieren, selbst wenn dieser Block bereits einen `/* */`-Kommentar enthält.

---

Um mehrere Zeilen auf einmal auszukommentieren, umgib sie mit einem einzigen Blockkommentar, statt zu jeder Zeile `//` hinzuzufügen:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Dank der Verschachtelung funktioniert das sogar, wenn eine dieser Zeilen bereits einen `/* */`-Kommentar enthält.

---

Eine häufige Verwendung von Blockkommentaren ist der **Header-Kommentar**: ein kurzer Block direkt über einer Funktion, der sagt, was sie tut und was ihre Parameter bedeuten.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Wer `toSeconds` aufruft, kann nun den Header lesen statt des Funktionskörpers. Lasse den Header neben der Funktion, damit beide zusammen aktualisiert werden.

---

Swift hat eine dritte Art von Kommentar, den **Dokumentationskommentar**: einen einzeiligen Kommentar, der mit `///` (drei Schrägstriche) beginnt und direkt über einer Funktion, einem Typ oder einer Eigenschaft steht.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
Für den Compiler ist er nur ein Kommentar, aber Tools wie Xcode lesen ihn und zeigen ihn als Hilfetext für `greet` an. Dokumentationskommentare unterstützen **Markdown**, deshalb kannst du Backticks für Code, `**fett**` und Listen verwenden.

---

Die erste Zeile eines Dokumentationskommentars ist die **Zusammenfassung**: ein kurzer Satz, der sagt, was die Funktion tut. Schreibe ihn in der dritten Person, als würdest du die Funktion beschreiben: „Returns…", „Adds…", „Checks…".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
Der Kommentar muss direkt über der Deklaration stehen, ohne Leerzeile dazwischen, sonst hängt Xcode ihn nicht an die Funktion an.

---

Dokumentationskommentare gibt es auch in Blockform: `/**` öffnet sie und `*/` schließt sie, genau wie ein mehrzeiliger Kommentar, nur mit einem zweiten Sternchen am Anfang.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// text` und `/** text */` bedeuten für die Tools dasselbe; `///` ist die häufigste Wahl in Swift-Code, während `/** */` praktisch für lange Beschreibungen ist. Ein gewöhnlicher `/* */`- oder `//`-Kommentar ist **keine** Dokumentation, selbst wenn er über einer Funktion steht.

---

Nach der Zusammenfassung kann ein Dokumentationskommentar die Parameter und den Rückgabewert mit besonderen Markdown-Listeneinträgen beschreiben, die Xcode erkennt:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Die Reihenfolge ist immer dieselbe: zuerst die Zusammenfassung, dann `- Parameter name:` für jeden Parameter, dann `- Returns:`.

---

Manche Kommentare folgen einer Konvention, die Editoren verstehen. In Swift sind die häufigsten **Marker**:
- `// MARK: - Titel` kennzeichnet einen Abschnitt der Datei, sodass er im Navigationsmenü von Xcode erscheint
- `// TODO: ...` markiert etwas, das noch geschrieben werden muss
- `// FIXME: ...` markiert Code, von dem bekannt ist, dass er falsch ist und korrigiert werden muss

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Für den Compiler sind es gewöhnliche Kommentare; Xcode listet sie auf, damit ausstehende Arbeit leicht zu finden ist. Sobald die Arbeit erledigt ist, lösche den Marker: ein veraltetes `TODO` führt in die Irre.

---

Ein `TODO` steht meist neben einem Platzhalter, der den Code kompilierbar hält, bis die eigentliche Implementierung geschrieben ist. Wenn du die Arbeit erledigst, ersetze den Platzhalter und entferne den Marker in derselben Änderung, damit der Kommentar nie etwas Falsches über den Zustand des Codes behauptet.

---

Ein `FIXME` unterscheidet sich von einem `TODO`: Der Code existiert bereits, ist aber bekanntermaßen falsch. Ein gutes `FIXME` sagt, worin der Fehler besteht, und gibt nach Möglichkeit ein Beispiel an, das ihn zeigt, damit die nächste Person ihn schnell beheben kann. Wie beim `TODO` löschst du den Marker, sobald der Fehler behoben ist, behältst aber den Dokumentationskommentar, der weiterhin zutrifft.

---

Ein guter Kommentar erklärt, **warum** der Code etwas tut, nicht **was** er tut. Der Code zeigt bereits, was passiert; das in Worten zu wiederholen erzeugt nur Rauschen und veraltet, sobald sich der Code ändert:
```swift
// set timeout to 30
let timeout = 30
```
Der Grund hinter der Zahl ist das, was eine Leserin nicht erraten kann:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
Wenn ein Kommentar nur die Zeile darunter wiederholt, lösche ihn oder ersetze ihn durch den Grund.
