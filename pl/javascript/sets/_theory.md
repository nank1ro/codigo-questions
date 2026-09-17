**Set** to kolekcja **unikalnych** wartości: każda wartość może wystąpić co najwyżej raz i nie ma indeksu, za pomocą którego można by odczytać wartość według pozycji.
Sety są idealne, gdy zależy ci tylko na tym, *które* wartości są obecne, a nie ile razy ani w jakiej kolejności.
Tworzysz pusty set za pomocą `new Set()`, dodajesz wartość za pomocą `add(value)` i sprawdzasz, czy wartość jest obecna, za pomocą `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// wypisuje true
console.log(colors.has("green"));
// wypisuje false
```

---

Dodanie wartości, która już jest w secie, **nic** nie robi: duplikaty są po prostu ignorowane.
Jeszcze dwie istotne rzeczy:
- `delete(value)` usuwa wartość z setu
- `size` to liczba przechowywanych wartości (właściwość, więc bez nawiasów)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// wypisuje 2
tags.delete("css");
console.log(tags.size);
// wypisuje 1
```

---

`add()` zwraca sam set, więc kilka wywołań można łączyć w łańcuch:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Niezależnie od tego, czy łączysz wywołania w łańcuch, czy nie, wartość, która już jest obecna, nigdy nie zostanie dodana po raz drugi, więc `size` liczy każdą odrębną wartość tylko raz.

---

Możesz zbudować set za jednym razem, przekazując tablicę do `new Set()`. Duplikaty w tablicy są odrzucane, więc jest to najszybszy sposób na znalezienie odrębnych wartości tablicy:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// wypisuje 3
```
Operator **rozproszenia** `...` działa w drugą stronę i zamienia set z powrotem w tablicę:
```javascript
let unique = [...distinct];
console.log(unique);
// wypisuje [ 1, 2, 3 ]
```
`Array.from(distinct)` robi dokładnie to samo.

---

Set pamięta kolejność, w jakiej dodawano wartości, i możesz przejść przez niego za pomocą `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// wypisuje 3
// wypisuje 1
// wypisuje 2
```
Sety mają też metodę `forEach()`, która wywołuje funkcję dla każdej wartości:
```javascript
nums.forEach((n) => console.log(n * 10));
// wypisuje 30
// wypisuje 10
// wypisuje 20
```

---

`delete(value)` zwraca `true`, gdy wartość została usunięta, i `false`, gdy nie było jej w secie.
Aby usunąć **wszystkie** wartości naraz, wywołaj `clear()`:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// wypisuje true
console.log(cart.delete("pen"));
// wypisuje false
cart.clear();
console.log(cart.size);
// wypisuje 0
```

---

Set decyduje, czy dwie wartości są "takie same", niemal według tej samej reguły co `===` (z tą różnicą, że `NaN` liczy się jako równe samemu sobie). Dla stringów i liczb porównywana jest zawartość, ale **obiekty są porównywane przez referencję**: dwa literały obiektów o identycznych polach to dwie różne wartości.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// wypisuje 1
people.add({ name: "Alice" });
console.log(people.size);
// wypisuje 2
```
Ignorowane jest tylko ponowne dodanie dokładnie tego samego obiektu.

---

Połączenie rozproszenia i `filter()` daje ci klasyczne operacje teorii mnogości. Każda z nich buduje **nową** kolekcję i pozostawia oryginały niezmienione:
- **suma (unia)**, każda wartość, która jest w `a`, w `b` lub w obu: `new Set([...a, ...b])`
- **przecięcie (część wspólna)**, tylko wartości, które są w **obu**: `[...a].filter((x) => b.has(x))`
- **różnica**, wartości z `a`, których **nie ma** w `b`: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// wypisuje [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// wypisuje [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// wypisuje [ 1, 2 ]
```
Nowsze silniki JavaScript udostępniają też `a.union(b)`, `a.intersection(b)` i `a.difference(b)` bezpośrednio na setach, ale wersje z rozproszeniem i `filter()` działają wszędzie.

---

Aby zachować ten sam interfejs co `Map`, set udostępnia metody iteratorów `values()`, `keys()` i `entries()`.
Ponieważ set nie ma kluczy, `keys()` to po prostu inna nazwa dla `values()`, a `entries()` zwraca każdą wartość **dwa razy**, jako parę `[value, value]`:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// wypisuje [ 'a', 'b' ]
console.log([...letters.entries()]);
// wypisuje [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
W praktyce rzadko ich potrzebujesz: `for...of` i rozproszenie już przechodzą bezpośrednio po wartościach.

---

`new Set()` przyjmuje dowolny obiekt **iterowalny**, nie tylko tablice. String jest iterowalny znak po znaku, więc daje ci odrębne znaki tekstu:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// wypisuje [ 'h', 'e', 'l', 'o' ]
```
