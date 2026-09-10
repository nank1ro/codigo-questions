Ein **Kommentar** ist eine Notiz, die im Quellcode für die Menschen steht, die ihn lesen. JavaScript ignoriert Kommentare vollständig, sie ändern also nie, was das Programm tut.

Der einfachste Kommentar ist der **einzeilige Kommentar**: Er beginnt mit `//` und läuft bis zum Ende der Zeile.
```javascript
// Greets the user
console.log("Hello");
```
Verwende Kommentare, um zu erklären, wofür ein Stück Code da ist oder warum es so geschrieben wurde. Beachte, dass `#` in JavaScript, anders als in manchen anderen Sprachen, **keinen** Kommentar beginnt.

---

Ein Kommentar braucht keine eigene Zeile: Er kann dem Code in derselben Zeile folgen. Das ist ein **Inline-Kommentar** (oder nachgestellter Kommentar), und er ist ein guter Platz für eine kurze Notiz zu genau dieser Anweisung:
```javascript
const retries = 3; // give up after three attempts
```
Alles von `//` bis zum Zeilenende wird ignoriert, während der Code davor wie gewohnt ausgeführt wird.

---

Da Kommentare ignoriert werden, ändert das Hinzufügen oder Löschen eines Kommentars nie, was ein Programm tut. Nur der Code, der **nicht** auskommentiert ist, läuft.

Damit ist `//` ein schneller Weg, eine Codezeile abzuschalten, ohne sie zu löschen. Das nennt man **Auskommentieren**:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
Die zweite Zeile ist jetzt ein Kommentar, also bleibt `total` bei `10`. Entfernt man das `//`, erwacht die Zeile wieder zum Leben.

Auskommentieren ist praktisch beim Experimentieren, aber denk ans Aufräumen: Code, der lange auskommentiert bleibt, verwirrt nur die nächste Person, die ihn liest.

---

Wenn ein Kommentar mehr als eine Zeile braucht, bietet JavaScript den **mehrzeiligen Kommentar** (auch Blockkommentar genannt): Er beginnt mit `/*` und endet mit `*/`, und alles dazwischen wird ignoriert, einschließlich der Zeilenumbrüche.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
Ein Blockkommentar kann auch kurz sein und auf einer Zeile bleiben: `/* like this */`.

---

Welche Art von Kommentar du auch verwendest, die Regel ist dieselbe: Der Text darin ist **kein Code**. Ein `console.log` in einem Kommentar gibt nie etwas aus, und Code, der nach `//` in derselben Zeile steht, läuft nie, selbst wenn die Zeile mit echtem Code beginnt:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
Wenn du dir nicht sicher bist, was ein Programm ausgibt, streiche gedanklich jeden Kommentar und lies, was übrig bleibt.

---

Anders als `//`, das am Zeilenende aufhört, endet ein `/*`-Kommentar erst beim `*/`. Wenn du vergisst, ihn zu schließen, behandelt JavaScript den gesamten folgenden Code als Teil des Kommentars und meldet einen Syntaxfehler:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
Sowohl `//` als auch `/* */` funktionieren als Inline-Kommentare, aber bei `/*` musst du immer sicherstellen, dass das `*/` da ist.

---

Blockkommentare können in JavaScript **nicht verschachtelt werden**: Der Kommentar endet beim **ersten** `*/`, auf das er trifft, egal wie viele `/*` davor standen.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Hier endet der Kommentar direkt nach `inner`, also wird `still a comment */` als Code gelesen und verursacht einen Syntaxfehler. Denk daran, wenn du einen Block auskommentierst, der bereits einen `/* */`-Kommentar enthält: Nimm stattdessen `//` in jeder Zeile oder entferne zuerst den inneren Kommentar.

---

Um mehrere Zeilen auf einmal auszukommentieren, umschließe sie mit einem einzigen Blockkommentar, statt jeder Zeile ein `//` voranzustellen:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Da die Zeilen im Block ignoriert werden, ändert sich `total` nie. Denk daran, dass das nur funktioniert, wenn keine dieser Zeilen ein `*/` enthält.

---

