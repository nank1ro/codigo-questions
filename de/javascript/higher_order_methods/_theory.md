In JavaScript ist eine Funktion ein **Wert**: Du kannst sie in einer Variablen speichern, in ein Array legen und einer anderen Funktion als Argument übergeben. Eine Funktion, die eine Funktion als Argument erhält oder eine zurückgibt, heißt **Funktion höherer Ordnung**. Die übergebene Funktion heißt **Callback**, weil der Empfänger sie *zurückruft*, wenn er sie braucht:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Beachte, dass `shout` **ohne Klammern** übergeben wird: `twice(shout, "hi")` übergibt die Funktion selbst, während `twice(shout("hi"), "hi")` zuerst `shout` aufrufen und dessen Ergebnis übergeben würde, den String `"HI!"`, der nicht aufgerufen werden kann.

---

Funktionen höherer Ordnung trennen *was mit jedem Element geschehen soll* von *wie die Elemente durchlaufen werden*. Der durchlaufende Teil wird einmal geschrieben, und der Callback entscheidet den Rest:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
Der Callback erhält ein Element nach dem anderen. Er kann eine inline geschriebene Arrow Function sein, wie oben, oder jede in einer Variablen gespeicherte Funktion. Genau so arbeiten intern die eingebauten Array-Methoden, die du als Nächstes kennenlernst.

---

Die eingebaute Methode `map` macht das, was `transform` macht: Sie ruft den Callback für jedes Element auf und sammelt die Ergebnisse in einem **neuen Array**. `forEach` ruft den Callback ebenfalls für jedes Element auf, sammelt aber nichts und gibt immer `undefined` zurück; benutze sie nur für Seiteneffekte, etwa zum Ausgeben:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
Ein häufiger Fehler ist, das Ergebnis von `forEach` zu speichern oder eine weitere Methode daran zu ketten: Es gibt nichts zu verketten, denn sie gibt `undefined` zurück. Faustregel: Nimm `map`, wenn du die neuen Werte brauchst, und `forEach`, wenn du nur etwas *tun* willst.

---

Zwei weitere Methoden höherer Ordnung decken die meisten alltäglichen Bedürfnisse ab.
`filter(callback)` gibt ein neues Array nur mit den Elementen zurück, für die der Callback `true` liefert; ein Callback, der so mit Ja oder Nein antwortet, heißt **Prädikat**.
`reduce(callback, initialValue)` fasst alle Elemente zu einem einzigen Wert zusammen: Der Callback erhält den **Akkumulator** (das bisherige Ergebnis) und das aktuelle Element und gibt den neuen Akkumulator zurück. Das zweite Argument von `reduce` ist der Startwert des Akkumulators:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Da `filter` und `map` Arrays zurückgeben, kannst du sie verketten und mit `reduce` abschließen: `numbers.filter(...).map(...).reduce(...)`.

---

Drei Methoden beantworten Fragen über ein Array mit einem Prädikat:
- `find(predicate)` gibt das **erste** Element zurück, für das das Prädikat `true` ist, oder `undefined`, wenn es keines gibt
- `some(predicate)` gibt `true` zurück, wenn **mindestens ein** Element das Prädikat erfüllt
- `every(predicate)` gibt `true` zurück, wenn **alle** Elemente es erfüllen (und `true` für ein leeres Array)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
Alle drei hören auf, sobald die Antwort feststeht, sie sehen sich also nie mehr Elemente an als nötig.

---

`sort(compare)` sortiert ein Array **an Ort und Stelle** mit einem Callback, der zwei Elemente erhält und eine negative Zahl zurückgibt, wenn das erste zuerst kommen soll, eine positive Zahl, wenn das zweite zuerst kommen soll, oder `0`, wenn sie gleich sind. Für Zahlen sortiert `(a, b) => a - b` aufsteigend und `(a, b) => b - a` absteigend.
Ohne Vergleichsfunktion wandelt `sort()` jedes Element in einen **String** um und vergleicht sie Zeichen für Zeichen, deshalb kommt `10` vor `9`, weil `"1"` kleiner ist als `"9"`:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Da `sort` das Array verändert, sortiere eine Kopie, wenn du auch die ursprüngliche Reihenfolge brauchst: `[...numbers].sort(...)`. Für Strings nimm `(a, b) => a.localeCompare(b)` als Vergleichsfunktion, die Text alphabetisch ordnet.

---

Die Vergleichsfunktion kann jeden Teil der Elemente betrachten, deshalb wird ein Array von Objekten nach einer ihrer Eigenschaften sortiert, indem einfach diese Eigenschaft verglichen wird:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Das Sortieren der Kopie lässt `items` in seiner ursprünglichen Reihenfolge.

---

Eine Funktion höherer Ordnung kann auch eine Funktion **zurückgeben**. Die zurückgegebene Funktion merkt sich die Variablen der Stelle, an der sie erzeugt wurde, auch nachdem die äußere Funktion beendet ist: Das nennt man **Closure**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Jeder Aufruf von `makeMultiplier` erzeugt eine neue Funktion mit ihrem eigenen `factor`. So baust du aus einer Vorlage eine Familie ähnlicher Funktionen. Dasselbe lässt sich mit Arrow Functions schreiben: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

