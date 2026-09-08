**Set** to kolekcja **unikalnych** wartości: każda wartość może wystąpić co najwyżej raz i nie ma indeksu, za pomocą którego można by odczytać wartość według pozycji.
Sety są idealne, gdy zależy ci tylko na tym, *które* wartości są obecne, a nie ile razy ani w jakiej kolejności.
Tworzysz pusty set za pomocą `new Set()`, dodajesz wartość za pomocą `add(value)` i sprawdzasz, czy wartość jest obecna, za pomocą `has(value)`:
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
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
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
// prints 3
```
Operator **rozproszenia** `...` działa w drugą stronę i zamienia set z powrotem w tablicę:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` robi dokładnie to samo.

---

Set pamięta kolejność, w jakiej dodawano wartości, i możesz przejść przez niego za pomocą `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
Sety mają też metodę `forEach()`, która wywołuje funkcję dla każdej wartości:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