JavaScript hat eine dritte Art von Kommentar, den **Dokumentationskommentar**, geschrieben im **JSDoc**-Format: ein Blockkommentar, der mit `/**` (zwei Sternchen) beginnt und direkt über einer Funktion steht. Darin beginnen die Zeilen meist mit ` * `, und spezielle **Tags**, die mit `@` anfangen, beschreiben die Funktion:
- `@param {type} name description` für jeden Parameter
- `@returns {type} description` für den Rückgabewert

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
Für JavaScript ist es nur ein Kommentar, aber Editoren lesen ihn und zeigen ihn als Hilfetext für `greet` an, zusammen mit dem Typ in geschweiften Klammern (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

Die erste Zeile eines JSDoc-Kommentars ist die **Zusammenfassung**: ein kurzer Satz, der sagt, was die Funktion tut. Schreibe ihn in der dritten Person, als würdest du die Funktion beschreiben: "Returns...", "Adds...", "Checks...". Danach listest du die Tags auf, eines pro Zeile:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
Der Kommentar muss direkt über der Deklaration stehen, ohne Leerzeile dazwischen, sonst ordnen Editoren ihn der Funktion nicht zu.

---

Ein JSDoc-Kommentar ist auch ein **Vertrag**: Er sagt demjenigen, der die Funktion aufruft, was er übergeben muss und was er zurückbekommt, noch bevor der Rumpf geschrieben ist. Den Kommentar zu lesen reicht oft aus, um die Funktion zu implementieren:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Jedes `@param` gehört zu einem Parameter, in derselben Reihenfolge, und `@returns` beschreibt jedes mögliche Ergebnis.

---

Die Reihenfolge in einem JSDoc-Kommentar ist immer dieselbe: zuerst die Zusammenfassung, dann ein `@param` pro Parameter in der Reihenfolge ihrer Deklaration, dann zuletzt `@returns`. Das öffnende `/**` und das schließende ` */` umschließen alles, und der Kommentar steht direkt über der Funktion, die er beschreibt:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

Eine JavaScript-Datei kann mit einer besonderen Zeile beginnen, dem **Shebang** (oder Hashbang): `#!` gefolgt vom Pfad des Programms, das die Datei ausführen soll. Auf unixartigen Systemen kannst du damit ein Skript direkt vom Terminal starten, etwa `./hello.js`, ohne vorher `node` zu tippen:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript ignoriert diese Zeile genau wie einen Kommentar, aber nur, wenn sie die **allererste Zeile** der Datei ist: an jeder anderen Stelle ist `#!` ein Syntaxfehler. `/usr/bin/env node` bedeutet "finde `node` auf diesem System und verwende es".

---

Ein guter Kommentar erklärt, **warum** der Code etwas tut, nicht **was** er tut. Der Code zeigt schon, was passiert; es in Worten zu wiederholen erzeugt nur Rauschen und veraltet, sobald sich der Code ändert:
```javascript
// set timeout to 30
const timeout = 30;
```
Der Grund hinter der Zahl ist das, was ein Leser nicht erraten kann:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
Wenn ein Kommentar nur die Zeile darunter wiederholt, lösche ihn oder ersetze ihn durch den Grund.

---

Manche Kommentare folgen einer Konvention, die Editoren verstehen. Die häufigsten **Marker** sind:
- `// TODO: ...` weist auf etwas hin, das noch geschrieben werden muss
- `// FIXME: ...` weist auf Code hin, von dem man weiß, dass er falsch ist und korrigiert werden muss

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Für JavaScript sind das ganz gewöhnliche Kommentare; Editoren listen sie auf, damit offene Arbeit leicht zu finden ist. Ein `TODO` steht meist neben einem Platzhalter, der den Code am Laufen hält, bis die echte Implementierung geschrieben ist. Wenn du die Arbeit erledigt hast, ersetze den Platzhalter und entferne den Marker in derselben Änderung: Ein veraltetes `TODO` führt in die Irre.

---

Ein `FIXME` unterscheidet sich von einem `TODO`: Der Code existiert bereits, aber man weiß, dass er falsch ist. Ein gutes `FIXME` sagt, worin der Fehler besteht, und gibt nach Möglichkeit ein Beispiel, das ihn zeigt, damit die nächste Person ihn schnell beheben kann. Wie beim `TODO` löschst du den Marker, sobald der Fehler behoben ist, behältst aber den JSDoc-Kommentar, der weiterhin stimmt.
