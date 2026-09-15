Ein **Kommentar** ist eine Notiz im Quellcode für die Menschen, die ihn lesen. Der Compiler ignoriert Kommentare vollständig, sie ändern also nie, was das Programm tut.

Der einfachste Kommentar ist der **einzeilige Kommentar**: er beginnt mit `//` und reicht bis zum Ende der Zeile.
```kotlin
// Begrüßt den Benutzer
println("Hello")
```
Verwende Kommentare, um zu erklären, wofür ein Stück Code gedacht ist oder warum es so geschrieben wurde.

---

Ein Kommentar braucht keine eigene Zeile: er kann dem Code in derselben Zeile folgen. Das ist ein **Kommentar am Zeilenende**, ein guter Platz für eine kurze Notiz zu genau dieser Anweisung:
```kotlin
val retries = 3 // nach drei Versuchen aufgeben
```
Alles von `//` bis zum Ende der Zeile wird ignoriert, während der Code davor wie üblich läuft.

---

Da der Compiler Kommentare vollständig entfernt, ändert das Hinzufügen oder Löschen eines Kommentars nie, was ein Programm tut. Es läuft nur der Code, der **nicht** auskommentiert ist.

Deshalb ist `//` ein schneller Weg, eine Codezeile abzuschalten, ohne sie zu löschen. Das nennt man **Auskommentieren**:
```kotlin
var total = 10
// total = total + 5
println(total) // gibt 10 aus
```
Die zweite Zeile ist jetzt ein Kommentar, `total` bleibt also `10`. Entfernt man das `//`, lebt die Zeile wieder auf.

Auskommentieren ist praktisch, während du experimentierst, aber denk ans Aufräumen: Code, der lange auskommentiert stehen bleibt, verwirrt nur die Person, die ihn als Nächstes liest.

---

Wenn ein Kommentar mehr als eine Zeile braucht, bietet Kotlin den **mehrzeiligen Kommentar** (auch Blockkommentar genannt) an: er beginnt mit `/*` und endet mit `*/`, und alles dazwischen wird ignoriert, auch Zeilenumbrüche.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
Ein Blockkommentar kann auch kurz sein und in einer Zeile bleiben: `/* like this */`.

---

Anders als `//`, das am Ende der Zeile stoppt, stoppt ein `/*`-Kommentar erst beim `*/`. Vergisst du ihn zu schließen, behandelt der Compiler den gesamten folgenden Code als Teil des Kommentars und meldet einen Fehler:
```kotlin
val width = 10 /* in Zentimetern
println(width) // noch innerhalb des Kommentars: Fehler, der Kommentar wird nie geschlossen
```
Sowohl `//` als auch `/* */` funktionieren als Kommentar am Zeilenende, aber bei `/*` vergewissere dich immer, dass das `*/` vorhanden ist.

---

In Java kann ein Blockkommentar keinen weiteren Blockkommentar enthalten, in Kotlin können sie **geschachtelt** werden: jedes `/*` muss von seinem eigenen `*/` abgeschlossen werden, und der Kommentar endet erst, wenn der äußerste geschlossen ist.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Hier ist `still a comment */` Teil des äußeren Kommentars, es wird also nur `done` ausgegeben. Das ermöglicht es dir, einen ganzen Codeblock auszukommentieren, selbst wenn dieser Block bereits einen `/* */`-Kommentar enthält.

---

