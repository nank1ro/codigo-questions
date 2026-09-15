Jeder Wert in JavaScript hat einen **Typ**. Es gibt sieben **primitive** Typen:
- `number` für jede Zahl, wie `42` oder `3.14`
- `string` für Text, wie `"Ana"`
- `boolean` für `true` und `false`
- `undefined` für einen Wert, der nie angegeben wurde
- `null` für einen absichtlich leeren Wert
- `bigint` für ganze Zahlen beliebiger Größe, wie `9007199254740993n`
- `symbol` für eindeutige Bezeichner, die mit `Symbol()` erstellt werden

Alles andere (Arrays, Funktionen, mit `{}` erstellte Objekte, Datumsangaben...) ist ein `object`.
Der Operator `typeof` sagt dir den Typ eines Werts, als String:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// gibt number string boolean aus
let city;
console.log(typeof city);
// gibt undefined aus
```

---

JavaScript ist **dynamisch typisiert**: eine Variable hat keinen eigenen Typ, nur der Wert, den sie gerade enthält, hat einen. Dieselbe Variable kann jetzt eine Zahl und später einen String enthalten, und `typeof` folgt dem Wert:
```javascript
let data = 10;
console.log(typeof data);
// gibt number aus
data = "ten";
console.log(typeof data);
// gibt string aus
```
Das ist praktisch, bedeutet aber auch, dass eine Funktion einen Wert eines unerwarteten Typs erhalten kann, daher ist eine Prüfung mit `typeof` ein häufiger erster Schritt. Da `typeof` einen String zurückgibt, vergleichst du sein Ergebnis mit einem String:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` hat einige Antworten, die Menschen überraschen.
Funktionen erhalten ihre eigene Antwort, `"function"`, obwohl sie Objekte sind:
```javascript
console.log(typeof function () {});
// gibt function aus
console.log(typeof console.log);
// gibt function aus
```
Arrays erhalten **keine** eigene Antwort: sie sind einfach `"object"`, genau wie `{}`:
```javascript
console.log(typeof [1, 2, 3]);
// gibt object aus
```
Und `typeof null` ist `"object"`, ein historischer Bug, der nie behoben wurde. `typeof` unterscheidet also Primitive und Funktionen gut, aber es kann ein Array, ein Objekt und `null` nicht auseinanderhalten.

---

Du kannst einen Wert **explizit** in einen anderen Typ umwandeln, indem du den Typ als Funktion aufrufst:
- `Number(value)` wandelt in eine Zahl um: `Number("42")` ist `42`
- `String(value)` wandelt in einen String um: `String(42)` ist `"42"`
- `Boolean(value)` wandelt in einen Boolean um: `Boolean("")` ist `false`

Das Ergebnis ist ein ganz neuer Wert; das Original wird nicht geändert:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// gibt 8 number aus
console.log(String(count) + "!");
// gibt 8! aus
```
Eine explizite Umwandlung macht deine Absicht sichtbar: Wer `Number(input)` liest, weiß, dass `input` Text war.

---

`Number()` ist streng: der gesamte String muss eine Zahl sein, sonst ist das Ergebnis `NaN` („Not a Number“):
```javascript
console.log(Number("12px"));
// gibt NaN aus
```
`parseInt()` und `parseFloat()` sind nachgiebiger: sie lesen Ziffern vom Anfang des Strings, überspringen führende Leerzeichen und stoppen beim ersten Zeichen, das nicht Teil einer Zahl ist. `parseInt` behält nur den ganzzahligen Teil:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// gibt 12 1.5 aus
console.log(parseInt("3.9em"), parseInt("-4px"));
// gibt 3 -4 aus
```
Beginnt der String nicht mit etwas, das den Anfang einer Zahl sein kann (ein optionales Vorzeichen, dann eine Ziffer), geben auch sie `NaN` zurück:
```javascript
console.log(parseInt("auto"));
// gibt NaN aus
```
`NaN` ist der einzige Wert, der nicht gleich sich selbst ist, daher ist `x === NaN` immer `false`; um ihn zu erkennen, verwende `Number.isNaN(x)`.

---

Es gibt zwei Möglichkeiten zu fragen „ist das `NaN`?“, und sie beantworten unterschiedliche Fragen.
Die alte globale Funktion `isNaN(value)` **wandelt** `value` zuerst in eine Zahl um und prüft dann. Sie sagt also `true` für alles, was keine Zahl werden kann, selbst wenn es gar nicht `NaN` ist:
```javascript
console.log(isNaN("hello"));
// gibt true aus, weil Number("hello") NaN ist
console.log(isNaN("42"));
// gibt false aus, weil Number("42") 42 ist
```
`Number.isNaN(value)` wandelt **nicht** um: es ist `true` nur, wenn `value` wirklich die Zahl `NaN` ist:
```javascript
console.log(Number.isNaN("hello"));
// gibt false aus, ein String ist kein NaN
console.log(Number.isNaN(Number("hello")));
// gibt true aus
```
Bevorzuge `Number.isNaN`, und wandle zuerst um, wenn du wissen willst, ob eine Umwandlung fehlgeschlagen ist.

---

JavaScript wandelt auch **implizit** um, und der Operator `+` ist die Stelle, an der das am häufigsten zuschlägt. Wenn eine der beiden Seiten ein String ist, **verkettet** `+` und die andere Seite wird in einen String umgewandelt:
```javascript
console.log("5" + 3);
// gibt 53 aus
console.log(1 + 2 + "3");
// gibt 33 aus, weil 1 + 2 zuerst berechnet wird
```
Jeder andere arithmetische Operator wandelt beide Seiten in **Zahlen** um:
```javascript
console.log("6" - 2, "3" * "4");
// gibt 4 12 aus
```
Das Addieren von Werten, die aus Text stammen (Benutzereingaben, Dateien, URLs), kann also stillschweigend einen String statt einer Summe erzeugen. Wandle mit `Number()` um, bevor du addierst, um sicher zu sein.

