Eine Funktion braucht keinen Namen. Ein **Funktionsausdruck** erzeugt eine Funktion als Wert, den du in einer Variable speichern und über sie aufrufen kannst:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Eine **Pfeilfunktion** ist eine kürzere Art, dasselbe zu schreiben: Streiche das Schlüsselwort `function` und setze einen „Fat Arrow" `=>` zwischen die Parameterliste und den Körper:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Pfeilfunktionen werden meist in einer `const` gespeichert, damit der Name nicht versehentlich neu zugewiesen werden kann, und werden genau wie jede andere Funktion aufgerufen.

---

Pfeilfunktionen werden in zwei häufigen Fällen noch kürzer.
Wenn der Körper ein **einzelner Ausdruck** ist, kannst du die geschweiften Klammern und das Schlüsselwort `return` weglassen: Der Wert des Ausdrucks wird automatisch zurückgegeben (ein **implizites return**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
Wenn es **genau einen Parameter** gibt, kannst du auch die Klammern darum weglassen:
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
Bei null Parametern oder bei zwei oder mehr sind die Klammern erforderlich: `() => 42` und `(a, b) => a + b`.

---

Beim impliziten return gibt es eine Falle. Eine Pfeilfunktion, deren Körper mit `{` beginnt, wird als **Blockkörper** gelesen, nie als Objektliteral:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
Hier ist `{ name: name }` ein Block, der das Label `name:` gefolgt vom Ausdruck `name` enthält. Nichts wird zurückgegeben, daher liefert der Aufruf `undefined`.
Um ein Objektliteral in einer Zeile zurückzugeben, setze es in **Klammern**, damit JavaScript es als Ausdruck behandelt:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

Das Objektliteral in Klammern zu setzen ist der Standardweg, um Objekte mit einer einzeiligen Pfeilfunktion zu erzeugen, zum Beispiel wenn du ein paar Werte in einen Datensatz umwandelst:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
Eine Pfeilfunktion ohne Parameter beginnt mit einem leeren Paar Klammern `()`:
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

Pfeilfunktionen entfalten ihre volle Stärke als **Callbacks**: Funktionen, die als Argumente an andere Funktionen übergeben werden. Array-Methoden sind das häufigste Beispiel.
`map(callback)` gibt ein neues Array mit dem Ergebnis des Callbacks für jedes Element zurück, und `filter(callback)` gibt ein neues Array mit nur den Elementen zurück, für die der Callback `true` zurückgibt:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
Beide geben ein neues Array zurück und lassen das Original unangetastet, sodass du sie verketten kannst: `numbers.filter(...).map(...)`.

---

Zwei weitere Array-Methoden nehmen einen Callback entgegen.
`forEach(callback)` ruft den Callback einmal pro Element auf und gibt nichts zurück; benutze ihn für Seiteneffekte wie das Ausgeben.
`reduce(callback, initialValue)` faltet das Array zu einem einzelnen Wert zusammen: Der Callback erhält den bisher akkumulierten Wert und das aktuelle Element und gibt den neuen akkumulierten Wert zurück:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` sortiert ein Array an Ort und Stelle mit einem Callback, der zwei Elemente erhält und eine negative Zahl zurückgibt, wenn das erste zuerst kommen soll, eine positive Zahl, wenn das zweite zuerst kommen soll, oder `0`, wenn sie gleich sind. Bei Zahlen sortiert `(a, b) => a - b` aufsteigend und `(a, b) => b - a` absteigend.
`find(callback)` gibt das erste Element zurück, für das der Callback `true` zurückgibt, oder `undefined`, wenn es keines gibt:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

Parameter von Pfeilfunktionen unterstützen dieselben Funktionen wie reguläre Funktionsparameter.
Ein **Standardwert** wird verwendet, wenn das Argument weggelassen wird oder `undefined` ist:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
Beachte, dass ein Parameter mit einem Standardwert immer die Klammern braucht, selbst wenn er der einzige ist: `name = "World" => ...` ist ein Syntaxfehler.

---

Ein **Rest-Parameter** `...name` sammelt beliebig viele Argumente in einem Array, und er funktioniert auch in Pfeilfunktionen:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
Reguläre Funktionen haben außerdem ein verstecktes Array-ähnliches `arguments`-Objekt, das jedes empfangene Argument enthält. Pfeilfunktionen **nicht**: Innerhalb einer Pfeilfunktion verweist `arguments` auf das `arguments` der umgebenden Funktion oder existiert gar nicht. Wann immer du „alle Argumente" in einer Pfeilfunktion brauchst, verwende einen Rest-Parameter.

---

Eine Funktion merkt sich die Variablen des Geltungsbereichs, in dem sie **erzeugt** wurde, selbst nachdem dieser Geltungsbereich fertig ausgeführt ist. Das nennt man eine **Closure**.
Das klassische Beispiel ist ein Zähler-Erzeuger: Jeder Aufruf von `makeCounter` erzeugt ein neues `count` und gibt eine Pfeilfunktion zurück, die genau dieses `count` weiterverwendet:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
Niemand sonst kann `count` lesen oder zurücksetzen: Es existiert nur innerhalb der zurückgegebenen Funktion. Ein zweiter Aufruf von `makeCounter()` erzeugt einen unabhängigen Zähler mit seinem eigenen `count`.

---

Da eine Funktion ein Wert ist, kann eine Pfeilfunktion **eine andere Pfeilfunktion zurückgeben**. Zwei Pfeilfunktionen zu verketten ist eine kompakte Art, eine Funktion zu schreiben, die Funktionen erzeugt:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
Lies sie von links nach rechts: `makeAdder` nimmt `amount` entgegen und gibt `(n) => n + amount` zurück, eine Pfeilfunktion, die `amount` über eine Closure einfängt. `makeAdder(1)(5)` ruft die zurückgegebene Funktion sofort auf.
