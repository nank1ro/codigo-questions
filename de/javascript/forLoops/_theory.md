Wir wissen, wie man Code mit einer `while`-Schleife wiederholt.
Wie dieses Programm, das Anweisungen wiederholt, um `hello` anzuzeigen
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
Aber wir können das Gleiche mit `for`-Schleifen machen:
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

In einer `for`-Schleife können wir angeben, wie oft wir unsere Schleife ausführen möchten

---

Wir können `<` verwenden, um bis zur nächsten Zahl ausgeschlossen zu schleifen, oder `<=` um bis zur nächsten Zahl eingeschlossen zu schleifen

---

Die Variable namens `i` ist die Zählervariable.
Wir können ihr den Namen geben, den wir möchten.
Sie zählt, in welcher Wiederholung der Schleife wir uns gerade befinden

---

In JavaScript haben wir auch die `forEach`-Schleife.
Tatsächlich ruft `forEach` die gegebene Closure auf jedes Element in der Sequenz in der gleichen Reihenfolge wie eine `for`-Schleife auf:
```javascript
// this is an array, we'll see about that soon
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
Die Verwendung der `forEach`-Methode unterscheidet sich von einer `for`-Schleife auf zwei wichtige Arten:
1. Die `break`- oder `continue`-Anweisungen können nicht verwendet werden, um den aktuellen Aufruf der Body-Closure zu beenden oder nachfolgende Aufrufe zu überspringen.
2. Die Verwendung der `return`-Anweisung in der Body-Closure beendet nur die Closure und nicht den äußeren Bereich, und sie überspringt nicht nachfolgende Aufrufe.
HINWEIS: `=>` wird _Pfeilfunktion_ genannt und ist eine ES6-Kurzfunktionssyntax, die geschweifte Klammern {} ersetzt und den Wert zurückgibt (falls erforderlich)