Eine Closure behält eine **lebendige** Verbindung zur Variablen, keine Kopie ihres Werts. Werden mehrere Funktionen im selben Aufruf erzeugt, teilen sie sich dieselbe Variable, und jede Änderung über die eine ist für die anderen sichtbar:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Niemand kann `count` von außen lesen oder zurücksetzen, außer über diese beiden Funktionen: Die Variable ist **privat**. Ein zweiter Aufruf von `makeCounter()` erzeugt ein völlig eigenes `count`.

---

Da Funktionen Werte sind, kannst du eine Funktion höherer Ordnung schreiben, die zwei Funktionen zu einer neuen **kombiniert**. `compose(f, g)` gibt eine Funktion zurück, die zuerst `g` und dann `f` auf das Ergebnis anwendet, passend zur mathematischen Schreibweise *f(g(x))*:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
Die Reihenfolge zählt: `compose(f, g)` führt zuerst `g` aus, dann `f`. Programme so aus kleinen, zusammengeklebten Funktionen zu bauen, nennt man **Funktionskomposition**.

---

Eine Funktion, die eine Funktion zurückgibt, ist auch der natürliche Weg, einen Callback **anzupassen**. Angenommen, du hast ein Prädikat und brauchst für `filter` das Gegenteil: Statt es neu zu schreiben, umhülle es:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
Ein allgemeines `not(predicate)` würde das für jedes Prädikat tun: Es gibt eine neue Funktion zurück, die `predicate` mit demselben Argument aufruft und das Ergebnis mit `!` umkehrt. Prädikate für `filter`, `find`, `some` und `every` erhalten das Element als erstes Argument, der Wrapper muss also nur diesen einen Wert weiterreichen.

---

Der Akkumulator von `reduce` muss keine Zahl sein: Er kann ein String, ein Array oder ein Objekt sein. Ausgehend von einem leeren Objekt `{}` kannst du in einem Durchgang zählen oder gruppieren. Denk daran, den **Akkumulator zurückzugeben**, sonst erhält der nächste Schritt `undefined`:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` liest den aktuellen Zähler oder `0`, wenn dieser Schlüssel noch nicht existiert.

---

Jede Funktion hat eine Methode `bind`, die eine **neue** Funktion mit vorab festgelegten Dingen zurückgibt. Ihr erstes Argument wird zum `this` der neuen Funktion; die übrigen Argumente werden vor die gestellt, mit denen die neue Funktion aufgerufen wird (eine **partielle Anwendung**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
`this` festzulegen ist bei Methoden wichtig. Wird eine Methode aus ihrem Objekt herauskopiert und allein aufgerufen, verweist `this` nicht mehr auf das Objekt, sodass `this.name` zu `undefined` wird. `bind` bindet es an das Objekt:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
Die ursprüngliche Funktion wird nie verändert: `bind` baut immer eine neue, deren `name` der ursprüngliche Name mit vorangestelltem `bound ` ist.

---

Echte Programme kombinieren diese Methoden zu einer **Pipeline**: Filtere die Elemente, die dich interessieren, bilde sie auf die benötigten Werte ab und reduziere sie zu einem Ergebnis. Die Zwischenarrays in Konstanten zu speichern hält jeden Schritt lesbar und erlaubt es, sie wiederzuverwenden:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` macht aus einem Array von Strings einen einzigen String, dessen Elemente durch Komma und Leerzeichen getrennt sind.

---

Closures erlauben es einer zurückgegebenen Funktion, zwischen den Aufrufen **privaten Zustand** zu behalten. Ein klassischer so gebauter Helfer ist `once(fn)`: Er gibt eine Funktion zurück, die `fn` nur beim ersten Aufruf ausführt, sich das Ergebnis merkt und bei jedem weiteren Aufruf dasselbe Ergebnis zurückgibt, ohne `fn` erneut auszuführen:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
Der Wrapper braucht zwei private Variablen: ob `fn` schon gelaufen ist, und das gespeicherte Ergebnis. Beide leben in der Closure, für die Außenwelt unsichtbar. Um alle Argumente des Wrappers an `fn` weiterzureichen, deklariere den Wrapper mit einem Rest-Parameter `(...args)` und rufe `fn(...args)` auf.

---

Alles kommt in `groupBy(items, keyFn)` zusammen: eine Funktion höherer Ordnung, die einen Callback erhält, der den **Gruppenschlüssel** jedes Elements bestimmt, und ein Objekt zurückgibt, das jedem Schlüssel das Array der Elemente mit diesem Schlüssel zuordnet. `reduce` mit einem Objekt-Akkumulator erledigt die ganze Arbeit:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
Berechne für jedes Element den Schlüssel, erzeuge das Array für diesen Schlüssel, falls es noch nicht existiert (`acc[key] ?? []`), füge das Element hinzu und gib den Akkumulator zurück. Da der Aufrufer `keyFn` wählt, gruppiert dieselbe Funktion Wörter nach Anfangsbuchstabe, Personen nach Stadt oder Zahlen nach Parität.
