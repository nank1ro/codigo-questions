JavaScript hat zwei verschiedene Möglichkeiten, um „hier ist kein Wert" auszudrücken.
`undefined` bedeutet, dass ein Wert **nie angegeben** wurde. Eine Variable, die ohne Wert deklariert wird, enthält `undefined`, und ebenso eine Eigenschaft, die in einem Objekt nicht existiert:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` ist ein Wert, den **du** absichtlich zuweist, um zu sagen: „leer, und ich weiß es":
```javascript
let owner = null;
console.log(owner);
// prints null
```
`undefined` ist also meistens die Sprache, die dir sagt, dass etwas fehlt, während `null` der Programmierer ist, der erklärt, dass etwas absichtlich leer ist.

---

Funktionen erzeugen `undefined` in zwei weiteren Situationen.
Wenn du eine Funktion mit **weniger Argumenten** aufrufst, als sie deklariert, enthalten die fehlenden Parameter `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Wenn eine Funktion **ohne ein `return`** endet (oder mit einem bloßen `return;`), liefert ihr Aufruf `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Beachte, dass das explizite Übergeben von `null` nicht dasselbe ist wie das Weglassen des Arguments: `greet(null)` gibt `null` aus, weil `null` ein echter Wert ist, der an die Funktion übergeben wurde.

---

Der Operator `typeof` gibt den Typ eines Werts als String zurück. Für `undefined` antwortet er mit `"undefined"`, wie du es erwartest:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Für `null` antwortet er jedoch mit `"object"`. Das ist ein Bug aus der allerersten Version von JavaScript, der nie behoben wurde, weil zu viel Code davon abhängt:
```javascript
console.log(typeof null);
// prints object
```
`typeof` ist also eine zuverlässige Möglichkeit, `undefined` zu erkennen, aber nicht `null`. Um auf `null` zu prüfen, vergleiche direkt damit: `value === null`.

---

Wie verhalten sich `null` und `undefined` beim Vergleich miteinander? Das hängt vom Operator ab.
Die **lose** Gleichheit `==` behandelt sie als dasselbe und betrachtet sie als verschieden von jedem anderen Wert, einschließlich `0`, `""` und `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
Die **strikte** Gleichheit `===` vergleicht auch den Typ, und `null` und `undefined` haben unterschiedliche Typen:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

Meistens ist es dir egal, *welche* der beiden „kein Wert"-Markierungen du erhalten hast: Du willst nur wissen, ob ein Wert vorhanden ist.
Weil `null == undefined` `true` ist und nichts anderes lose gleich `null` ist, ist der Vergleich `value == null` das Standardidiom, um **beide** auf einmal abzufangen:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
Das ist der eine Fall, in dem `==` gegenüber `===` bevorzugt wird: `value === null || value === undefined` zu schreiben erledigt genau dieselbe Aufgabe, nur länger.
Werte wie `0`, `""` und `false` sind *nicht* `null`: Sie sind echte Werte, die zufällig falsy sind.

---

Das Lesen einer Eigenschaft von `null` oder `undefined` ist ein Fehler, der das Programm stoppt:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` ist `undefined`, und `undefined` hat keine Eigenschaften. Der Operator der **optionalen Verkettung** (optional chaining) `?.` löst das: Wenn der Wert auf seiner linken Seite `null` oder `undefined` ist, bricht der gesamte Ausdruck ab und ergibt `undefined`, statt einen Fehler zu werfen:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Wenn die linke Seite doch einen Wert hat, verhält sich `?.` genau wie ein normaler `.`. Du kannst mehrere verketten: `user.address?.street?.name` gibt `undefined` zurück, sobald ein Glied fehlt.

---

Optionale Verkettung ist nicht auf Punkt-Eigenschaften beschränkt. Es gibt zwei weitere Formen.
`?.[]` liest ein Element oder einen berechneten Schlüssel nur, wenn die linke Seite einen Wert hat:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` ruft eine Funktion nur auf, wenn sie existiert, was bei optionalen Callbacks praktisch ist:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
In jeder Form gilt die Prüfung für den Wert **direkt vor** dem `?.`: `post?.tags?.[0]` ist sicher, selbst wenn `post` selbst `null` oder `undefined` ist.

