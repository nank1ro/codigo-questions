Werte mit einem Index nach dem anderen aus einem Array zu lesen ist umständlich:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**Destrukturierung** erledigt dieselbe Aufgabe in einer Zeile. Links von `=` schreibst du ein Muster, das wie das Array selbst aussieht, und jeder Name darin erhält das Element an derselben Position:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// gibt 3 7 aus
```
Das Muster muss nicht das ganze Array abdecken: Überzählige Elemente werden einfach ignoriert, und ein Name ohne passendes Element wird zu `undefined`.

---

Destrukturierung ist am nützlichsten genau dort, wo ein Array ankommt: als Funktionsargument oder als Ergebnis eines Aufrufs. Statt das Array aufzuheben und überall in ihm zu indizieren, packst du es einmal aus und gibst den Teilen richtige Namen:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// gibt 5 aus
```
Im ursprünglichen Array wird nichts kopiert oder geändert, das Muster liest nur daraus.

---

Manchmal ist nur ein einziges Element tief im Array wichtig. Du kannst eine Position im Muster leer lassen und das Komma behalten, das sie trennt: Eine solche leere Position heißt **Loch**, und sie überspringt das Element, ohne es zu benennen:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// gibt 64 aus
```
Zähle die Kommas, nicht die Namen: Jedes Komma rückt das Muster eine Position weiter, ganz gleich, ob vor ihm ein Name steht oder nicht.

---

Ein Array ist nicht immer so lang, wie das Muster es erwartet. Hinter einen Namen `= value` zu schreiben, gibt ihm einen **Standardwert**, der immer dann benutzt wird, wenn das Array an dieser Position nichts hat:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// gibt 1920 1080 aus
```
Der Standardwert wird nur ausgewertet, wenn er gebraucht wird, er darf also sogar ein Funktionsaufruf sein, und ein Standardwert kann an jeder Position stehen, nicht nur an der letzten.

---

