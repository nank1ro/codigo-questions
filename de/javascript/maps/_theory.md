Eine **Map** speichert **Schlüssel-Wert-Paare**: Jeder Wert wird unter einem Schlüssel gespeichert, und du verwendest diesen Schlüssel, um den Wert wiederzufinden.
Du erstellst eine leere Map mit `new Map()`, fügst ein Paar mit `set(key, value)` hinzu und liest einen Wert mit `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Ruft man `set()` mit einem bereits vorhandenen Schlüssel auf, wird dessen Wert ersetzt.

---

Eine Map hat noch ein paar weitere wichtige Methoden und Eigenschaften:
- `has(key)` gibt `true` zurück, wenn der Schlüssel existiert
- `delete(key)` entfernt das Paar mit diesem Schlüssel
- `size` ist die Anzahl der gespeicherten Paare

```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
console.log(stock.has("apple"));
// prints true
stock.delete("pear");
console.log(stock.size);
// prints 1
```
Beachte, dass `size` eine Eigenschaft und keine Methode ist, sie hat also keine Klammern.

---

Eine Map nach einem Schlüssel zu fragen, den sie nicht enthält, ist kein Fehler: `get()` gibt einfach `undefined` zurück.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
Deshalb gibt es `has()`: Damit kannst du einen fehlenden Schlüssel von einem Schlüssel unterscheiden, dessen Wert zufällig `undefined` ist.
`set()` gibt die Map selbst zurück, sodass Aufrufe verkettet werden können:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

In einem einfachen Objekt wird jeder Schlüssel in einen String umgewandelt: `user[1]` und `user["1"]` sind derselbe Schlüssel.
Eine Map behält den **Typ** ihrer Schlüssel bei, sodass eine Zahl, ein String, ein Boolean oder sogar ein Objekt jeweils ein eigener Schlüssel sein können:
```javascript
let lookup = new Map();
lookup.set(1, "number one");
lookup.set("1", "string one");
console.log(lookup.size);
// prints 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// prints an object key
```
Objektschlüssel werden anhand ihrer Identität verglichen: Nur genau dasselbe Objekt liefert den zugehörigen Wert zurück.

---

Eine Map merkt sich die Reihenfolge, in der Paare hinzugefügt wurden, und du kannst mit `for...of` über sie iterieren.
Die Methode `entries()` liefert jedes Paar als `[key, value]`-Array, das du direkt in der Schleife entpacken kannst:
```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
for (const [name, qty] of stock.entries()) {
  console.log(`${name}: ${qty}`);
}
// prints apple: 3
// prints pear: 5
```
Direkt über die Map zu iterieren, `for (const [name, qty] of stock)`, macht genau dasselbe.

---

Wenn du nur eine Seite der Paare brauchst, verwende in der Schleife `keys()` oder `values()` statt `entries()`:
```javascript
let prices = new Map();
prices.set("tea", 2);
prices.set("cake", 4);
for (const name of prices.keys()) {
  console.log(name);
}
// prints tea
// prints cake
for (const price of prices.values()) {
  console.log(price);
}
// prints 2
// prints 4
```

---

Statt `set()` viele Male aufzurufen, kannst du eine Map auf einmal erstellen, indem du `new Map()` ein **Array von Paaren** übergibst:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Da `Object.entries(obj)` genau ein solches Array von Paaren zurückgibt, ist dies der schnellste Weg, ein Objekt in eine Map umzuwandeln:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