Um mehrere Zeilen auf einmal auszukommentieren, wickle sie in einen einzigen Blockkommentar, statt an jede Zeile ein `//` zu hängen:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // gibt 100 aus
```
Dank der Schachtelung funktioniert das sogar, wenn eine dieser Zeilen bereits einen `/* */`-Kommentar enthält.

---

Eine übliche Verwendung von Blockkommentaren ist der **Header-Kommentar**: ein kurzer Block direkt über einer Funktion, der sagt, was sie tut und was ihre Parameter bedeuten.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Wer `toSeconds` aufruft, kann jetzt den Header lesen statt des Funktionskörpers. Lass den Header neben der Funktion stehen, damit beide zusammen aktualisiert werden.

---

Kotlin hat eine dritte Art von Kommentar, den **Dokumentationskommentar**, geschrieben in einem Format namens **KDoc**: er beginnt mit `/**` (ein Schrägstrich und zwei Sterne) und endet mit `*/`, und er steht direkt über einer Funktion, einer Klasse oder einer Eigenschaft.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
Für den Compiler ist er nur ein Kommentar, aber Tools wie IntelliJ IDEA lesen ihn und zeigen ihn als Hilfetext für `greet` an. Das `*` am Anfang der inneren Zeilen ist nur eine Konvention, die den Block ausrichtet. Innerhalb von KDoc kannst du Markdown verwenden, und eckige Klammern wie `[name]` werden zu Links auf diesen Parameter.

---

Die erste Zeile eines Dokumentationskommentars ist die **Zusammenfassung**: ein kurzer Satz, der sagt, was die Funktion tut. Schreibe ihn in der dritten Person, als würdest du die Funktion beschreiben: "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
Der Kommentar muss direkt über der Deklaration stehen, ohne eine andere Anweisung dazwischen, sonst hängen die Tools ihn nicht an die Funktion an.

---

Nach der Zusammenfassung kann ein Dokumentationskommentar die Parameter und den Rückgabewert mit **KDoc-Tags** beschreiben, die immer mit `@` beginnen:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Auf `@param` folgen der Name des Parameters und dann seine Beschreibung; es gibt ein `@param` pro Parameter. `@return` beschreibt den Wert, den die Funktion zurückgibt. Die Reihenfolge ist immer dieselbe: zuerst die Zusammenfassung, dann die `@param`-Tags, dann `@return`.

---

Eine Funktion mit mehr als einem Parameter bekommt für jeden davon ein `@param`-Tag, geschrieben in derselben Reihenfolge wie die Parameter:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
Ein Tag ist trotzdem nur ein Kommentar: benennst du einen Parameter um und vergisst das Tag, geht nichts kaputt, aber die Dokumentation beginnt zu lügen. Aktualisiere das KDoc zusammen mit der Signatur.

---

Der Compiler sucht Kommentare nur im Code, niemals innerhalb eines **String-Literals**. Zwischen doppelten Anführungszeichen sind `//` und `/* */` ganz normale Zeichen:
```kotlin
println("50 // 2") // prints 50 // 2
```
Das erste `//` ist Teil des Texts, das zweite startet einen echten Kommentar. Am häufigsten überrascht das bei Webadressen, die direkt nach dem Protokoll ein `//` enthalten.

---

Manche Kommentare folgen einer Konvention, die Editoren verstehen. Die häufigsten **Marker** sind:
- `// TODO: ...` markiert etwas, das noch geschrieben werden muss
- `// FIXME: ...` markiert Code, von dem bekannt ist, dass er falsch ist und korrigiert werden muss

```kotlin
val limit = 10
// TODO: das Limit aus den Einstellungen lesen
```
Für den Compiler sind sie ganz normale Kommentare; IntelliJ IDEA sammelt sie in einem eigenen Tool-Fenster, damit offene Arbeit leicht zu finden ist. Ein `TODO` steht meist neben einem Platzhalter, der den Code kompilierfähig hält, bis die echte Implementierung geschrieben ist. Wenn du die Arbeit abschließt, ersetze den Platzhalter und entferne den Marker in derselben Änderung, damit der Kommentar nie etwas über den Zustand des Codes vortäuscht.

---

Ein `FIXME` ist etwas anderes als ein `TODO`: der Code existiert bereits, aber es ist bekannt, dass er falsch ist. Ein gutes `FIXME` sagt, was der Fehler ist, und gibt — wenn möglich — ein Beispiel, das ihn zeigt, damit die nächste Person ihn schnell beheben kann. Wie beim `TODO` gilt: Lösche den Marker, sobald der Fehler behoben ist, aber behalte den Dokumentationskommentar, der weiterhin stimmt.

---

Ein guter Kommentar erklärt, **warum** der Code etwas tut, nicht **was** er tut. Der Code zeigt bereits, was passiert; es in Worten zu wiederholen fügt nur Rauschen hinzu und veraltet, sobald sich der Code ändert:
```kotlin
// timeout auf 30 setzen
val timeout = 30
```
Der Grund hinter der Zahl ist das, was man als Leser nicht erraten kann:
```kotlin
// der Server trennt inaktive Verbindungen nach 35 Sekunden, also lieber früher aufhören
val timeout = 30
```
Wiederholt ein Kommentar nur die Zeile unter ihm, lösche ihn oder ersetze ihn durch den Grund. Die besten Kommentare sind die, die etwas sagen, das der Code nicht sagen kann.
