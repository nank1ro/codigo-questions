Ein **formatierter String** ist ein Text, bei dem einige Teile zur Laufzeit mit Werten gefüllt werden: ein Preis, ein Name, ein Punktestand. Swift gibt dir dafür zwei Werkzeuge.

Das erste ist die **Zeichenketteninterpolation**, die du bereits kennst: Alles, was innerhalb von `\( )` geschrieben steht, wird ausgewertet und in den Text eingefügt. Es muss keine Variable sein, es kann ein beliebiger Ausdruck sein:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
Interpolation ist der schnellste Weg, einen String zu erzeugen, aber sie gibt Zahlen genau so aus, wie Swift sie speichert: `3.5` bleibt `3.5`, nie `3.50`. Für die volle Kontrolle über Ziffern, Breite und Auffüllung verwenden wir `String(format:)`, das in der nächsten Übung vorgestellt wird.

---

Das zweite Werkzeug ist `String(format:)`, das aus dem Framework **Foundation** stammt, daher muss die Datei mit `import Foundation` beginnen.

Es nimmt einen **Formatstring** entgegen, gefolgt von den einzufügenden Werten. Innerhalb des Formatstrings markiert ein **Spezifizierer**, der mit `%` beginnt, wo jeder Wert eingefügt wird und wie er geschrieben wird. Der Spezifizierer für eine ganze Zahl ist `%d`:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` gibt einen normalen `String` zurück, den du ausgeben, speichern oder aus einer Funktion zurückgeben kannst.

---

Für Dezimalzahlen (`Double`) ist der Spezifizierer `%f`. Für sich allein gibt er immer sechs Ziffern nach dem Punkt aus:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
Um zu wählen, wie viele Dezimalstellen du möchtest, schreibe einen Punkt und eine Zahl zwischen `%` und `f`. Das ist die **Präzision**, und der Wert wird entsprechend gerundet:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` ist die übliche Wahl für Preise, weil er immer genau zwei Dezimalstellen zeigt.

---

Eine Zahl zwischen `%` und dem Buchstaben legt die **Mindestbreite** des Feldes fest. Ist der Wert kürzer, werden links Leerzeichen hinzugefügt, sodass er **rechtsbündig** ausgerichtet ist; ist er länger, wird nichts abgeschnitten:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
Breite und Präzision lassen sich kombinieren: `%8.2f` bedeutet "mindestens 8 Zeichen breit, mit 2 Dezimalstellen":
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
Durch feste Breiten werden die Spalten einer Tabelle ausgerichtet.

---

Standardmäßig erfolgt die Auffüllung auf der linken Seite. Ein Minuszeichen direkt nach `%` legt die Auffüllung stattdessen auf die rechte Seite, sodass der Wert **linksbündig** ausgerichtet ist:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
Das Minuszeichen ist eine **Flag**: Sie ändert, wie das Feld gefüllt wird, ohne die Breite zu verändern.

---

Eine weitere Flag ist `0`: Statt mit Leerzeichen wird das Feld links mit Nullen gefüllt. So erhält man Zahlen wie `007` oder `00042`:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
Wie bei Leerzeichen wird ein Wert, der länger als die Breite ist, nie abgeschnitten.

---

Ein Formatstring kann so viele Spezifizierer enthalten, wie du möchtest. Die Werte folgen in derselben Reihenfolge, getrennt durch Kommas, und jeder muss zum Typ seines Spezifizierers passen: `%d` für ein `Int`, `%f` für ein `Double`:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Ein `Double` an `%d` zu übergeben (oder ein `Int` an `%f`) kompiliert, gibt aber eine bedeutungslose Zahl aus, prüfe also immer, ob Spezifizierer und Werte zusammenpassen.

---

Ganze Zahlen kann man auch in anderen Basen schreiben. `%x` gibt den Wert in **Hexadezimal** mit Kleinbuchstaben aus, `%X` mit Großbuchstaben und `%o` in Oktal:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
Breite und die `0`-Flag funktionieren hier ebenfalls: `%02x` ist die klassische Art, ein Byte einer Farbe zu schreiben, wie in `#ff8000`.

---

Um einen `String` in einen Formatstring einzufügen, verwende den Spezifizierer `%@`:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` akzeptiert einen Swift-`String` direkt. Verwende `%s` nicht mit einem Swift-String: Dieser Spezifizierer erwartet einen C-String und gibt Datenmüll aus oder stürzt ab.