Ein Muster kann auch links von einer einfachen Zuweisung stehen, ohne `const` oder `let` davor, und schreibt dann in Variablen, die bereits existieren. Damit wird das Vertauschen zweier Werte zu einer einzigen Zeile, ganz ohne temporäre Variable:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// gibt 2 1 aus
```
Die rechte Seite wird zuerst aufgebaut, daher sind beide alten Werte beim Zuweisen bereits sicher im temporären Array gespeichert. Achte auf das Semikolon in der Zeile davor: Eine Zeile, die mit `[` beginnt, würde sonst als Index des davor Stehenden gelesen.

---

Auch Objekte lassen sich destrukturieren, mit geschweiften statt eckigen Klammern. Hier bedeutet die Position nichts: Jeder Name wird mit dem **Schlüssel** abgeglichen, der genauso heißt:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// gibt Ada 36 aus
```
`age` und `name` im Muster zu tauschen ändert nichts, und Schlüssel, die das Muster nicht erwähnt, werden einfach übergangen. Ein Name ohne passenden Schlüssel wird zu `undefined`.

---

Objektmuster und Standardwerte lassen sich genauso kombinieren wie Arraymuster, was sie zu einem ordentlichen Weg macht, ein Konfigurationsobjekt zu lesen, dessen Schlüssel vorhanden sein können oder auch nicht:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// gibt dark en aus
```
Da das ganze Muster eine einzige Anweisung ist, kann eine Funktion in ihrer allerersten Zeile alles, was sie braucht, aus ihrem Argument auspacken.

---

Ein Objektmuster benennt seine Variablen nach den Schlüsseln, was unpraktisch ist, wenn die Schlüssel kryptisch oder bereits vergeben sind. `key: newName` zu schreiben, **benennt die Variable um**:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// gibt Ada 1815 aus
```
Lies es als „nimm `n`, nenne es `name`". Der Doppelpunkt deklariert keinen Typ, und `n` selbst wird nie als Variable angelegt, nur `name`. Ein umbenannter Name kann trotzdem einen Standardwert bekommen, der dahinter geschrieben wird: `{ n: name = "unknown" }`.

---

Standardwerte haben eine Regel, die jeden überrascht: Sie greifen **nur** bei `undefined`. Ein Schlüssel, der existiert und `null`, `0`, `""` oder `false` enthält, ist ein echter Wert, also nimmt das Muster ihn und der Standardwert wird nie benutzt:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// gibt 0 aus
```
`null` verhält sich hier genauso wie `0`, obwohl es in einer API-Antwort oft „kein Wert" bedeutet. Wenn auch `null` ersetzt werden muss, destrukturiere zuerst und greife danach mit `??` darauf zurück.

---

Wenn ein Schlüssel ein weiteres Objekt oder ein Array enthält, kann das Muster einfach weiterlaufen und auch diese Form beschreiben:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// gibt London aus
```
Achte darauf, was diese Zeile erzeugt: `address: { city }` bedeutet „geh in `address` hinein", nicht „gib mir `address`", daher wird nur `city` zu einer Variable. Um beides zu bekommen, nenne den Schlüssel zweimal: `const { address, address: { city } } = user;`. Array- und Objektmuster lassen sich frei ineinander verschachteln, wie in `{ tags: [first] }`.

---

Den Kopf eines Arrays zu nehmen und den Rest zu behalten ist ein so verbreitetes Bedürfnis, dass Muster dafür eine eigene Syntax haben. Drei Punkte vor dem letzten Namen machen ihn zu einem **Rest-Element**, und es sammelt jedes verbleibende Element in einem ganz neuen Array:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// gibt a [ 'b', 'c' ] aus
```
Ein Rest-Element muss im Muster an letzter Stelle stehen und darf keinen Standardwert haben: Wenn nichts übrig bleibt, ist es einfach ein leeres Array.

---

Auch Objektmuster haben ein Rest-Element, und dort sammelt es jeden Schlüssel, den das Muster nicht erwähnt hat, in einem neuen Objekt:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// gibt { name: 'Ada', city: 'London' } aus
```
Das ist der kürzeste Weg, eine Kopie eines Objekts ohne einen seiner Schlüssel zu bauen: Das Original wird nie angetastet, und das Rest-Objekt ist ein frisches, das die übrigen Werte enthält.

---

Ein Muster kann in einer Funktionsdeklaration den Parameternamen ersetzen, sodass das Auspacken genau beim Aufruf passiert:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// gibt 12 aus
```
Im Körper gibt es überhaupt keine Objekt-Variable, nur `width` und `height`. Der Aufrufer übergibt ein Objekt, aber die Signatur dokumentiert genau, welche Schlüssel die Funktion liest, und die Schlüssel können in beliebiger Reihenfolge ankommen.

---

Ein destrukturierter Parameter mit Standardwerten ergibt ein sauberes Optionsobjekt, aber es bricht trotzdem, wenn der Aufrufer nichts übergibt: Das Lesen eines Schlüssels aus `undefined` wirft einen `TypeError`. Dem ganzen Muster einen Standardwert von `{}` zu geben, behebt das:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// gibt guest/false aus
```
Lies die Zeile von außen nach innen: `= {}` liefert ein leeres Objekt, wenn das Argument fehlt, und jeder innere Standardwert füllt dann seinen eigenen Schlüssel auf.

---

`Object.entries(obj)` macht aus einem Objekt ein Array von `[key, value]`-Paaren. Stelle ein Arraymuster an den Kopf einer `for...of`-Schleife, und jedes Paar wird ausgepackt, während die Schleife läuft:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// gibt ada is 36 aus
// gibt bob is 41 aus
```
Das ist die lesbare Art, ein Objekt zu durchlaufen: kein Index, keine Suche, nur die beiden Namen, die dich interessieren. `Object.keys` und `Object.values` liefern jeweils nur eine Seite, `Object.entries` liefert beide.

---

Alles bisher Gesehene gehört zu einer einzigen Syntax, daher lassen sich die Teile frei kombinieren: Ein Objektmuster kann ein weiteres Objektmuster verschachteln, das einen umbenannten Schlüssel mit Standardwert enthalten kann, neben einem Arraymuster, das mit einem Rest-Element endet. Eine Zeile beschreibt dann die ganze Form, die eine Funktion erwartet:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// gibt Post [js] +2 aus
```
Halte es lesbar: Ein Muster, das nicht mehr auf ein paar Zeilen passt, ist meist ein Zeichen dafür, dass die Funktion zu viel verlangt.
