Entscheidungsfindung ist erforderlich, wenn wir Code nur unter bestimmten Bedingungen ausführen möchten.
Angenommen, wir möchten nur dann nach draußen gehen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `niceWeather` speichern und die Aktion `if` diese Variable `true` ist, wie folgt ausführen:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

Lassen Sie uns das vorherige Beispiel fortsetzen.
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
// prints 10
```
Der Kurzcode für den obigen Code ist:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
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
