Arrays sind ein Datentyp, mit dem du eine Sammlung verschiedener Informationen als Sequenz unter einem einzelnen Variablennamen speichern kannst.
Ein Array speichert mehrere Werte eines oder mehrerer Typen und verwendet **Indizes**, um diese Werte zu unterscheiden.
Sie können Elemente einem Array mit einem Ausdruck der folgenden Form zuweisen:
```javascript
var arrayName = [item1, item2];
```

---

Du kannst auf ein einzelnes Element des Arrays über seinen Index zugreifen.
Ein Index ist wie eine Adresse, die die Position des Elements im Array identifiziert.
Der Index erscheint direkt nach dem Array-Namen, zwischen Klammern, wie folgt:
```javascript
arrayName[index];
```
Array-Indizes beginnen mit `0`, **nicht** `1`! Du greifst auf das erste Element eines Arrays so zu: `arrayName[0]`.
Das zweite Element in einem Array hat den Index 1: `arrayName[1]`.

---

Ein Array-Index verhält sich wie jeder andere Variablenname.
Er kann sowohl zum Zugriff als auch zum Zuweisen von Werten verwendet werden.
Du hast gesehen, wie man auf einen Array-Index so zugreift:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Druckt den Wert "Jeremiah"
console.log(names[0]);
```
So funktioniert eine Zuweisung:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Weise den neuen Wert "Jordan" zu
names[0] = "Jordan";
// Druckt den Wert "Jordan"
console.log(names[0]);
```

---

Genau wie Strings haben auch Arrays eine **Länge**.
Die Länge eines Arrays ist die Anzahl der Elemente, die es enthält

---

Ein Array muss keine feste Länge haben.
Du kannst jederzeit Elemente am Ende eines Arrays hinzufügen!
Um ein Element zu einem Array hinzuzufügen, verwenden wir die `push`-Funktion:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Druckt ["a", "b", "c"]
```

---

Manchmal möchtest du nur auf einen Teil eines Arrays zugreifen.
Betrachte den folgenden Code:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// druckt [2, 3]
```
Zuerst erstellen wir ein Array namens `numbers`.
Dann nehmen wir einen Abschnitt des Arrays und speichern ihn im Slice-Array.
Das tun wir, indem wir die Indizes definieren, die wir nach dem Namen des Arrays einbeziehen möchten: `numbers.slice(1, 3)`.
Denke daran, dass der rechte Index ausgeschlossen ist

---

In JavaScript können wir ein Array teilen, wie wir möchten!
```javascript
// Nimmt die ersten zwei Elemente
listName.slice(0, 2);
// Nimmt die vierte bis zur letzten Element
listName.slice(3);
```
Wenn dein Array-Slice das erste oder letzte Element im Array einbezieht, muss der Index für dieses Element nicht eingegeben werden

---

Array-Elemente können von jedem Typ sein.
```javascript
var arrayName = ["one", 2, true];
```
Tatsächlich haben wir oben der Reihe nach einen String, eine Ganzzahl und einen Boolean.
Aber wir können auch Arrays mit Arrays haben!

---

Manchmal musst du nach einem Element in einem Array suchen.
In JavaScript können wir die `indexOf()`-Methode verwenden:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// druckt 1
```
Der Code oben druckt den ersten Index, der den String `"Zac"` enthält, in diesem Fall `1`.
Wir können auch Elemente mit der `splice()`-Methode an einem bestimmten Index in ein Array einfügen:
```javascript
names.splice(1, 0, "Ali");
// druckt ["Trevor", "Ali", "Zac", "Glenn"]
```
Der Code oben fügt `"Ali"` am Index `1` ein, was alles nach diesem Index um 1 verschiebt.
Der zweite Wert `0` bedeutet _deleteCount_, in diesem Fall löschen wir kein Element aus dem Array; aber wenn wir `1` angegeben hätten, würde der Wert `Zac` aus dem Array entfernt

---

In JavaScript können wir auf sehr einfache Weise mit den `for..of`-Schlüsselwörtern durch ein Array schleifen:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// druckt 1, 2, 3
```
Dem `for`-Schlüsselwort folgt ein Variablenname, dem der Wert jedes Array-Elements nacheinander zugewiesen wird.
