Ein **Set** ist eine Sammlung von **eindeutigen** Werten: Jeder Wert kann höchstens einmal vorkommen, und es gibt keinen Index, um einen Wert über seine Position zu erreichen.
Sets sind perfekt, wenn dich nur interessiert, *welche* Werte vorhanden sind, nicht wie oft oder in welcher Reihenfolge.
Du erstellst ein leeres Set mit `new Set()`, fügst einen Wert mit `add(value)` hinzu und prüfst, ob ein Wert vorhanden ist, mit `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
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
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
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
// prints 3
```
Der **Spread**-Operator `...` funktioniert umgekehrt und verwandelt ein Set zurück in ein Array:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` macht dasselbe.

---

Ein Set merkt sich die Reihenfolge, in der Werte hinzugefügt wurden, und du kannst mit `for...of` darüber iterieren:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
Sets haben außerdem eine `forEach()`-Methode, die für jeden Wert eine Funktion aufruft:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
