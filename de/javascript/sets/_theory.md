Ein **Set** ist eine Sammlung von **eindeutigen** Werten: Jeder Wert kann höchstens einmal vorkommen, und es gibt keinen Index, um einen Wert über seine Position zu erreichen.
Sets sind perfekt, wenn dich nur interessiert, *welche* Werte vorhanden sind, nicht wie oft oder in welcher Reihenfolge.
Du erstellst ein leeres Set mit `new Set()`, fügst einen Wert mit `add(value)` hinzu und prüfst, ob ein Wert vorhanden ist, mit `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// gibt true aus
console.log(colors.has("green"));
// gibt false aus
```

---

Einen Wert hinzuzufügen, der bereits im Set enthalten ist, bewirkt **nichts**: Duplikate werden einfach ignoriert.
Zwei weitere wichtige Dinge:
- `delete(value)` entfernt den Wert aus dem Set
- `size` ist die Anzahl der gespeicherten Werte (eine Eigenschaft, also ohne Klammern)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// gibt 2 aus
tags.delete("css");
console.log(tags.size);
// gibt 1 aus
```

---

`add()` gibt das Set selbst zurück, sodass mehrere Aufrufe verkettet werden können:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Ob du verkettest oder nicht, ein Wert, der bereits vorhanden ist, wird nie ein zweites Mal hinzugefügt, sodass `size` jeden eindeutigen Wert nur einmal zählt.

---

Du kannst ein Set auf einen Schlag erstellen, indem du ein Array an `new Set()` übergibst. Duplikate im Array werden entfernt, das ist also der schnellste Weg, die eindeutigen Werte eines Arrays zu finden:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// gibt 3 aus
```
Der **Spread**-Operator `...` funktioniert umgekehrt und verwandelt ein Set zurück in ein Array:
```javascript
let unique = [...distinct];
console.log(unique);
// gibt [ 1, 2, 3 ] aus
```
`Array.from(distinct)` macht dasselbe.

---

Ein Set merkt sich die Reihenfolge, in der Werte hinzugefügt wurden, und du kannst mit `for...of` darüber iterieren:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// gibt 3 aus
// gibt 1 aus
// gibt 2 aus
```
Sets haben außerdem eine `forEach()`-Methode, die für jeden Wert eine Funktion aufruft:
```javascript
nums.forEach((n) => console.log(n * 10));
// gibt 30 aus
// gibt 10 aus
// gibt 20 aus
```

---

`delete(value)` gibt `true` zurück, wenn der Wert entfernt wurde, und `false`, wenn er nicht im Set war.
Um **alle** Werte auf einmal zu entfernen, rufe `clear()` auf:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// gibt true aus
console.log(cart.delete("pen"));
// gibt false aus
cart.clear();
console.log(cart.size);
// gibt 0 aus
```

---

Ein Set entscheidet mit fast derselben Regel wie `===`, ob zwei Werte "gleich" sind (außer dass `NaN` als gleich zu sich selbst zählt). Bei Strings und Zahlen wird dabei der Inhalt verglichen, aber **Objekte werden anhand ihrer Referenz verglichen**: zwei Objektliterale mit identischen Feldern sind zwei verschiedene Werte.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// gibt 1 aus
people.add({ name: "Alice" });
console.log(people.size);
// gibt 2 aus
```
Nur das erneute Hinzufügen genau desselben Objekts wird ignoriert.

---

Die Kombination von Spread und `filter()` liefert dir die klassischen Operationen der Mengenlehre. Jede davon erstellt eine **neue** Sammlung und lässt die Originale unverändert:
- **Vereinigung**, jeder Wert, der in `a`, in `b` oder in beiden ist: `new Set([...a, ...b])`
- **Schnittmenge**, nur die Werte, die in **beiden** sind: `[...a].filter((x) => b.has(x))`
- **Differenz**, die Werte von `a`, die **nicht** in `b` sind: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// gibt [ 1, 2, 3, 4 ] aus
console.log([...a].filter((x) => b.has(x)));
// gibt [ 3 ] aus
console.log([...a].filter((x) => !b.has(x)));
// gibt [ 1, 2 ] aus
```
Neuere JavaScript-Engines bieten außerdem `a.union(b)`, `a.intersection(b)` und `a.difference(b)` direkt auf Sets an, aber die Spread- und Filter-Varianten funktionieren überall.

---

Um dieselbe Schnittstelle wie `Map` beizubehalten, bietet ein Set die Iterator-Methoden `values()`, `keys()` und `entries()`.
Da ein Set keine Schlüssel hat, ist `keys()` nur ein anderer Name für `values()`, und `entries()` liefert jeden Wert **zweimal**, als `[value, value]`-Paar:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// gibt [ 'a', 'b' ] aus
console.log([...letters.entries()]);
// gibt [ [ 'a', 'a' ], [ 'b', 'b' ] ] aus
```
In der Praxis brauchst du sie selten: `for...of` und Spread iterieren bereits direkt über die Werte.

---

`new Set()` akzeptiert jedes **iterierbare Objekt**, nicht nur Arrays. Ein String ist zeichenweise iterierbar, sodass du damit die eindeutigen Zeichen eines Textes erhältst:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// gibt [ 'h', 'e', 'l', 'o' ] aus
```
