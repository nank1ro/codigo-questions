Entscheidungsfindung ist erforderlich, wenn wir Code nur unter bestimmten Bedingungen ausführen möchten.
Angenommen, wir möchten nur dann nach draußen gehen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `niceWeather` speichern und die Aktion `if` diese Variable `true` ist, wie folgt ausführen:
```javascript
var niceWeather = true;
if (niceWeather) {
    // draußen spielen
}
```

---

Lassen Sie uns das vorherige Beispiel fortsetzen.
```javascript
var niceWeather = true;
if (niceWeather) {
    // draußen spielen
}
```
Wir haben gesehen, dass die `if`-Anweisung den Codeblock nur ausführt, wenn die Bedingung `true` ist.
Ein weiteres wichtiges Merkmal sind die **geschwungenen Klammern** `{}`, die einen Codeblock anzeigen.

---

Wir haben gerade gesehen, wie man einen Codeblock ausführt, wenn eine Bedingung erfüllt ist. Jetzt schauen wir uns an, wie man einen anderen Codeblock ausführt, wenn die erste Bedingung nicht erfüllt ist.
Wir gehen nach draußen, wenn das Wetter schön ist; ansonsten bleiben wir zu Hause.
In JavaScript können wir die `else`-Anweisung verwenden:
```javascript
var niceWeather = true;
if (niceWeather) {
    // draußen spielen
} else {
    // zu Hause bleiben
}
```

---

Angenommen, wir haben eine weitere Bedingung zu überprüfen, wie in diesem Beispiel:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
und die Ausgabe dieses Codes ist `the number is 3`.
Zunächst überprüfen wir, ob die Zahl gleich 2 ist, dies ist falsch.
Also gehen wir zur zweiten Anweisung über und überprüfen, ob `num` gleich 3 ist. Da dies wahr ist, führen wir den folgenden Codeblock aus, indem wir `the number is 3` ausgeben.

---

Wir können so viele `else if`-Anweisungen hinzufügen, wie wir möchten, es gibt keine Grenzen
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Wir können auch eine Bedingungsanweisung (`if`, `else if` oder `else`) in einer anderen Bedingungsanweisung verschachteln, um eine komplexere Struktur zu schaffen.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Der ternäre Bedingungsoperator ist ein spezieller Operator mit drei Teilen, der die Form `question ? answer1 : answer2` annimmt.
Es ist eine Abkürzung für die Auswertung eines von zwei Ausdrücken, je nachdem, ob `question` wahr oder falsch ist.
Wenn `question` wahr ist, wertet es `answer1` aus und gibt seinen Wert zurück; ansonsten wertet es `answer2` aus und gibt seinen Wert zurück.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// gibt 10 aus
```
Der Kurzcode für den obigen Code ist:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// gibt 10 aus
```
`c` wird auf `a` gesetzt, weil die Bedingung `a < b` wahr war

---

Der _Nil-Coalescing-Operator_ `a ?? b` entpackt ein optionales `a`, wenn es einen Wert enthält, oder gibt einen Standardwert `b` zurück, wenn `a` `nil` ist.
Der Ausdruck `a` ist immer von einem optionalen Typ.
Der Ausdruck `b` muss dem Typ entsprechen, der in a gespeichert ist.
Der Nil-Coalescing-Operator ist die Kurzform für den untenstehenden Code:
```javascript
a != nil ? a! : b;
```

---

`if` ist das Schlüsselwort, das eine bedingte Anweisung in JavaScript einleitet. Es gibt hier kein Schlüsselwort `elif` — eine zweite Bedingung wird mit `else if` eingeleitet, geschrieben als zwei getrennte Wörter.

---

Die booleschen Literale in JavaScript sind kleingeschrieben: `true` und `false`, nicht `True`/`False`, und auch nicht die Zeichenketten `"true"`/`"false"`.

---

Damit ein Codeblock nicht ausgeführt wird, muss die Bedingung in den Klammern zu `false` ausgewertet werden.

---

Das Leerzeichen zwischen `if` und seinen Klammern ist rein kosmetisch: `if(true)` und `if (true)` sind für JavaScript dieselbe Anweisung.

---

Die geschwungenen Klammern sind es, die mehrere Anweisungen zu einem Block zusammenfassen. Ohne sie steuert ein `if` nur die einzelne Anweisung, die darauf folgt, weshalb `if (true) console.log("Hello!");` gültiges JavaScript ist.

---

Die Bedingung wird einmal ausgewertet, bevor der Block beginnt. JavaScript schaut sie sich nicht noch einmal an, während die Anweisungen zwischen den geschwungenen Klammern ausgeführt werden.

---

Eine `false`-Bedingung überspringt den Block vollständig, und das Programm setzt bei der ersten Anweisung nach der schließenden Klammer fort.

---

Eine Bedingung muss kein boolescher Wert sein: JavaScript wandelt alles, was es vorfindet, in einen solchen um, weshalb `if (1)` seinen Block ausführt und `if (0)` nicht. Ein literales `true` braucht überhaupt keine Umwandlung.

---

Ein Codeblock ist nicht auf eine einzige Zeile beschränkt — jede Anweisung innerhalb der geschwungenen Klammern wird der Reihe nach ausgeführt, wenn die Bedingung `true` ist.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
und die Ausgabe ist `First line`, gefolgt von `Second line`.

---

Anweisungen innerhalb eines Blocks werden nacheinander ausgeführt, von oben nach unten, weshalb zwei `console.log`-Aufrufe im selben Block auf zwei getrennten Zeilen ausgeben.

---

Die Einrückung der Anweisungen innerhalb eines Blocks ist nur eine Konvention zur besseren Lesbarkeit. JavaScript verwendet die geschwungenen Klammern, niemals die Einrückung, um zu entscheiden, was zum Block gehört.

---

Anweisungen wie `if`, `else if` und `else`, die Code je nachdem ausführen oder überspringen, ob eine Bedingung `true` oder `false` ist, werden **bedingte Anweisungen** genannt.

---

Eine boolesche Variable, selbst eine aus einer `!`-Negation gebildete wie `isAfternoon`, kann direkt als `if`-Bedingung verwendet werden, ohne dass ein Vergleich nötig ist.

---

Die Bedingung einer `if`-Anweisung steht immer innerhalb von Klammern `()`, direkt nach dem Schlüsselwort `if` und vor der öffnenden geschwungenen Klammer.

---

Ein Block kann eine beliebige Anzahl von Anweisungen enthalten, aber auch keine: `if (true) {}` ist gültiges JavaScript, das einfach nichts tut.

---

Der Codeblock einer `if`-Anweisung ist die Menge der Anweisungen innerhalb der geschwungenen Klammern `{ }`, der Teil, der tatsächlich ausgeführt wird, wenn die Bedingung `true` ist.