---

Ein kurzer Weg, einen String in eine Zahl umzuwandeln, ist das **unäre Plus**: ein `+` vor einem einzelnen Wert wandelt ihn genau so um wie `Number()`:
```javascript
console.log(+"5" + 5);
// gibt 10 aus
console.log(typeof +"5");
// gibt number aus
```
Es ist kompakt, aber leicht mit einer Addition zu verwechseln, daher ziehen es viele Teams vor, das explizite `Number("5")` zu verwenden.

---

Die **lose** Gleichheit `==` wandelt die beiden Seiten vor dem Vergleich in einen gemeinsamen Typ um, nach Regeln, die schwer zu merken sind:
```javascript
console.log("5" == 5);
// gibt true aus, "5" wird zu 5
console.log(0 == "");
// gibt true aus, "" wird zu 0
console.log(0 == false, "1" == true);
// gibt true true aus
```
Die **strikte** Gleichheit `===` wandelt nie um: Werte unterschiedlicher Typen sind einfach nicht gleich:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// gibt false false false aus
```
Verwende standardmäßig `===` (und `!==`). Die einzige häufige Ausnahme ist `value == null`, das `null` und `undefined` zusammen prüft.

---

Wenn JavaScript einen Boolean benötigt, zum Beispiel in einer `if`-Bedingung oder in `Boolean(value)`, wandelt es den Wert um. Nur acht Werte werden zu `false`; sie werden **falsy** genannt:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` und `NaN`.
**Alles andere ist truthy**, einschließlich einiger Werte, die leer aussehen:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// gibt false false false aus
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// gibt true true true true aus
```
`"0"` ist ein nicht-leerer String, also ist er truthy; ein leeres Array ist ein Objekt, also ist es auch truthy.

---

Eine häufige Abkürzung, um einen beliebigen Wert in einen Boolean umzuwandeln, ist die **doppelte Verneinung** `!!`: das erste `!` wandelt in einen Boolean um und kehrt ihn um, das zweite kehrt ihn zurück:
```javascript
console.log(!!"text", !!0);
// gibt true false aus
```
`!!value` und `Boolean(value)` liefern genau dasselbe Ergebnis; die explizite Form ist leichter zu lesen.

---

JavaScript hat einen einzigen `number`-Typ für ganze Zahlen und Dezimalzahlen: jede Zahl ist ein 64-Bit-Gleitkommawert (ein *double*). `5` und `5.0` sind also derselbe Wert, und es gibt keinen separaten Integer-Typ:
```javascript
console.log(5 === 5.0, 10 / 2);
// gibt true 5 aus
```
Um zu fragen, ob eine Zahl keinen Bruchteil hat, verwende `Number.isInteger`:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// gibt true false aus
```
Template-Literale wandeln den interpolierten Wert mit denselben Regeln wie `String()` in einen String um, daher wird `${5.0}` zu `"5"`, nicht zu `"5.0"`.

---

Da Zahlen Doubles sind, können manche Dezimalzahlen nicht exakt gespeichert werden und kleine Fehler erscheinen:
```javascript
console.log(0.1 + 0.2);
// gibt 0.30000000000000004 aus
console.log(0.1 + 0.2 === 0.3);
// gibt false aus
```
Die Methode `toFixed(digits)` rundet eine Zahl auf `digits` Dezimalstellen, gibt aber einen **String** zurück, was für die Anzeige in Ordnung und für weitere Berechnungen falsch ist:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// gibt 0.30 string aus
```
Um eine gerundete **Zahl** zu erhalten, wandle das Ergebnis mit `Number()` zurück:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// gibt 0.3 aus
```

---

Ein `number` kann ganze Zahlen nur bis `Number.MAX_SAFE_INTEGER`, also `9007199254740991`, exakt darstellen. Darüber gehen Ziffern verloren:
```javascript
console.log(9007199254740993);
// gibt 9007199254740992 aus
```
Für größere ganze Zahlen verwende `bigint`: schreibe das Literal mit einem `n`-Suffix oder wandle mit `BigInt()` um:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// gibt bigint 9007199254740994n aus
```
`console.log` zeigt das `n`-Suffix; `String(big)` gibt die reinen Ziffern.
Ein `bigint` und ein `number` können in der Arithmetik nicht gemischt werden: `big + 1` wirft einen `TypeError`. Wandle eine Seite explizit um, mit `BigInt(count)` oder `Number(big)`.

---

Da `typeof` für Arrays, Objekte und `null` `"object"` antwortet, braucht man zwei zusätzliche Prüfungen, um sie auseinanderzuhalten.
`Array.isArray(value)` ist `true` nur für Arrays:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// gibt true false aus
```
Für `null` vergleiche direkt, `value === null`. Kombiniert ergibt das ein vollständiges Bild jedes Werts:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Prüfe zuerst auf `null` und Arrays, weil das einfache `typeof` sie nicht unterscheiden kann.

---

Text aus Formularen, Dateien oder URLs ist immer ein String, selbst wenn er eine Zahl oder einen Boolean darstellt. Ihn zurück in den richtigen Typ umzuwandeln, kombiniert alles, was du gesehen hast: vergleiche mit `"true"` und `"false"` für Booleans, und versuche `Number()` für Zahlen, indem du daran denkst, dass `Number("")` `0` ist und dass `Number.isNaN` dir sagt, wann die Umwandlung fehlgeschlagen ist:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// gibt 3.5 0 NaN aus
```
Wenn nichts passt, behalte den String, wie er ist.
