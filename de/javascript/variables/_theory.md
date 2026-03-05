Variablen sind Container zur Speicherung von Datenwerten.
Jede Variable in JavaScript ist ein Objekt.
Um eine Variable zu erstellen, müssen wir ihr einen **Namen** geben und beachten, dass dieser keine Leerzeichen enthalten darf.
Eine Variable wird in dem Moment erstellt, in dem Sie ihr erstmals einen Wert zuweisen.
In JavaScript deklarieren Sie Konstanten mit den Schlüsselwörtern `let` oder `const` und Variablen mit dem Schlüsselwort `var`.
Der Wert einer Konstante kann nicht geändert werden, sobald er festgelegt ist, aber eine Variable kann später auf einen anderen Wert gesetzt werden.
Ein Beispiel für die Erstellung einer Variablen mit dem Namen `x` ist:
```javascript
var x = 1;
```
Auf diese Weise haben wir der Variablen mit dem Namen `x` den Wert `1` zugewiesen.
Wenn wir die Variable `x` ausgeben, erhalten wir die Zahl `1` zurück:
```javascript
console.log(x);
// gibt 1 aus
```

---

Variablen werden so genannt, weil sich der Wert, den sie speichern, ändern kann.
Wir können `x` mit `=` aktualisieren und ihm einen neuen Wert geben.
```javascript
var x = 1;
console.log(x); // gibt 1 aus
x = 2;
console.log(x); // gibt 2 aus
```

---

Wir können Variablen auch die Werte anderer Variablen zuweisen.
Hier können wir der Variablen `y` den Wert von `x` zuweisen
```javascript
var x = 5;
var y = x;
console.log(y); // gibt 5 aus
```

---

Wenn wir eine Variable aktualisieren, vergisst sie ihren vorherigen Wert.
Hier können wir die Variable `x` zweimal anzeigen und sehen, wie sich ihr Wert aktualisiert.
```javascript
var x = 5;
console.log(x); // gibt 5 aus
x = 10;
console.log(x); // gibt 10 aus
```

---

In JavaScript können String-Variablen mit doppelten und einfachen Anführungszeichen deklariert werden:
```javascript
let x = "May";
// beide sind derselbe String
let y = 'May';
console.log(x === y);
// gibt true aus
```

---

Wenn wir einen Variablennamen mit mehreren Wörtern haben, verwenden wir **camelCase**.
Es ist die Praxis, Phrasen so zu schreiben, dass jedes Wort in der Mitte der Phrase mit einem Großbuchstaben beginnt