---

Sobald du weißt, dass ein Wert fehlen kann, möchtest du meistens einen **Standardwert** an seiner Stelle. Zwei Operatoren tun das, und sie unterscheiden sich darin, was sie als „fehlend" betrachten.
`a || b` gibt `b` zurück, wann immer `a` **falsy** ist: nicht nur `null` und `undefined`, sondern auch `0`, `""`, `false` und `NaN`.
Der Operator des **nullish coalescing** `a ?? b` gibt `b` nur zurück, wenn `a` `null` oder `undefined` ist, und behält jeden anderen Wert:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Verwende `??`, wenn `0`, `""` oder `false` legitime Werte sind, die erhalten bleiben müssen, und `||`, wenn du wirklich jeden falsy-Wert ersetzen willst.

---

Ein sehr häufiges Muster ist „setze diese Eigenschaft nur, wenn sie noch nicht gesetzt ist". Mit `??` geschrieben wiederholt es den Namen:
```javascript
options.timeout = options.timeout ?? 1000;
```
Der Operator der **nullish assignment** `??=` tut dasselbe in einem Schritt: Er weist die rechte Seite nur zu, wenn die linke Seite gerade `null` oder `undefined` ist, und lässt jeden anderen Wert unberührt:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` bleibt `0`, weil `0` nicht nullish ist; `timeout` existierte nicht, also erhält es `1000`. Dieselbe Idee gibt es für `||` als `||=`, das jeden falsy-Wert überschreibt.

---

Ein **Standardparameter** gibt einem Parameter einen Wert, wenn der Aufrufer keinen liefert. Die Regel ist präzise: Der Standardwert wird nur verwendet, wenn das Argument `undefined` ist, was auch das Weglassen einschließt. `null` zu übergeben löst den Standardwert **nicht** aus, weil `null` ein Wert ist:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Standardparameter folgen der `undefined`-Regel, während `??` sowohl `null` als auch `undefined` abdeckt: Wähle das, das dazu passt, wie deine Funktion aufgerufen wird.

---

Optionale Verkettung und die `== null`-Prüfung arbeiten gut zusammen: Die Kette liest den verschachtelten Wert, ohne einen Fehler zu werfen, und die Prüfung entscheidet, was zu tun ist, wenn das Ergebnis fehlt:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Im letzten `return` ist ein einfacher `.` sicher, weil die Prüfung bereits bewiesen hat, dass jedes Glied existiert.

---

Viele eingebaute Methoden melden „nichts gefunden", indem sie `undefined` zurückgeben. Die Array-Methode `find(callback)` ist das typische Beispiel: Sie gibt das erste Element zurück, für das der Callback `true` ist, oder `undefined`, wenn kein Element passt:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Hier `found.price` zu lesen würde einen Fehler werfen, also sind `?.` und `??` die natürlichen Begleiter von `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` und `undefined` verhalten sich unterschiedlich, wenn ein Objekt mit `JSON.stringify()` in JSON umgewandelt wird.
JSON hat einen `null`-Wert, aber kein `undefined`, daher wird eine Eigenschaft, deren Wert `undefined` ist, einfach **weggelassen**, während eine `null`-Eigenschaft erhalten bleibt:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Innerhalb von Arrays können die Positionen nicht verschwinden, daher wird `undefined` dort zu `null`:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Die Prüfung `obj.key === undefined` kann zwei Situationen nicht unterscheiden: Die Eigenschaft existiert nicht, oder sie existiert und enthält den Wert `undefined`.
`Object.hasOwn(obj, key)` beantwortet nur die erste Frage: Es gibt `true` zurück, wenn das Objekt seine **eigene** Eigenschaft namens `key` hat, ganz gleich welchen Werts:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
„Eigene" bedeutet, direkt am Objekt selbst deklariert: Geerbte Member wie `toString` sind an jedem Objekt verfügbar, aber `Object.hasOwn(config, "toString")` ist `false`.
