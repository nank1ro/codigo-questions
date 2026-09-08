Ein **Kommentar** ist Text in deinem Quellcode, der für Menschen gedacht ist, nicht für den Compiler. Der Compiler verwirft Kommentare, bevor er das Programm baut, sodass du sie verwenden kannst, um zu erklären, wofür der Code da ist, Erinnerungen zu hinterlassen oder eine Entscheidung festzuhalten.

Die häufigste Art ist der **einzeilige Kommentar**: Alles von `//` bis zum Ende dieser Zeile wird ignoriert.
```c
// Greet the user
printf("Hello\n");
```
Die erste Zeile tut nichts, wenn das Programm läuft; nur das `printf` erzeugt eine Ausgabe.

---

Da der Compiler Kommentare vollständig entfernt, ändert das Hinzufügen oder Löschen eines Kommentars nie, was ein Programm tut. Es läuft nur der Code, der **nicht** kommentiert ist.

Das macht `//` zu einem schnellen Weg, eine Codezeile abzuschalten, ohne sie zu löschen. Das nennt man **Auskommentieren**:
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
Die zweite Zeile ist jetzt ein Kommentar, also bleibt `total` `10`. Das Entfernen des `//` bringt die Zeile wieder zum Leben.

Auskommentieren ist praktisch, während du experimentierst, aber denke ans Aufräumen: Code, der lange auskommentiert bleibt, verwirrt nur diejenigen, die ihn als Nächstes lesen.

---

Wenn ein Kommentar mehr als eine Zeile braucht, bietet C den **mehrzeiligen Kommentar** (auch Blockkommentar genannt): Er beginnt mit `/*` und endet mit `*/`, und alles dazwischen wird ignoriert, einschließlich Zeilenumbrüchen.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
Ein Blockkommentar kann auch kurz sein und in einer Zeile bleiben: `/* like this */`.

Anders als `//`, das am Ende der Zeile stoppt, stoppt ein `/*`-Kommentar erst beim `*/`. Wenn du vergisst, ihn zu schließen, behandelt der Compiler den gesamten folgenden Code als Teil des Kommentars.

---

Blockkommentare **lassen sich nicht schachteln**. Der Compiler beendet einen `/*`-Kommentar beim allerersten `*/`, das er findet, egal wie viele `/*` davor kamen:
```c
/* outer /* inner */ still code */
```
Hier endet der Kommentar direkt nach `inner`, also wird `still code */` als Code kompiliert und erzeugt einen Fehler.

Das wird wichtig, wenn du einen Block auskommentieren willst, der bereits einen `/* */`-Kommentar enthält: Das innere `*/` würde deinen äußeren Kommentar zu früh schließen. Setze in dem Fall stattdessen `//` an den Anfang jeder Zeile.

---

Ein Kommentar braucht keine eigene Zeile: Er kann dem Code in derselben Zeile folgen. Das ist ein **nachgestellter Kommentar**, und er ist ein guter Platz für eine kurze Notiz zu genau dieser Anweisung:
```c
int retries = 3; // give up after three attempts
```
Sowohl `//` als auch `/* */` funktionieren als nachgestellte Kommentare, aber sei vorsichtig mit `/*`: Da er erst beim `*/` stoppt, verschluckt ein ungeschlossenes `/*` am Ende einer Zeile die Zeilen danach, und das Programm kompiliert nicht mehr.

---

Ein häufiger Einsatz von Blockkommentaren ist der **Header-Kommentar**: ein kurzer Block direkt über einer Funktion, der sagt, was sie tut, was ihre Parameter bedeuten und was sie zurückgibt.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
Wer `to_seconds` aufruft, kann jetzt den Header lesen statt den Funktionskörper. Halte den Header neben der Funktion, damit beide zusammen aktualisiert werden.

---

Der Compiler ersetzt jeden Kommentar durch ein einzelnes Leerzeichen. Das bedeutet, dass ein `/* */`-Kommentar überall stehen kann, wo ein Leerzeichen stehen kann, sogar mitten in einer Anweisung oder einem Ausdruck:
```c
int area = width /* cm */ * height /* cm */;
```
Das ist gelegentlich nützlich, um die Operanden oder die Argumente eines Aufrufs zu beschriften. Ein `//`-Kommentar kann das nicht, denn er würde den Rest der Zeile auskommentieren, einschließlich des Codes danach.

---

Programmierer verwenden einige konventionelle Schlüsselwörter am Anfang eines Kommentars, um unvollendete Arbeit zu kennzeichnen:

- `TODO` markiert etwas, das noch geschrieben werden muss
- `FIXME` markiert Code, von dem bekannt ist, dass er falsch ist, und der korrigiert werden muss

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Editoren und Tools können diese Markierungen auflisten, sodass die offene Arbeit leicht zu finden ist. Sobald die Arbeit erledigt ist, lösche die Markierung: Ein veraltetes `TODO` ist irreführend.

---

Ein guter Kommentar erklärt, **warum** der Code etwas tut, nicht **was** er tut. Der Code zeigt bereits, was passiert; ihn in Worten zu wiederholen fügt nur Rauschen hinzu und wird unzutreffend, sobald sich der Code ändert:
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
Der Grund hinter den Zahlen ist das, was ein Leser nicht erraten kann:
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
Wenn ein Kommentar nur die Zeile unter ihm wiederholt, lösche ihn oder ersetze ihn durch den Grund.

---

Alles zusammen: Verwende `//` für kurze Notizen und nachgestellte Kommentare, `/* */` für längere Blöcke und Header-Kommentare, kennzeichne unvollendete Arbeit mit `TODO` oder `FIXME` und entferne auskommentierten Code und veraltete Markierungen, sobald sie nicht mehr gebraucht werden.
